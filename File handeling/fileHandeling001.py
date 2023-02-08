# access mode - read(r),write(w),append(a),wb,rb,ab
file = open("File handeling/newfile.txt",'r')
# data = file.read()
# data = file.read(10)
# data = file.readline()
data = file.readlines()
for line in data:
    print(line,end="")
file.close()