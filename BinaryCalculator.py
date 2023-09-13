from NumToBinary import NumToBinary

def BinaryCalculator(number1, number2):
    try:
        binary1, binary2 = NumToBinary(number1), NumToBinary(number2)    
        return binary1, binary2

    except Exception as er:
        print(f"BinaryCalculator : {er}")