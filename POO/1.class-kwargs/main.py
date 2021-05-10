import student

persona = student.Persona(Name="Jean", LastName="Rada", Age=21)
estudiante = student.Student(Name='Anahi', LastName='Abigail', carrera='Ing. Sistemas')
profesional = student.Profesional(carrera='Economia', profesion='Ing. Civil', experiencia='No', Name="Breta")

print(persona.get_infoPersona())

print("+"*40)

print(estudiante.get_infoEstudent())

print('+'*40)

print(profesional.get_infoProfesional())