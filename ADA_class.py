

class Materia:
    def __init__(self, codigo, cupo):
        self.codigo = codigo
        self.cupo = cupo

    def restar_cupo(self):
        if self.cupo > 0:
            self.cupo -= 1
        return self.cupo

class Estudiante:
    def __init__(self, codigo, solicitudes):
        self.codigo = codigo
        self.solicitudes = solicitudes

    def __str__(self):
        return f'{self.codigo} {self.solicitudes}'

    def prioridad_total(self):
        return (len(self.solicitudes)* 3)-1

