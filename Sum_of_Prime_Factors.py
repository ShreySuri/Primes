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

def factor(x):
    factor_list = []
    while x > 1:
        div = 2
        while (x/div) % 1 != 0:
            div = div + 1
        factor_list.append(div)
        x = int(x/div)
    return(factor_list)

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
    input_1 = input("Enter an integer. The prime factors of this integer will be added and then printed. ")
    main_check = validate(input_1)

input_1 = int(input_1)
fact_list = factor(input_1)
length = len(fact_list)
total = 0
for i in range (0, length):
    num = fact_list[i]
    if isPrime(num) == True:
        total = total + num
    else:
        toggle = False
print(total)

        
        
