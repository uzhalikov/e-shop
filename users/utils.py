from random import randint

def generate_password():
    return f'{randint(100, 999)}_random_{randint(5556, 9999)}'