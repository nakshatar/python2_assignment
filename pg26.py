String=raw_input("Enter the string to be converted uppercase: ")
print("the string after getting converted to uppercase")
for i in range (0,len(String)):
   x=ord(String[i])
   if x>=97 and x<=122:
       x=x-32
   y=chr(x)
   print(y)
