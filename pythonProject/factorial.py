# Returns the value of the factorial of num if it is defined, otherwise, returns None
def factorial(num):
    if type(num) == int and num >= 0:
        if num > 0: 
            return_value = num
            while num > 1:
                prev_value = return_value
                return_value = return_value * (num - 1)
                print(str(prev_value) + ' * ' + str(num - 1) + ' = ' + str(return_value))
                num = num - 1
        elif num == 0:
            return_value = 1

        return(return_value)