class InputString:
   def __init__(self):
       self.s = ""
   def getString(self):
       self.s = input("Enter a string: ")
   def printString(self):
       print(self.s.upper())
print()
str_obj = InputString()
str_obj.getString()
str_obj.printString()