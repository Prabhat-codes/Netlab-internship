#copy all of this to remove.py
import pandas as pd
import numpy as np

class Remove_Row:
    #Function to remove full blank rows. 
    def column_exists_validator(self, cond, df):
        print('I validate stuff')
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
    def fully_blank_rows(self,df):
        data=df
        data = pd.read_csv(file_path,skip_blank_lines=True)

        #so here we have to use skip_blank_lines wherever we first import the data at,
        #so that this is automatically done and we dont need to pass the filepath to this all over again. 
        data.dropna(how="all", inplace=True)
        return data #Just check if returning data like this is alright

        #assuming we get cond in the form cond["config"]["selected_blanks"]["column_list"]
    def remove_selected_blanks(self,cond,df):

        #check if the column list contains columns that actually exist. 
        df.dropna(subset=cond,inplace=True)
        return df
        #here in cond we have to accept the list of columns in the format 
        #cond=["XYZ","ABC","DEF"]


    def conditional_removing_blanks(self,cond,df):
        
        mesg=self.column_exists_validator(cond,df) 
        if not mesg["val"]:
            return msg
        #Checking columns exist or not 


        #If the middle column is empty, we fill them up 
        d_mid=df[cond["column"][1:-1]]
        if d_mid.dtype=="object":
            d_mid = d_mid.fillna(value="")
        if d_mid.dtype == 'float':
            d_mid = d_mid.fillna(value=0.0)
        if d_mid.dtype == 'int':
            d_mid = d_mid.fillna(value=0)

        middle_vals=list(d_mid)
        #Checking if the left and the right conditions are columns or, values 

        left_vals = []
        right_vals = []
        try:
            if cond["left_cond"][0] == "#":
                d_left = df[cond["left_cond"][1:-1]]
                if df[cond["left_cond"][1:-1]].dtype == 'object':
                    d_left = d_left.fillna(value="")
                elif df[cond["left_cond"][1:-1]].dtype == 'float':
                    d_left = d_left.fillna(value=0.0)
                elif df[cond["left_cond"][1:-1]].dtype == 'int':
                    d_left = d_left.fillna(value=0)
                left_vals = list(d_left)
        except:
            print('')
        
        try:
            if cond["right_cond"][0] == "#":
                d_right = df[cond["right_cond"][1:-1]]
                if df[cond["right_cond"][1:-1]].dtype == 'object':
                    d_right = d_right.fillna(value="")
                elif df[cond["right_cond"][1:-1]].dtype == 'float':
                    d_right = d_right.fillna(value=0.0)
                elif df[cond["right_cond"][1:-1]].dtype == 'int':
                    d_right = d_right.fillna(value=0)
                right_vals = list(d_right)
        except:
            print('')
        

        final=[]

        for i in range(leng(middle_vals)):
            cnt=0

            left_condition=cond["left_cond"]
            right_condition=cond["right_cond"]
            left_sign=cond["left_sign"]
            right_sign=cond["right_sign"]

            if left_vals!=[]:
                left_condition=left_vals[i]
            if right_vals!=[]:
                right_condition=right_vals[i]

            if left_condition == "NA":
                        left_condition = ""
                    if right_condition == "NA":
                        right_condition = ""
                    if left_sign == "NA":
                        left_sign = ""
                    if right_sign == "NA":
                        right_sign = ""
                        
            middle = middle_vals[i]

            eval_str = self.get_eval_str(left_condition, left_sign, middle, right_sign, right_condition)
    
            if eval(eval_str):
                final.append(j["val"])
                break
            cnt+=1
            if cnt == len(cond):
                final.append("")
    return final
        
    #generating string for the er    
    def get_eval_str(self, lc, ls, v, rs, rc):
        return str(lc)+str(ls)+str(v)+str(rs)+str(rc)


        