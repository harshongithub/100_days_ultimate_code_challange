import random
import hangman_words
import hangman_logo

print(hangman_logo.logo)
player_lives=int(6)
word=random.choice(hangman_words.word_list)
blanks=[]
for l in word:
    blanks+="_"

end=False
while not end :
    letter=str(input("Guess a letter : ").lower())
    for l in range(len(word)):
        lt=word[l]
        if lt==letter:
            blanks[l]=letter

    if letter not in word:
        player_lives=int(player_lives-1)
        print(hangman_logo.stages[player_lives]+"\n")
        if player_lives==0:
            end=True
            print(f"{hangman_logo.loose} You Lost the Game.")
        else:
            print(f"{letter} is the wrong guess, You loose a life (-_-)' ")
    if "_" not in blanks:
        end=True
        print("Congratulations!, You completed the spelling (^_^)\n You won the Game.")

    print(f"{''.join(blanks)}\n")

