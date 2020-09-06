def say_hello(name,emoji):
    print(f'Heloo {name} {emoji}')

#positional arguments
say_hello('Osvaldo', ';-)')

#keywords arguments
say_hello(emoji=';-)', name='Santi')

# better follow the natural order!!!

#Default parametters...
def say_hello1(name='Darth Vader',emoji=';-)'):
    print(f'Heloo {name} {emoji}')

say_hello1()