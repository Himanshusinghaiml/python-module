class student:
    stu_name=''
    stu_location=''
    def show(self):
        print(self.stu_location,self.stu_name)
obj=student()
obj.stu_location='location'
obj.stu_name='himanhsu singh '
obj.show()


class test:
    def __init__(self,name,location,degree) -> None:
        self.name=name
        self.location=location
        self.degree=degree
    def showtest(self):
        print(f'{self.degree}    {self.name}    {self.location}')
a=test('himanhsu singh','varanasi','btech degree')
print(a.degree)
a.showtest()