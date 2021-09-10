import numpy as np
import pandas as pd
import math
from .msg import Message

class AddPivotUtilities:
    def column_exists_validator(self, column_list, df):
        m = Message()
        for i in column_list:
            if i not in list(df.columns):
                return m.msg(False, "Column doesn't exist")
        return m.msg(True, "")
    
    def pivot_add(self,cond,df):
        
        m=Message()

        col=cond["config"]["column"]
        msg=self.column_exists_validator(col,df)
        if not msg["val"]:
            return msg

        ind=cond["config"]["indexes"]
        msg=self.column_exists_validator(ind,df)
        if not msg["val"]:
            return msg

        value=cond["config"]["value"]
        msg=self.column_exists_validator(value,df)
        if not msg["val"]:
            return msg

        agg_func=cond["config"]["agg_func"]

        grd_total=cond["config"]["grand total column and row"]

        if agg_func=="distinct count":
            table=pd.pivot_table(data=df,index=ind,values=value,columns=col,aggfunc=pd.Series.nunique)    
        else :
            table=pd.pivot_table(data=df,index=ind,values=value,columns=col,aggfunc=[agg_func])
        
        if grd_total=="True":
            table["Grand Total"]=table.sum(axis=1)
            #Need to add the row of grand total here
        return table