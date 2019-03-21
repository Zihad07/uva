

# test = 1
while True:

    try:
        sentence = input()

        myFlag = 0
        word = 0
        for letter in sentence:

            if(letter>='a' and letter<= 'z') or (letter>='A' and letter<= 'Z'):
                myFlag = 1
            else:
                word += myFlag
                myFlag = 0
        if len(sentence) == 0:
            break
        print(word+myFlag)
    except EOFError:
        break
    
    
