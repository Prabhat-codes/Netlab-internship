import numpy as np
import pandas as pd
import math
from .msg import Message

class FilterUtilities:
    def column_exists_validator(self, col, df):
        m = Message()
        if col not in list(df.columns):
            return m.msg(False, "Column doesn't exist")
        return m.msg(True, "")
    
    def select_unique_values(self,cond,df):
        m=Message()
        col=cond["config"]["choose"]["column"]
        msg=self.column_exists_validator(col,df)
        if not msg["val"]:
            return msg
        to_filter=cond["config"]["choose"]["selected"]
        df=df[~df[col].isin(to_filter)]
        return df




    def filter_data(self,cond,df):
        m=Message()
        df["satisfy"]=None
        df["satisfy"]=df["satisfy"].astype(bool)
        col=cond["config"]["search"]["column"]
        msg=self.column_exists_validator(col,df)
        if not msg["val"]:
            return msg
        key=cond["config"]["search"]["keyword"]
        option=cond["config"]["search"]["option"]
        remove=cond["config"]["search"]["remove"]
        

        for i in range(len(df)):
            check=df[col][i]    
            
            if option=="starts with":
                if check.startswith(key):
                    df["satisfy"][i]=True
            elif option=="contains":
                if key in str(check):
                    df["satisfy"][i]=True
            elif option=="ends with":
                if check.endswith(key):
                    df["satisfy"][i]=True

        if remove==True:
            df=df[df["satisfy"]]
        else:
            df=df[~df["satisfy"]]

        df=df.drop("satisfy",axis="columns")
        return df