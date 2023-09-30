class student:

    def __init__(self):
        self._name= " "

    def getname(self):
        return self._name
    
    def setname(self,name):
        self._name=name

obj=student()
obj.setname("avnish")
ans=obj.getname()
print(ans)
