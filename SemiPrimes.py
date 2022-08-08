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
    input_1 = input("Enter an integer. All semi-primes less than this integer will be printed. ")
    main_check = validate(input_1)

input_1 = int(input_1)
for i in range (0, input_1):
    fact_list = factor(i)
    length = len(fact_list)
    if length == 2:
        print(i)
    else:
        toggle = True
