

while True:
    try:
        sentence =input()
        number_of_time = 0
        for letter in sentence:
            char = ''
            
            if letter >='0' and letter <='9':
                number_of_time += int(letter)
            elif letter == 'b':
                for i in range(number_of_time):
                    print(' ',end='')
                number_of_time = 0
            elif letter == '!':
                number_of_time = 0
                print()
            else:
                for i in range(number_of_time):
                    print(letter,end='')
                number_of_time = 0
        
        print()


    except EOFError:
        break