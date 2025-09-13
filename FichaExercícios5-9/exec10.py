num1 = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))


for i in range(num1, num2, 2):
    if i % 2 == 0:
        print(i)
    else:
        print(i + 1)