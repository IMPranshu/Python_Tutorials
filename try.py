def div42by(divideBy):
    try:
        return 42/divideBy

    except ZeroDivisionError:
        print('Error:You are dividing by Zero!!!!')
        return ''
    

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))
