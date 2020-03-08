def not_empty(value):
    if not value:
        raise ValueError('não pode ser nulo.')
    return value