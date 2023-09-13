from NumToBinary import NumToBinary

def BinaryCalculator(number1, number2):
    try:
        binary1, binary2 = NumToBinary(number1), NumToBinary(number2)
        binary1 = [[binary1[i:i+4]] for i in range(0, len(binary1), 4)]
        binary2 = [[binary2[i:i+4]] for i in range(0, len(binary2), 4)]
        return binary1, binary2

    except Exception as er:
        print(f"BinaryCalculator : {er}")
