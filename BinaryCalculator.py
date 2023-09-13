from DivideBinary import DivideBinary

def BinaryCalculator(number1, number2):
    try:
        number1, number2 = DivideBinary(number1), DivideBinary(number2)
        return number1, number2
    except Exception as er:
        print(f"BinaryCalculator : {er}")
