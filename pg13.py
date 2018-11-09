def switch_funct(value, x,y):
	return{
			'1': lambda x,y: x+y,
			'2': lambda x,y: x-y,
			'3': lambda x,y: x*y,
			'4': lambda x,y: x/y,
	}
    #.get(value)(x,y)
p = int(input("enter the choice 1/2/3/4"))
x = int(input("enter the first number"))
y = int(input("enter the second number"))
print(" the result of the given input is:", switch_funct(p, x,y)) 
'''def switch_func(value, x,y):
    return {
        'a': lambda x,y: x+y,
        'b': lambda x,y: x*y,
        'c': lambda x,y: x-y,
        'd': lambda x,y: x/y
    }.get(value)(x,y)

# take user input
inp = input('Input a operation Character : ')

print('The result for inp is : ', switch_func(inp, 4,8))'''