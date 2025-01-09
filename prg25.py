class person:
    def init (self,name,age):
        self.name=name
        self.age=age 
    def display(self):
        print("name is:",self.name)
        print("age is:",self.age)
p1=person("sanju",23)
p1.display()