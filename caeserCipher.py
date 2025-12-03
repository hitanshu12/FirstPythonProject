# import string
#
# alphabets = list(string.ascii_lowercase)
# print(alphabets)



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to to encrypt and 'decode' to dycript: \n ").lower()
# text = input("Type your message: \n").lower()
# shift = int(input("Type the shift number:\n"))


# Todo 1: create a function called encrypt that takes original text and shift amount as 2 inputs





# create a encrypt function
# def encrypt(original_text, shift_amount):
#
#         # what happen if you try to shift the letter z by 9
#
#
#
#     chiper_text = ""
#         # Todo 2: Inside the encrypt function shift each letter of the original_text to words the alphabet
#         #  of the shift amount and print the encrypted text
#
#     for letter in original_text:
#         shifted_pos = alphabet.index(letter) + shift_amount
#
#         shifted_pos = shifted_pos % len(alphabet)
#
#         chiper_text = chiper_text + alphabet[shifted_pos]
#
#
#
#     print(f"Your final encrypted output should be {chiper_text}")
#
#
#     # Todo 3: call the encrypt function and pass in the user inputs. you should be
#     #  able to test the code and encrypt a massage
#
#     encrypt(original_text=text, shift_amount=shift)



# def dycript(original_text, shift_amount):
#
#     decipher_text = ''
#
#     for letter in original_text:
#
#         shifted_pos = alphabet.index(letter) - shift_amount
#         shifted_pos = shifted_pos % len(alphabet)
#         decipher_text = decipher_text + alphabet[shifted_pos]
#
#     print(f"Your final encrypted output should be {decipher_text}")
#
#
# dycript(original_text=text, shift_amount=shift)




def caesar(original_text, shift_amount, encode_or_decode):

    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_pos = alphabet.index(letter) + shift_amount
            shifted_pos = shifted_pos % len(alphabet)
            output_text = output_text + alphabet[shifted_pos]

    print(f"here id the {encode_or_decode} result: {output_text}")


# rerun the chiper program

should_continue = True

while should_continue:
    direction = input("Type 'encode' to to encrypt and 'decode' to dycript: \n ").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart  = input("Type 'yes' if you want to go again. Otherwise type 'NO': \n ").lower()

    if restart == 'No':
        should_continue = False
        print("Good Bye")
