"""
def log_function(func):
    def greeting(*args,**args2):
        print("Calling function:{func._name_}")
        result=func(*args,**args2)
        print("function name:{func._name_}")
        return result 
return greeting
"""