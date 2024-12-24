a = int(input("a >>> "))
b = int(input("b >>> "))
amal = input("amal >>> ")  

def amaldayech(a, b, amal):
    if amal == "+":
        print("Qo'shish:", a + b)
    elif amal == "-":
        print("Ayirish:", a - b)
    elif amal == "*":
        print("Ko'paytirish:", a * b)
    elif amal == "/":
         print("Bolish:", a / b)
amaldayech(a, b, amal)