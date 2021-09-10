import pandas as pd
import numpy as np
from .utilities import AddPivotUtilities
from .msg import Message

##################### Create  a pivot table #####################
class AddPivotTable:
    df = "" #will store the dataframe
    details = "" #will store json config
    m = Message()
    
    def __init__(self, df, details):
        self.details = details
        self.df = df
    
    def add_pivot_table(self):
        a=AddPivotUtilities()
        msg=a.pivot_add(self.details,self.df)
        return msg
    