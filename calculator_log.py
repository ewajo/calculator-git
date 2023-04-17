print("Kalkulator")
import sys
import logging
logging.basicConfig(level=logging.DEBUG)

     
def add(x,y):
    logging.info(f"Dodaję {x} i {y}")
    return x + y

def subtract(x,y):
    logging.info(f"Odejmuję {x} i {y}")
    return x - y

def multiply(x,y):
    logging.info(f"Mnożę {x} i {y}")
    return x * y 

def divide(x,y):
    logging.info(f"Dzielę {x} i {y}")
    return x / y 

def calculate (operator,x,y):
    if operator == "1":
        result=add(x,y)
    elif operator == "2":
        result=subtract(x,y)
    elif operator == "3":
        result=multiply(x,y)
    elif operator == "4":
        result=divide(x,y)
    return result

if __name__ == "__main__":
    operator = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie ")
    x = float(input("Podaj składnik 1:"))
    y = float(input("Podaj składnik 2:"))
    result = calculate(operator, x,y)
    print(result)
    if y==0:
        print("Nie można dzielić przez zero")
    elif result is None:
        print("Niedozwolona operacja")
        