estudiantes = {
    "elena": "Presente",
    "pepe" : "Ausente",
    "ana" : "Ausente",
    "juan" : "Presente",
}

user = input("Dime el nombre del estudiante que quieras saber su asistencia: ")
print(estudiantes.get(user.lower(), "Ese alumno no existe"))