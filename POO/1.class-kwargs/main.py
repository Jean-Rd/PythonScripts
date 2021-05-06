import student

persona = student.Persona(Name="Jean", LastName="Rada", Age=21)
estudiante = student.Student(Name='Anahi', LastName='Abigail')
profesional = student.Profesional(Name="Breta")

print(persona.get_infoPersona())

print("+"*40)

print(estudiante.get_infoEstudent(carrera='Ing.Sistemas'))

print('+'*40)

print(profesional.get_infoProfesional(carrera='Ing. Electrica', profesion='Lic. Economia', experiencia='Si'))