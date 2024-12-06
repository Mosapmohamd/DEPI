class Calculator:
    def add (self,x,y):
        return x+y
    def sub (self,x,y):
        return x-y
    def mult (self,x,y):
        return x*y
    def div (self,x,y):
        if y==0:
            return "Error!, You can't division by Zero"
        else:
            return x/y