import numpy as np
import pandas as pd

class Condition:
    #Function to parse through the various conditions, and return the value that we need to add to 
    # he column, based on whichever condition it satisfies. 
    def parse_through_condition(self,cond,row_value):

        #Cond is a list of conditions, from which we need to pick up each condition, 
        #and evaluate the value based on that condition
        
        for j in cond: 
            #Taking each condition and evaluating the value based on that. 
            left_condition=j.left_cond
            right_condition=j.right_cond 
            left_sign=j.left_sign
            right_sign=j.right_sign 
            
            #Combining all the strings to give one big string 
            string_to_eval=str(left_condition)+str(left_sign)+str(row_value)+str(right_sign)+str(right_condition)

            #Evaluating that string using the eval function and then  returning the value to append to the 
            #column only if it is true otherwise moving on to the next condition 
            if(eval(string_to_eval)):
                return cond.val
        

        
    def condition(self,cond,name,pos,df):
            
        middle=cond.middle  
        
        #Removing the hashes from the ends of the middle column
        middle=middle[1:]
        middle=middle[:-1]

        col=df[middle][1:]    #Column which has the data to input. 

        results=[] #Results to append to so that we can add this column to the final df.

        #iterating through each row value in the column that we have, and appending 
        for row_value in col:
                results.append(self.parse_through_condition(cond,row_value))
        #NOW WE NEED TO CONVERT RESULTS TO A DF COLUMN AND APPEND IT TO THE DATAFRAME
        #Unsure as to how to proceed in this 
        self.add_column(results,name,df,pos)
                

    

        
     #adding column to dataframe
    
    def add_column(self, new_col_val, name, df, position):
        
        if position["deet"] == "after":
            loc = list(df.columns).index(position["col"]) + 1
            df.insert(loc, name, new_col_val)
        elif position["deet"] == "before":
            loc = list(df.columns).index(position["col"])
            df.insert(loc, name, new_col_val)
        elif position["deet"] == "beg":
            df.insert(0, name, new_col_val)
        elif position["deet"] == "end":
            df[name] = new_col_val
        