print('How many cats do you have?')
numCats = input()
try:
    if int(numCats)>=4:
        print('Thats a lot of cats!')
    elif int(numCats)<0:
        print('How can you have negative no. of Cats????')


    else:
        print('Not that many cats!')
    
except ValueError:
    print('You did not enter a Number')
