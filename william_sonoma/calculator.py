def basic_calculator(expression):
    try:
        calc = eval(expression)
    except:
        return 'Error'
    return calc


