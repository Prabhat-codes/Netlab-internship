    cond=cond["config"]["condition"]
    final=[]
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

  

    for i in df.index:
        mid_val=df[middle][i]
        check=str(left_condition)+str(left_sign)+str(mid_val)+str(right_sign)+str(right_condition)

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
    df.head()
