def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b

print("select the operation to be performed")
print("1 - Addition")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

choice = int(input("enter choice 1/2/3/4:"))

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))

if choice == 1:
	print(a,'+',b,"=",add(a,b))
elif choice == 2:
	print(a,"-",b,"=",sub(a,b))
elif choice == 3:
	print(a,"*",b,"=",mul(a,b))
elif choice == 4:
	print(a,"/",b,"=",div(a,b))
else:
	print("Invalid input")
