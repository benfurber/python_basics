def fizzbuzz(number):
    '''
    A standard/simple fizzbuzz for python. It returns the number provided
    unless a multiple of three (then returns 'fizz'), a multiple of five
    ('buzz') or both ('fizzbuzz').
    '''

    if number % 3 == 0 and number % 5 == 0:
        return 'fizzbuzz'
    if number % 3 == 0:
        return 'fizz'
    if number % 5 == 0:
        return 'buzz'
    return number
