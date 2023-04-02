"""print("nguyen duy quang")

a = 23
a +=1
print('aloze '+ str(a))

"""#name=input("What is your name?:")
#print("Hello "+name)
"""
List = ["nguyen", " my", " Linh"]
List[0] = "Tran"
print(List)

List.append("quang")
print(List)

first_name =["nguyen", "tran", "le", "Vu"]
last_name = ["Quang","Linh","Ha","Nhi"]
mid_name = ["van", "thi", "my"]

name =[first_name, mid_name, last_name]

print(name)

dictionary_list = {'USA':'Washinton DC',
                   "VietNam":'Ha noi',
                   'Indian':'New Dehli'
                   }

print(len(dictionary_list))
print(dictionary_list)

for key,value in dictionary_list.items():
    print(key, value)

dictionary_list.update({'Korea':'seoul'})
print(dictionary_list)"""

name = 'Nguyen Duy Quang'

if (name[0].islower()):
    name = name.capitalize()
print(name)