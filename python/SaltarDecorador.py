#Hay 2 maneras de hacerlo

import functools

def my_decorator(func):
    @functools.wraps(func)  # Usar functools.wraps para preservar metadatos
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

# Definir el decorador
@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

# Usar la función decorada
say_hello("Alice")

# Usar la función sin el decorador
undecorated_say_hello = say_hello.__wrapped__
undecorated_say_hello("Bob")

###################################################################################

#De esta forma no es necesario usar la libreria functools.wraps
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    
    # Almacena la función original en un atributo personalizado
    wrapper.original_function = func
    return wrapper

# Definir el decorador
@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

# Usar la función decorada
say_hello("Alice")

# Usar la función sin el decorador
undecorated_say_hello = say_hello.original_function
undecorated_say_hello("Bob")

