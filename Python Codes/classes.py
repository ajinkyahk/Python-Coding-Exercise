class Employee :

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    def display_employee(self):
        print(self.name, self.age, self.gender)



em_data= Employee(
    name="ajinkya",
    age=32,
    gender="male"
)
em_data.display_employee()


