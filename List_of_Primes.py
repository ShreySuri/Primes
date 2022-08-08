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

def validate(x):
    list_x = list(x)
    length = len(list_x)
    counter = 0
    for i in range (0, length):
        for j in range (0, 10):
            j = str(j)
            if list_x[i] == j:
                counter = counter + 1
            else:
                toggle = True
    if counter == length:
        return(True)
    else:
        return(False)

main_check = False
while main_check == False:
    input_1 = input("Enter an integer. All primes less than this integer will be shown. ")
    main_check = validate(input_1)

input_1 = int(input_1)
for i in range (0, input_1):
    if isPrime(i) == True:
        print(i)
    else:
        toggle = True
