from student import Student

estudiante = Student(Name='Jean', LastName='Rada', Age=21, University="UPEA")

print(estudiante.get_info())

print("+"*30)

estudiante_2 = Student(Name="Maria", Age=16)

print(estudiante_2.get_info())