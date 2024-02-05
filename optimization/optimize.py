def enumeration(interval: list, function, step_size: float):
    N = int((interval[1]-interval[0])/step_size)
    f_x = []
    x = []
    x_ = interval[0]
    for iter in range(N):
        x_ += step_size
        f_x.append(function(x_))
        x.append(x_)
    idx = f_x.index(min(f_x))
    return f_x[idx], x[idx]


def updated_enumeration(interval: list, function, accuracy: float):
    delta = 0.1
    N = int((interval[1]-interval[0])/delta)
    f_x_min = float("inf")
    x0 = interval[0]
    x_min = 0
    x1 = 0
    while True:
        x0 += delta
        if function(x0) > function(x1):
            delta /= 4
            delta *= -1
            
        if function(x0) < f_x_min:
            f_x_min = function(x0)
            x_min = x0
        
        if abs(delta) < accuracy:
            f_x_min = function(x0)
            x_min = x0
            break
        x1 = x0
    return f_x_min, x_min