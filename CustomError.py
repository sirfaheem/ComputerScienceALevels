try:
    price = float(input('Enter price: '))
    if price<0:
        raise NegativeError('price cannot be negative')
    else:
        pass
except NegativeError:
    print('price cannot be a negative value')
