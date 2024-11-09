def Transform(a, b):
    a += b
    return a

print(Transform(45,67))


class School:
    def __init__(self, location, name, classsize) -> None:
        self.location = location
        self.name = name
        self.classsize = classsize

    def canEducate(self, speciality):
        return f" The {self.name} school located at {self.location} is specialized in teaching {speciality}"
    

class PrivateSchool(School):
    def __init__(self, location, name, classsize, privatelounge) -> None:
        self.location = location
        self.name = name
        self.classsize = classsize
        self.privatelounge = privatelounge

    def canTutor(self):
        return f" The {self.name} school has a private lounge located at {self.privatelounge} for  parents"

        #super().__init__(location, name, classsize, privateLounge)



NorthDallasSchool = PrivateSchool('White-rock','Eduardo-mata',200,'GardensLounge')
print(NorthDallasSchool.canTutor())


DallasSchool = School('Sooth Dallas','Wilmer-Hutchins',400)
print(DallasSchool.canEducate('Math'))