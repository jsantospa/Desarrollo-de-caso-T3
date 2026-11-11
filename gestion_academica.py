estudiantes = {}
matriculas = {}


def registrar_estudiante(codigo, nombre):
    if not codigo or not nombre:
        raise ValueError("Codigo y nombre son obligatorios")
    if codigo in estudiantes:
        raise ValueError("El estudiante ya esta registrado")
    estudiantes[codigo] = nombre
    return True


def matricular(codigo, curso):
    if codigo not in estudiantes:
        raise KeyError("Estudiante no registrado")
    matriculas.setdefault(codigo, []).append(curso)
    return matriculas[codigo]


def calcular_promedio(notas):
    if not notas:
        raise ValueError("Debe ingresar al menos una nota")
    for n in notas:
        if n < 0 or n > 20:
            raise ValueError("Las notas deben estar entre 0 y 20")
    return round(sum(notas) / len(notas), 2)


def obtener_estado(promedio):
    return "Aprobado" if promedio >= 13 else "Desaprobado"


if __name__ == "__main__":
    print("Sistema de Gestion Academica - Innovatec Education")
    registrar_estudiante("N00384186", "Joseph Santos")
    matricular("N00384186", "Calidad y Pruebas de Software")
    promedio = calcular_promedio([14, 16, 12])
    print("Promedio:", promedio)
    print("Estado:", obtener_estado(promedio))