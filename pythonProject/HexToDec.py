hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    valid = True
    for j in range(0, len(hexNum)):
        if hexNum[j] not in hexNumbers:
            valid = False
            break
    
    if valid == True: 
        return_value = 0
        for i in range(0, len(hexNum)):
            return_value = return_value + 16**(len(hexNum)-1-i) * hexNumbers[hexNum[i]]
        return return_value
