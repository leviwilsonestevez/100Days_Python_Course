guests = open("Input/Names/invited_names.txt").read().splitlines()
for guest in guests:
    with open("Input/Letters/starting_letter.txt", mode="r") as letter:
        text = letter.read()
        output_letter = text.replace("[name]", guest)
        specific_letter = open(f"Output/ReadyToSend/{guest}.txt", mode="w")
        specific_letter.write(output_letter)
        specific_letter.close()
    letter.close()
