#5
def text():
    try:
        n=input('string')
        print(len(n))
    except ValueError as exceptie:
        print(exceptie)
        print('textul este string')