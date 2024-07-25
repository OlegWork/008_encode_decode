
continue_cyphering = True


while continue_cyphering is True:
    user_action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    user_message = input("Type your message:\n")
    shift_number = int(input("Type the shift number:\n"))

    encoded_result = "xxxxx"
    print(f"Here's the encoded result: {encoded_result}")

    continue_working = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if continue_working == "no":
        continue_cyphering = False


else:
    print("Goodbye")