print("Kalkulator")
import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def calculate (operator,x,y):
    if operator == "1":
        logging.info("Dodaję", x, "i",y)
        return x + y
    elif operator == "2": 
        logging.info("Odejmuję", x ,"i", y)
        return x - y
    elif operator == "3": 
        logging.info("Mnożę", x,"i",y)
        return x * y 
    elif operator == "4": 
        logging.info("Dzielę", x,"i", y)
        return x / y 
    else: return None

if __name__ == "__main__":
        operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: 1")
        x = float(input("Podaj składnik 1:"))
        y = float(input("Podaj składnik 2:"))
        operator = sys.argv[1:]
        result = calculate(operation, x, y)
        print(result)
if y==0:
    print("Nie można dzielić przez zero")
elif result is None:
    print("Niedozwolona operacja")
        