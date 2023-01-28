with open("./Input/Names/invited_names.txt") as names_file:
    list_of_names = names_file.readlines()


with open("./Input/Letters/starting_letter.txt") as letter_format:
    lines = letter_format.read()

print(list_of_names)
list_of_names = [x.strip("\n") for x in list_of_names]
print(list_of_names)
print(lines)

for name in list_of_names:
    lines2 = lines.replace("[name]", name)
    print(lines2)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "a" ) as final_letter:
        final_letter.write(lines2)



