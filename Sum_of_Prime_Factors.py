def factor(x):
    factor_list = []
    while x > 1:
        div = 2
        while (x/div) % 1 != 0:
            div = div + 1
        factor_list.append(div)
        x = int(x/div)
    return(factor_list)
        
        
