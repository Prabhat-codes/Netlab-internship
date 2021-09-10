import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from .msg import Message

class CreateChartUtilities:
    def column_exists_validator(self, column, df):
        m = Message()
        if column not in list(df.columns):
            return m.msg(False, "Column doesn't exist")
        return m.msg(True, "")

    def create_chart(self,cond,df):
        
        m=Message()
        col=cond["config"]["column"]
        msg=self.column_exists_validator(col,df)
        if not msg["val"]:
            return msg
       
        kind=cond["config"]["kind"]
        number=cond["config"]["number"]
        size_x=cond["config"]["size_x"]
        size_y=cond["config"]["size_y"]
        top=cond["config"]["top"]
        try:
            if top=="True":
                chart=b.value_counts().head(int(number)).plot(kind=kind,figsize=(int(size_x),int(size_y)))
            else:
                chart=b.value_counts().tail(int(number)).plot(kind=kind,figsize=(int(size_x),int(size_y)))
        except:
            return m.msg(False,"Chart cannot be plotted")

        return chart