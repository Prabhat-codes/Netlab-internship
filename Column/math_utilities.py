import numpy as np
import pandas as pd

class MathUtilities:

    #parenthesis checker
    def parenthesis_checker(self, formula):
        open_list = ["[","{","("]
        close_list = ["]","}",")"]
        
        stack = []
        for i in formula:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                pos = close_list.index(i)
                if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack)-1])):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


    #==========================================================================================================#
    #basic modifications on the formula for easier parsing    
    def modify_formula(self, formula):
        #add brackets
        formula = '((' + formula + '))'
        
        #add spaces
        new_formula = ''
        open_bracket = '('
        close_bracket = ')'
        operations = ['+', '-', '*', '/', '^']
        
        for f in formula:
                if f == open_bracket:
                    new_formula+=f
                    new_formula+=" "
                elif f == close_bracket:
                    new_formula+=" "
                    new_formula+=f
                elif f in operations:
                    new_formula+=" "
                    new_formula+=f
                    new_formula+=" "
                else:
                    new_formula+=f
        
        return new_formula
    
    
    #==========================================================================================================#
    #infix to postfix for better parsing of the formula
    
    def infix_to_postfix(self, expression):
        expression = self.modify_formula(expression)
        OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])  # set of operators
        PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities 
        
        stack = [] # initially stack empty
        output = '' # initially output empty

        for ch in expression:
    
            if ch not in OPERATORS:  # if an operand then put it directly in postfix expression
                output+= ch
    
            elif ch=='(':  # else operators should be put in stack
                stack.append('(')
    
            elif ch==')':
                while stack and stack[-1]!= '(':
                    output+=stack.pop()
                stack.pop()
    
            else:
                # lesser priority can't be on top on higher or equal priority    
                 # so pop and put in output   
                while stack and stack[-1]!='(' and PRIORITY[ch]<=PRIORITY[stack[-1]]:
                    output+=stack.pop()
                stack.append(ch)
    
        while stack:
            output+=stack.pop()
        return self.infix_to_list(output)
    
    
    #==========================================================================================================#
    
    #infix to postfix output to list for better parsing
    def infix_to_list(self, s):
        i = 0
        ll = []

        while i<len(s):
            if s[i] == '#':
                #get entire word till # reached
                #add in list
                i+=1
                w = "#"
                while s[i]!="#":
                    w+=s[i]
                    i+=1
                ll.append(w)
                i+=1
            elif s[i] == " ":
                i+=1;
                continue
            else:
                #get entire number or operation till empty space reached
                #add in list
                w = ""
                while s[i]!=" ":
                    w+=s[i]
                    i+=1
                ll.append(w)
                
        return ll
    
    
    #==========================================================================================================#
    #validating formula (checking for parenthesis, column names and column datatypes
    
    def validate_formula(self, formula,df):
        datatype = {"INT_DATA_TYPE": "int", "FLOAT_DATA_TYPE" : "float", "OBJECT_DATA_TYPE" : "object", "BOOLEAN_DATA_TYPE" : "bool"}
        
        if self.parenthesis_checker(formula)==False:
            return {"val" : False, "detail" : "Parenthesis checker fail"}
        
        ll = self.infix_to_postfix(formula)
        for i in ll:
            if i[0]=='#':
                if i[1:] not in list(df.columns):
                    return {"val" : False, "detail" : "Column name wrong"}
                elif (df[i[1:]].dtype == datatype["OBJECT_DATA_TYPE"]) or (df[i[1:]].dtype == datatype["BOOLEAN_DATA_TYPE"]):
                    return {"val" : False, "detail": "Column data type wrong"}
        return {"val" : True, "detail": ll}
    
    #==========================================================================================================#
    #calculating the column value using the formula

    def get_math_result(self,infix_list, df):
        stack = []
        operations = ['+', '-', '*', '/', '^']                                                                   
        length = len(infix_list)
        i = 0
                                                                           
        while i<length:
            if infix_list[i] in operations:
                a = stack.pop()
                b = stack.pop()
                op = infix_list[i]
                
                if type(a)==str:
                    a = float(a)
                if type(b)==str:
                    b = float(b)
                        
                if op=='+':
                    stack.append(a+b)
                elif op=='-':
                    stack.append(b-a)
                elif op=='/':                                      
                    stack.append(b/a)
                elif op=='*':                                       
                    stack.append(b*a)
                elif op=='^':
                    stack.append(b^a)
                                                                           
            elif infix_list[i][0]=="#":
                stack.append(df[infix_list[i][1:]])
            else:
                stack.append(infix_list[i])
            i+=1
                                                                           
        return stack[0]
    
    #==========================================================================================================#
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
