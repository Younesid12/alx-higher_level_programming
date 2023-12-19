def safe_print_division(a, b):
    result_value = None
    try:
        if b != 0:
            result_value = a / b
    except ZeroDivisionError:
        result_value = None
    finally:
        print("Inside result: {}".format(result_value))
        return result_value
