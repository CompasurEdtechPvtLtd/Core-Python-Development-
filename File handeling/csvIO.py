import csv
data=[
        {"id":101,"Name":"Navya","Marks":90},
        {"id":102,"Name":"Sahil","Marks":80},
        {"id":103,"Name":"Vishal","Marks":40},
        {"id":104,"Name":"Navya","Marks":30},
        {"id":105,"Name":"Navya","Marks":100}
    ]

# with open("File handeling/excel.csv",'w') as file:
#     writer = csv.writer(file)
#     for item in data:
#         writer.writerow(item.values())

with open("File handeling/excel.csv",'r') as file:
    reader = csv.reader(file)
    for item in data:
        print(item)
