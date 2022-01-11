class Persona:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def setName(self,nuevoName):
        self.name=nuevoName

    def setAddress(self,nuevoAddress):
        self.address=nuevoAddress
    def __str__(self):
        return "El nombre de la persona es: %s"
        + "\nLa direccion es: %s" % (str(self.name),self.address)

class Student (Persona):
    def __init__(self,program,year,fee):
        self.program=program
        self.year=year
        self.fee= fee
    
    def getProgram(self):
        return self.program
    def getYear(self):
        return self.year
    def getFee(self):
        return self.fee
    
    def setProgram(self,nuevoProgram):
        self.program=nuevoProgram

    def setYear(self,nuevoYear):
        self.year=nuevoYear

    def setFee(self,nuevoFee):
        self.fee=nuevoFee
    
class Staff (Persona):
    def __init__(self,school,pay):
        self.school=school
        self.pay=pay

    def getSchool(self):
        return self.school

    def getPay(self):
        return self.pay
    
    def setSchool(self,nuevaSchool):
        self.school=nuevaSchool

    def setPay(self,nuevoPay):
        self.pay=nuevoPay



class Principal:

    person= Persona("Ozuna","Barrio España")
    print(person.getName(), person.getAddress())

    Org=Staff("Foundation School", 25000)
    print(person.getName(),person.getAddress(),Org.getSchool(),Org.getPay())

    student=Student("Desarrollo",2019,250.90)
    print(person.getName(),person.getAddress(),student.getProgram(), student.getYear(),student.getFee())
