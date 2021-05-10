
class Persona:

    def __init__(self, **kwargs):

        self.nombre = kwargs.get("Name", "NoName")
        self.edad = kwargs.get("Age", "NaN")
        self.apellidos = kwargs.get("LastName","NoLastName")

    def __str__(self):

        return "Class Persona: Ingrese Name, LastName ^ Age"

    def get_infoPersona(self):

        print("\t\tPersona:")
        print(f"Nombre: {self.nombre}\tApellido: {self.apellidos}\nEdad: {self.edad}")

class Student(Persona):

    def __init__(self, carrera, **kwargs):

        super().__init__(**kwargs)
        self.carrera = carrera

    def __str__(self):
        return "Class Student: Ingrese Name, LastName, Age ^ carrera"

    def get_infoEstudent(self):

        print('\t\tEstudiante:')
        print(f"Nombre: {self.nombre}\tApellido: {self.apellidos}\nEdad: {self.edad}\tCarrera: {self.carrera}")

class Profesional(Student):

    def __init__(self, experiencia, profesion, carrera, **kwargs):

        super().__init__(carrera, **kwargs)
        self.profesion = profesion
        self.experiencia = experiencia

    def __str__(self):
        return "Class Profesional: Ingrese Name, LastName, Age, carrera ^ profesion"

    def get_infoProfesional(self):

        print('\t\tProfesional:')
        print(f"Nombre: {self.nombre}\tApellido: {self.apellidos}\nEdad: {self.edad}\tCarrera: {self.carrera}\nProfesion: {self.profesion}\nExp: {self.experiencia}")

