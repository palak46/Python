import random

def random_guess():
        sample=["EVAPORATE","TABULAR","RAINFALL","CELEBRATE"]
        oword=random.choice(sample)
        guessed="_"*len(oword)
        word=list(oword)
        guessed=list(guessed)
        return guessed,oword

def main_process(guessed,oword):
    first=[]
    letter=input("guess a letter:")
    word=list(oword)
    while True:
        if letter.upper() in first:
            letter=''
            print("already guessed")
        elif letter.upper() in word:
            index=word.index(letter.upper())
            guessed[index]=letter.upper()
            word[index]='_'
        else:
            print(' '.join(guessed))
            if letter is not '':
               first.append(letter.upper())
            letter=input("guess a letter:")
        if'_' not in guessed:
            print("you win")
            break
return_guessed,oword = random_guess()
main_process(return_guessed,oword)
print("your word is ",oword)