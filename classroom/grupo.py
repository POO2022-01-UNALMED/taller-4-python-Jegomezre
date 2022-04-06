

from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo ordinado", asignaturas=[], estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, *args):
        if self.listadoAlumnos is None:
            self.listadoAlumnos = []
        
        for alumno in args:
            self.listadoAlumnos.append(alumno)

    def __str__(self):
        texto = "Grupo de estudiantes: "
        if self._grupo == "grupo ordinado":
            texto += "grupo predeterminado"
        else:
            texto += self._grupo
        return texto

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre


