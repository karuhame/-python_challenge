import math

""" #paint area calculator
def paint_cal(height,width, cover):
    num_of_cans= math.ceil(height * width / cover)
    print(f"You'll need {num_of_cans} cans of paint")
test_h = int(input())
test_w = int(input())
paint_cal(test_h,test_w,5) """
""" #prime number checker
def prime_check(x):
    cnt = 0
    for i in range(1,x):
        print(i)
        if(i*i<=x):
            if(x%i==0): 
                cnt +=1
                print(i)
        else:
            break
    if(cnt==1):
        print("This is a prime number")
    else:
        print("This is not a prime number")
n = int(input())
prime_check(n) """
#Caesar Ciper part 1
should_continue = True
while should_continue:
    direction = input ("Type 'encode' to encrypt,type 'decode' to decrypt:\n")
    text = input ("Type your message:\n").lower()
    shift = int(input ("Type the shift number:\n"))
    shift %=26
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    def encrypt(plain_text, shift_amount):
        cipher_text = ""
        for i in plain_text:
            position = alphabet.index(i)
            new_position = position+ shift_amount
            new_letter = alphabet[new_position]
            cipher_text+=new_letter
        print(f"The encode text is {cipher_text}")
    def decode(cipher_text, shift_amount):
        plain_text = ""
        for i in cipher_text:
            position = alphabet.index(i)
            new_position = position- shift_amount
            new_letter = alphabet[new_position]
            plain_text +=new_letter
        print(plain_text)
    def caesar(start_text, shift_amount, cipher_direction):
        end_text =""
        if cipher_direction == "decode":
            shift_amount *= -1
        for char in start_text:
            if char in alphabet:
                position =alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += char
        print(f"Here's the {cipher_direction}d result: {end_text}")
    caesar(text,shift,direction)
    conti=input("Do you want to go again?Type 'yes' or 'no'.").lower()
    if(conti=="no"):
        should_continue=False
        print("Goodbye!!!")
   