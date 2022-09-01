def c_sum(a, b):
    return a + b


def c_sub(a, b):
    return a - b


def c_mul(a, b):
    return a * b


def c_div(a, b):
    if b == 0:
        print("Нельзя делить на ноль (даже в комплексных числах)")
        return None

    return a / b
