def ln(x, order = 100):
    sum = 0
    for i in range(0, order+1):
        sum += ((-1)**(i)*(x-1)**i)/(i+1)
    return sum