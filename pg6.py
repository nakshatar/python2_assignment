#append/create/sort/reverse_sort in agiven list
list =["EWT","VLSI","VIR","ES"]
print("the initial elements of the list are:\t")
print(list)
list.append('BIGDATA')
print("the elements of the list after appending are:\t")
print(list)
list.insert(3,'CL')
print("the elements of the list after inserting")
print(list)
print("here are the elements of the list after sorting")
for branch in sorted(list):
	print(branch.title())
print("here is the elements of the list after reverse sorting")
for branch in sorted(list,reverse=True):
	print(branch.title())