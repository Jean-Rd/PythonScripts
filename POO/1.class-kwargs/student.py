
class Student:

    def __init__(self, **kwargs):

        self.nombre = kwargs.get("Name", "NoName")
        self.edad = kwargs.get("Age", "NaN")
        self.apellidos = kwargs.get("LastName","NoLastName")
        self.university = kwargs.get("University", "Null")

    def get_info(self):
        return f"Nombre: {self.nombre}\tApellido: {self.apellidos}\nEdad: {self.edad}\tUniversidad: {self.university}"