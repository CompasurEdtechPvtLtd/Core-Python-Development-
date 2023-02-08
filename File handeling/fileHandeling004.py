import os
with open("File handeling/bg.jpg","rb") as file:
    data = file.read()

with open("File Handeling/bg001.jpg",'ab') as file:
    file.write(data)
    file.write(data)
    file.write(data)

x = os.path.getsize("File handeling/bg001.jpg")
print(f"{x} bytes")