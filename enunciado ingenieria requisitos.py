class Empleado:
    def __init__(self, nombre, edad, sueldo_bruto):
        self.nombre = nombre
        self.edad = edad
        self.sueldo_bruto = sueldo_bruto

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Sueldo Bruto: {self.sueldo_bruto}"

class Directivo(Empleado):
    def __init__(self, nombre, edad, sueldo_bruto, categoria, subordinados=[]):
        super().__init__(nombre, edad, sueldo_bruto)
        self.categoria = categoria
        self.subordinados = subordinados

    def agregar_subordinado(self, subordinado):
        self.subordinados.append(subordinado)

    def __str__(self):
        return f"{super().__str__()}, Categoría: {self.categoria}, Subordinados: {', '.join(sub.nombre for sub in self.subordinados)}"

class Cliente:
    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Teléfono: {self.telefono}"

# Ejemplo de uso:

# Crear empleados
empleado1 = Empleado("Santiago", 30, 30000)
empleado2 = Empleado("Amanda", 25, 25000)
directivo = Directivo("Camilo", 35, 40000, "Gerente", [empleado1, empleado2])

# Crear cliente
cliente = Cliente("Samuel", 40, "555-555-555")

# Mostrar información de empleados y clientes
print("Empleados:")
print(empleado1)
print(empleado2)
print(directivo)

print("\nClientes:")
print(cliente)
