from DivideBinary import DivideBinary

def BinaryCalculator(number1, number2):
    try:
        number1, number2 = DivideBinary(number1), DivideBinary(number2)
        for i, n in zip(number1, number2):
            i, n = int(i), int(n)
            i, n = '{0:04d}'.format(i), '{0:04d}'.format(n)
            print(i, n)

    except Exception as er:
        print(f"BinaryCalculator : {er}")
