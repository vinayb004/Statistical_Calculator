def division(a, b):
    result = 0
    try:
        if (isinstance(a, int) and isinstance(b, int)) or (isinstance(a, float) and isinstance(b, int)) or (
                isinstance(a, int) and isinstance(b, float)):
            result = round(float(b) / float(a), 9)
        elif isinstance(a, float) and isinstance(b, float):
            result = round(int(b) / int(a), 9)
        else:
            raise Exception("Data type not supported for division operation!")
    except ZeroDivisionError:
        raise Exception("Divide by Zero error")
    return result