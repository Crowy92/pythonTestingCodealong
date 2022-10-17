import requests

class StuffError(Exception):
    pass

cats = []

def find_cat_by_id(cat_id):
    return next(cat for cat in cats if cat['id'] == cat_id)

def greeting(name):
    print(f'Hello, {name}!')

def sheep_translator(phrase):
    result = f"M{' m'.join([''.join(['a' for char in word]) for word in phrase.split(' ')])}"
    return result

def how_many_sweets(sweets, people):
    if not people:
        raise StuffError('We need some people to share sweets with!')
    return len(sweets) / len(people)

def do_maths(x, y):
    try:
        return x + y
    except:
        raise StuffError(f'We can\'t add {x} and {y}...')

def add_fruit(fruit, salad):
    salad.append(fruit)
    return salad

def fetch_stuff():
    req = requests.get('https://api.github.com/users/getfutureproof')
    data = req.json()
    print(f"Email is {data['email']}")