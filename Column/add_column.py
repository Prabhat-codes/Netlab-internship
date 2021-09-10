import pandas as pd
import numpy as np
from math_utilities import MathUtilities
from add_cond import Condition

class AddColumn:
    df = "" #will store the dataframe
    details = "" #will store json config
    math_utility = MathUtilities() #utilities object
    
    def __init__(self, df, details):
        self.details = details
        self.df = df
        
    def add_cond(self):
        name=self.details["name"]
        pos=self.details["position"]
        cond=self.details["config"]["condition"]
        #write code based on condition here
        c=Condition()
        c.condition(cond,name,pos,df)
        return "newdf"
    '''
    JSON 1
{
	"group" : "column operations",
	"task" : "add",
	"name" : "Ageing",
	"position":{
		"col" : ""
		"deet" : "before" 
	},
	"config" : {
		"condition": [{"left_cond":0, "left_sign":"<", "middle":"#Pending Days#", "right_sign":"<=", "right_cond":10, "val":"0 to 10"}, 
        {left_cond:10, left_sign:"<", middle:"#Pending Days#", right_sign:"<=", right_cond:30, val:"10 to 30"}, 
        {left_cond:30, left_sign:"<", middle:"#Pending Days#", right_sign:"<=", right_cond:45, val:"30 to 45"}, 
        {"left_cond":45, "left_sign":"<", "middle":"#Pending Days#", "right_sign":"NA", "right_cond":NA, "val":"greater than 45"}],
		"math": "NA",
		"condmath": "NA"
	}
}
'''
    def add_math(self):
        #write code based on math here
        name = self.details["name"]
        formula = self.details["config"]["math"]
        val = self.math_utility.validate_formula(formula, self.df)
        if val["val"]:
            new_col_val = self.math_utility.get_math_result(val["detail"], self.df)
            self.math_utility.add_column(new_col_val, name, self.df, self.details["position"])
            return {"val":True, "detail":self.df}
        else:
            return val
    
    def add_cond_math(self):
        #write code based on cond_math here
        return "new df"

    
    
'''
MATH JSON EXAMPLE
{
    "group" : "column operations",
    "task" : "add",
    "position" : {
        "col" : "Canceled", #col name before or after stuff has to be added (will be ignored when deet = end or beg)
        "deet" : "end" #after, before, beg, end
    },
    "name" : "Math Test",
    "config" : {
        "condition" : "NA",
        "math": "(#Total Days#+2)*#PO Number#",  #formula with column name encapsulated in '#'
        "condmath": "NA"
    }
}



'''
