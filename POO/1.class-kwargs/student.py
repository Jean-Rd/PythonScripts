
class Persona:

    def __init__(self, **kwargs):

        self.nombre = kwargs.get("Name", "NoName")
        self.edad = kwargs.get("Age", "NaN")
        self.apellidos = kwargs.get("LastName","NoLastName")

    def __str__(self):

        return "Class Persona: Ingrese Name, LastName ^ Age"

    def get_infoPersona(self):
        return f"Nombre: {self.nombre}\tApellido: {self.apellidos}\nEdad: {self.edad}"

    def exp_lab(self, experiencia):

        return f"Experiencia laboral: {experiencia}"

class Student(Persona):

    def __str__(self):
        return "Class Student: Ingrese Name, LastName, Age ^ carrera"

    def get_infoEstudent(self, carrera):

        return f"Nombre: {self.nombre}\tApellido: {self.apellidos}\nEdad: {self.edad}\tCarrera: {carrera}"

class Profesional(Persona):

    def __str__(self):
        return "Class Profesional: Ingrese Name, LastName, Age, carrera ^ profesion"

    def get_infoProfesional(self, carrera, profesion, experiencia):

        return f"Nombre: {self.nombre}\tApellido: {self.apellidos}\nEdad: {self.edad}\tCarrera: {carrera}\nProfesion: {profesion}\n{Persona.exp_lab(self, experiencia)}"

