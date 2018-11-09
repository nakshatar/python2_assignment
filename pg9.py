#dictionary for registration and name and perform operatons(insert and delete)
my_dict= {181040009:'Nakshatra',181040010:'rachana'}
print("elements before the operations are performed")
print(my_dict)
#inserting an elemnt
my_dict[181040008]='pooja'
print("elements after insertion")
print(my_dict)
# delete an element
del my_dict[181040008]
print("elements after deletion")
print(my_dict)