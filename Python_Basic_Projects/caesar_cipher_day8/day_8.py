import logo
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo.logo)
def caesar(message,shift,cryto):
    end_text=''
    if crypto=="decode":
            shift*=-1
    for letter in message:
        if letter in alpha:
            position=alpha.index(letter)
            new_pos=position+shift
            end_text+=alpha[new_pos]
        else:
            end_text+=letter
    print(f"The {crypto}d text is {end_text}")
continue_loop=True
while continue_loop:
    crypto=input("Type 'encode' to encrypt, type 'decode' to decrypt :\n").lower()
    message=input("Type your massage :\n").lower()
    shift=int(input("Type the shift number :\n"))
    shift = shift%26


    caesar(message,shift,crypto)
    inp=input("Type Yes to continuem, No to exit: \n").lowerr()
    if inp=="no":
        continue_loop=False
        print("GoodBye")