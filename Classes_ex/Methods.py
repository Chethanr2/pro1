class Students:

    School = 'NEC'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    @classmethod
    def info(cls):
        return cls.School

    @staticmethod
    def Clg_Info():
        print("NEC technologies")

s1 = Students(28,49,50)
s2 = Students(33,69,90)

print(s1.m1,s1.m2,s1.m3)
print(Students.info())
Students.Clg_Info()

