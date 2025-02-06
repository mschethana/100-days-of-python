alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
go_again='y'
def ceasar(text,shift):

    if direction=="encode":
        encrypt_message=''
        for i in text:
            if i not in alphabet:
                encrypt_message+=i
            else:
                old_index=alphabet.index(i)
                if (old_index+shift)>len(alphabet):
                    index=old_index+shift-len(alphabet)
                else:
                    index=old_index+shift
                encrypt_message+=alphabet[index]
        print(f"Here is the encoded result: {encrypt_message}")

    elif direction=='decode':
        decrypt_message=''
        for i in text:
            if i not in alphabet:
                decrypt_message+=i
            else:
                old_index=alphabet.index(i)
                if (old_index-shift)<0:
                    index=len(alphabet)+(old_index-shift)
                else:
                    index=old_index-shift
                decrypt_message+=alphabet[index]
        print(f"Here is the decoded result: {decrypt_message}")
while go_again=='y':
    direction=input("Type 'encode' to encrypt and 'decode' to decrypt\n").lower()
    text=input("Type your message: \n").lower()
    shift=int(input("Type the shift number: \n"))
    ceasar(text,shift)
    go_again=input("do you want to go again: y or n? ").lower()

-------------------------------------------
#instructor's version

def caesar(text,shift,encode_or_decode):
    output_text=''
    if encode_or_decode=='decode':
        shift*=-1
    for letter in text:
        if letter not in alphabet:
            output_text+=letter
        else:
            shifted_position=alphabet.index(letter)+shift
            shifted_position%=len(alphabet)
            output_text+=alphabet[shifted_position]
        print(f"Here is the {encode_or_decode}d result: {decrypt_message}")
should_continue=True
while should_continue:
    direction=input("Type 'encode' to encrypt and 'decode' to decrypt\n").lower()
    text=input("Type your message: \n").lower()
    shift=int(input("Type the shift number: \n"))
    ceasar(text,shift,direction)
    restart=input("Type 'yes' if you want to continue, otherwise type 'no'").lower()
    if restart=='no':
        should_continue=False
        print("Goodbye")

