file = open("File handeling/newfile.txt",'r')
data =file.read()
file.close()

file = open("File handeling/newfile1.txt",'w')

# data = "Welcome to our python programming class"
# data1 = "Welcome to our Java programming class"

file.write(data)
print("File written successfully ")
file.close()