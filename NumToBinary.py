import BinaryCalculator

def NumToBinary(number):
    try:
        binary = ""
        while number/2 > 0:
            bit_binary = number%2
            binary = binary + str(bit_binary)
            number = number//2
        return binary
    except Exception as er:
        print(f"NumToBinary : {er}")