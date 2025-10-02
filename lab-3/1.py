class InputString:
   def __init__(self):
       self.s = ""
   def getString(self):
       self.s = input("Enter a string: ")
   def printString(self):
       # Print the string in upper case
       print(self.s.upper())
print()
str_obj = InputString()
str_obj.getString()
str_obj.printString()