import pandas as pd
import numpy as np
from .utilities import CreateChartUtilities()
from .msg import Message

##################### Create  a chart #####################
class CreateChart:
    df = "" #will store the dataframe
    details = "" #will store json config
    m = Message()
    
    def __init__(self, df, details):
        self.details = details
        self.df = df
    
    def add_pivot_table(self):
        a=CreateChartUtilities()
        msg=a.create_chart(self.details,self.df)
        return msg
    