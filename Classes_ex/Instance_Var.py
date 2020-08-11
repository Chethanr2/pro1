import pandas as pd

df = pd.read_excel('F:/Chethan/STUDY/Python notes/Selenium programs/VPSD/Stop_creation/Stops_Input.xlsx')
service_type = df['B'][7]

def Convt(str):
    li = list(str.split(","))
    print(type(li))
    print(len(li))
    return li

print(Convt(service_type))

color_code = df['B'][10]
print(color_code)
Color_code = df['B'][10]

if Color_code == 'Green':
    print("Its Green")
