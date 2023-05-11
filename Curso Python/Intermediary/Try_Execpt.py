
try:
    a = 10
    c = a / b
except ZeroDivisionError:
    print("Division by zero")

except ValueError:
    print("Value error")

except NameError:
    print("Name error")

except TypeError:
    print("Type error")

except IndexError:
    print("Index error")

except Exception:
    print('Error Desconhecido.')

#Try, except, else e finally