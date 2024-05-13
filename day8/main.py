def greet():
    print("Hello, world!")
    print("Goodbye, world!")
    print("Hello again, world!")
    
greet()

def greet_with_name(name):
    print(f"Hello, {name}!")
    print(f"Goodbye, {name}!")
    print(f"Hello again, {name}!")

greet_with_name("Alice")

def greet_with_parameters(name,location):
    print(f"Hello, {name}!")
    print(f"You are from {location}!")
    
greet_with_parameters("Alice","Wonderland")

def greet_with_keyword_parameters(name,location):
    print(f"Hello, {name}!")
    print(f"You are from {location}!")
    
greet_with_keyword_parameters(location="Wonderland",name="Alice")

