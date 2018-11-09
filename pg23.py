a=raw_input("enter a text")
appendMe = a
appendFile = open('friends.txt','a')
appendFile.write(appendMe)
appendFile.close()