string=raw_input("Enter the string to be converted: ")

for i in range (0,len(string)):

   x=ord(string[i])
   if x>=97 and x<=122:
       x=x-32
   elif x<=97 :
       x=x+32
   y=chr(x)
   print(y)
   
  # y=chr(x)
  # print(y)
   