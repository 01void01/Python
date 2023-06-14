def add(a, b):
    result = a + b
    print(result)

#this is for subtraction
def sub(a, b):
    result = a - b
    print(result)

#multiply
def mul(a, b):
    result = a * b
    print(result)

#divide
def div(a, b):
    result = a / b
    print(result)


if __name__ == '__main__':

    a = input("enter your no.")
    b = input("enter your no.")

    op = input("Enter the operator: ")

    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        print(a/b)
    else:
        print("invalid input")