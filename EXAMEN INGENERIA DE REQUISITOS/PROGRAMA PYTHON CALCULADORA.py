#PROGRAMA CALCULADORA
#realizado por Yuly Bastidas 

#definimos la clase 
class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        return self.num1 + self.num2

    def restar(self):
        return self.num1 - self.num2

    def multiplicar(self):
        return self.num1 * self.num2

    def dividir(self):
        return self.num1 / self.num2

#pedimo al usuario que ingrese los numeros a operar 
def main():
    num1 = int(input("Ingrese el primer número a operar : "))
    num2 = int(input("Ingrese el segundo número a operar: "))

    calculadora = Calculadora(num1, num2)
    # se indicara en la pantalla el resultado de los numeros ingresados 
    #imprimir resultados

    print("Suma:", calculadora.sumar())
    print("Resta:", calculadora.restar())
    print("Multiplicación:", calculadora.multiplicar())
    print("División:", calculadora.dividir())


if __name__ == "__main__":
    main()
