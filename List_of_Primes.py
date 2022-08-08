import math

def max_divisor(x):
    a = math.sqrt(x)
    b = round(a + 1)
    return(b)

def isPrime(x):
    max_div = max_divisor(x)
    check = True
    for i in range (2, max_div):
        if (x/i) % 1 == 0 and x != i:
            check = False
        else:
            toggle = False
    if x < 2:
        return(False)
    else:
        return(check)

main_check = False
while main_check == False:
    input_1 = input("Enter an integer. All primes less than this integer will be shown.")
    input_list = list(input_1)
    length = len(input_list)
    counter = 0
    for i in range (0, length):
        for j in range (0, 10):
            j = str(j)
            if input_list[i] == j:
                counter = counter + 1
            else:
                toggle = True

    if counter == length:
        main_check = True
    else:
        toggle = False

input_1 = int(input_1)
for i in range (0, input_1):
    if isPrime(i) == True:
        print(i)
    else:
        toggle = True
