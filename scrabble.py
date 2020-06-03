# Scrabble Calculator

scrabble_time = input('Would you like to play scrabble?\n')
if scrabble_time == 'yes':
    print('type "exit" to stop game running')

    while True:

            word = input('Enter your word ')
             # print('to exit game input "exit"')


            score = {"a": 1, "b": 3, "c": 3, "d": 2,
                     "e": 1, "f": 4, "g": 2, "h": 4,
                     "i": 1, "j": 8, "k": 5, "l": 1,
                     "m": 3, "n": 1, "o": 1, "p": 3,
                     "q": 10, "r": 1, "s": 1, "t": 1,
                     "u": 1, "v": 4, "w": 4, "x": 8,
                     "y": 4, "z": 10}

                      # put a total word inside the function
                      # loop through the input word

            def scrabble_score(word):
                return sum(score[letter] for letter in word)
                                        # ^^^return total
            print(scrabble_score(word))
            if word == 'exit':
                break



