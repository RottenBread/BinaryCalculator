from NumToBinary import NumToBinary
from ReverseBinary import ReverseBinary

def DivideBinary(number):
    binary_list = []
    binary = NumToBinary(number)
    for i in range(0, len(binary), 4):
        binary_list.append(ReverseBinary(binary[i:i+4]))

    binary_list = binary_list[::-1]
    return binary_list
