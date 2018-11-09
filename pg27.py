String=raw_input("Enter the string to be converted lowercase: ")
print("string after getting converted to lower case")
for i in range (0,len(String)):

   x=ord(String[i])
   if x<=97: 
       x=x+32
   y=chr(x)
   print(y)