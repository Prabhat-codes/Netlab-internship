def column_exists_validator_conditional_blank_removal(self, cond, df):
        
        #if column doesn't exist 
        flag = True
        if cond["column"][1:-1] not in list(df.columns):
            flag = False
        try: 
            if cond["left_cond"][0] == '#':
                if cond["left_cond"][1:-1] not in list(df.columns):
                    flag = False
        except:
            print()
        
        try: 
            if cond["right_cond"][0] == '#':
                if cond["right_cond"][1:-1] not in list(df.columns):
                    flag = False
        except:
            print()
        
        if flag:
            return {"val" : flag, "details": ""}
        else:
            return {"val" : flag, "details":"column doesn't existing"}

#Assumed that cond is cond[config][condition]
def conditional_removing_blanks_append_new_column(self,cond,df):
    final=[]

    mesg=self.column_exists_validator_conditonal_blank_removal(cond,df) 
        if not mesg["val"]:
            return msg
    
    left_condition=cond["left_cond"]
    right_condition=cond["right_cond"]
    left_sign=cond["left_sign"]
    right_sign=cond["right_sign"]
    middle=cond["column"][1:-1]


    #If the middle column is empty, we fill them up 
    d_mid=df[cond["column"][1:-1]]
    if d_mid.dtype=="object":
        d_mid = d_mid.fillna(value="")
    if d_mid.dtype == 'float':
        d_mid = d_mid.fillna(value=0.0)
    if d_mid.dtype == 'int':
        d_mid = d_mid.fillna(value=0)
    middle_vals=list(d_mid)

    # left_vals = []
    # right_vals = []
    # try:
    #     if cond["left_cond"][0] == "#":
    #         d_left = df[cond["left_cond"][1:-1]]
    #         if df[cond["left_cond"][1:-1]].dtype == 'object':
    #             d_left = d_left.fillna(value="")
    #         elif df[cond["left_cond"][1:-1]].dtype == 'float':
    #             d_left = d_left.fillna(value=0.0)
    #         elif df[cond["left_cond"][1:-1]].dtype == 'int':
    #             d_left = d_left.fillna(value=0)
    #         left_vals = list(d_left)
    # except:
    #     print('')

    # try:
    #     if cond["right_cond"][0] == "#":
    #         d_right = df[cond["right_cond"][1:-1]]
    #         if df[cond["right_cond"][1:-1]].dtype == 'object':
    #             d_right = d_right.fillna(value="")
    #         elif df[cond["right_cond"][1:-1]].dtype == 'float':
    #             d_right = d_right.fillna(value=0.0)
    #         elif df[cond["right_cond"][1:-1]].dtype == 'int':
    #             d_right = d_right.fillna(value=0)
    #         right_vals = list(d_right)
    # except:
    #     print('')


#Based on the truth or false values based on, the last column that we append at the end of the df, we will remove values.
# In that, we'll also have to consider the fact that we might want to remove everything other than the said rows, therefore we must check for the truth or false values of the cond["remove"]

    for i in df.index:
        mid_val=df[middle][i]
        check=str(left_condition)+str(left_sign)+str(mid_val)+str(right_sign)+str(right_condition)
        # if (left_vals != []) and (right_vals == []):
        #         eval_str = "left_vals[i]" + str(left_sign) + "middle_vals[i]" + str(right_sign) + str(right_condition)
        # elif (right_vals != []) and (left_vals == []):
        #     eval_str = str(left_condition) + str(left_sign) + "middle_vals[i]" + str(right_sign) + "right_vals[i]"
        # elif (left_vals != []) and (right_vals != []):
        #     eval_str = "left_vals[i]" + str(left_sign) + "middle_vals[i]" + str(right_sign) + "right_vals[i]"
        # elif (left_vals == []) and (right_vals == []):
        #     eval_str = str(left_condition) + str(left_sign) + "middle_vals[i]" + str(right_sign) + str(right_condition)
        if eval(check):
            final.append(True)
        else:        
            final.append(False)


    df["ToRemove"]=pd.DataFrame(final)
    removal=cond["remove"]
    removal=str(removal)
    if (removal=="True"):
        rows_to_remove=df[df['ToRemove']==True].index
        df.drop(rows_to_remove,inplace=True)
        
    else:
        rows_to_remove=df[df['ToRemove']==False].index
        df.drop(rows_to_remove,inplace=True)

    df.drop(columns=["ToRemove"],inplace=True)
    
