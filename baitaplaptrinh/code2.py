import numpy as np


class Student:
    def __init__(self, name, age, math_score, literature_score):
        self.name = name
        self.age = age
        self.math_score = math_score
        self.literature_score = literature_score
        self.average_score()

    def average_score(self):
        self.ave_score = (self.math_score + self.literature_score) / 2
        return self.ave_score

    def xuat(self):
        return ('ten : {} ,'
                'tuoi : {} ,'
                'diem toan: {} ,'
                'diem van: {} ,'
                'TBM : {} '.format(self.name,self.age,self.math_score,self.literature_score,self.ave_score))

def main():
    a = Student('Vu Duc Quang', 20, 9, 8)
    b = Student('Nguyen Thi Sen',20,9,9)
    c = Student('Mai Thi Huong',20,9,8)
    Students = []
    Students.append(a)
    Students.append(b)
    Students.append(c)
    for i in range(len(Students)):
        print(Students[i].xuat())

main()














