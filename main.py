def suma(x, y):
    print( x + y)


def resta(x, y):
    return x - y


def multiplicacion(x, y):
    return x * y


def division(x, y):
    if y == 0:
        print("Error. Division por cero." )
    else:
        print(x / y)

print ("Bienvenido a tu calculadora Matematica!! ")
print("Escoge una operacion aritmetica: ")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")

while True:
    choice = input("Escoje una opcion (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Coloca el primer numero: "))
        num2 = float(input("Coloca el segundo numero: "))

        if choice == '1':
            print("Resultado:", suma(num1, num2))
        elif choice == '2':
            print("Result:", resta(num1, num2))
        elif choice == '3':
            print("Result:", multiplicacion(num1, num2))
        elif choice == '4':
            print("Result:", division(num1, num2))
        break
    else:
        print("Invalid Input")