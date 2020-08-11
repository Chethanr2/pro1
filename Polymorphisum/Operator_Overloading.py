class Student:

    def __init__(self, mark1, mark2):
        self.m1 = mark1
        self.m2 = mark2

        print(self.m1,self.m2)

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2

        m3 = Student(m1,m2)

        return m3

    def __ge__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)

s1 = Student(45,67)
s2 = Student(55,78)

s3 = s1 + s2

if s1 >= s2:
    print("S1 wins")
else:
    print("S2 wins")

print(s1)
print(s2)