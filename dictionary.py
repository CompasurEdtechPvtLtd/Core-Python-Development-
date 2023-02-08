Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={"Name":"Navya"}
>>> type(d)
<class 'dict'>
>>> d={"id":101,"Name":"Navya","Marks":98}
>>> #how to add new key value pair
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d[0]
KeyError: 0
>>> d
{'id': 101, 'Name': 'Navya', 'Marks': 98}
>>> d["Phone":9876543210]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d["Phone":9876543210]
TypeError: unhashable type: 'slice'
>>> d["Phone"]=9876543210
>>> d
{'id': 101, 'Name': 'Navya', 'Marks': 98, 'Phone': 9876543210}
>>> d["Name"] = "Navya Gosain"
>>> d
{'id': 101, 'Name': 'Navya Gosain', 'Marks': 98, 'Phone': 9876543210}
>>> #insert,update
>>> d
{'id': 101, 'Name': 'Navya Gosain', 'Marks': 98, 'Phone': 9876543210}
>>> d.pop("Phone")
9876543210
>>> d
{'id': 101, 'Name': 'Navya Gosain', 'Marks': 98}
>>> d.pop(id)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d.pop(id)
KeyError: <built-in function id>
>>> d.pop('id')
101
>>> d
{'Name': 'Navya Gosain', 'Marks': 98}
>>> d={'id': 101, 'Name': 'Navya', 'Marks': 98, 'Phone': 9876543210}
>>> d
{'id': 101, 'Name': 'Navya', 'Marks': 98, 'Phone': 9876543210}
>>> d.popitem()
('Phone', 9876543210)
>>> d
{'id': 101, 'Name': 'Navya', 'Marks': 98}
>>> d.popitem()
('Marks', 98)
>>> d
{'id': 101, 'Name': 'Navya'}
>>> del d["Name"]
>>> d
{'id': 101}
>>> d.popitem()
('id', 101)
>>> d={'id': 101, 'Name': 'Navya', 'Marks': 98, 'Phone': 9876543210}
>>> d.clear()
>>> d
{}
>>> d
{}
>>> del d
>>> d
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> x={'id': 101, 'Name': 'Navya', 'Marks': 98, 'Phone': 9876543210}
>>> x.keys()
dict_keys(['id', 'Name', 'Marks', 'Phone'])
>>> x.values()
dict_values([101, 'Navya', 98, 9876543210])
>>> x.items()
dict_items([('id', 101), ('Name', 'Navya'), ('Marks', 98), ('Phone', 9876543210)])
>>> x
{'id': 101, 'Name': 'Navya', 'Marks': 98, 'Phone': 9876543210}
>>> x.get("id")
101
>>> x.get("Name")
'Navya'
>>> 