class Cliente:
    def __init__(self, dni, nombre, direccion, telefono, codigo):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.codigo = codigo
        self.aval = None  # Cliente avalador

class Coche:
    def __init__(self, matricula, modelo, color, marca, garaje):
        self.matricula = matricula
        self.modelo = modelo
        self.color = color
        self.marca = marca
        self.garaje = garaje

class Reserva:
    def __init__(self, cliente, coches, agencia, fecha_inicio, fecha_final, precio_alquiler, litros_gasolina, precio_total, entregado):
        self.cliente = cliente
        self.coches = coches
        self.agencia = agencia
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.precio_alquiler = precio_alquiler
        self.litros_gasolina = litros_gasolina
        self.precio_total = precio_total
        self.entregado = entregado

class Agencia:
    def __init__(self, nombre):
        self.nombre = nombre

# Ejemplo de uso:

# Crear clientes
cliente1 = Cliente("12345678A", "Carlos Rosero", "Calle 123", "555-555-555", "C001")
cliente2 = Cliente("87654321B", "María López", "Avenida XYZ", "555-555-556", "C002")

# Establecer aval
cliente1.aval = cliente2

# Crear coches
coche1 = Coche("ABC123", "Toyota", "Rojo", "Corolla", "Garaje1")
coche2 = Coche("DEF456", "Ford", "Azul", "Focus", "Garaje2")

# Crear agencia
agencia = Agencia("Agencia Principal")

# Crear reserva
reserva = Reserva(cliente1, [coche1, coche2], agencia, "2023-09-21", "2023-09-28", 200, 40, 400, False)

# Mostrar información
print("Información del Cliente:")
print(f"DNI: {cliente1.dni}, Nombre: {cliente1.nombre}, Dirección: {cliente1.direccion}, Teléfono: {cliente1.telefono}, Código: {cliente1.codigo}")
if cliente1.aval:
    print(f"Avalado por: {cliente1.aval.nombre}")

print("\nInformación del Coche:")
print(f"Matrícula: {coche1.matricula}, Modelo: {coche1.modelo}, Color: {coche1.color}, Marca: {coche1.marca}, Garaje: {coche1.garaje}")

print("\nInformación de la Reserva:")
print(f"Cliente: {reserva.cliente.nombre}")
print(f"Coches: {[coche.matricula for coche in reserva.coches]}")
print(f"Agencia: {reserva.agencia.nombre}")
print(f"Fecha de Inicio: {reserva.fecha_inicio}, Fecha Final: {reserva.fecha_final}")
print(f"Precio de Alquiler: {reserva.precio_alquiler}, Litros de Gasolina: {reserva.litros_gasolina}")
print(f"Precio Total: {reserva.precio_total}, Entregado: {reserva.entregado}")
