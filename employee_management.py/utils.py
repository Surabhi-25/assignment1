def validate_integer_input(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
