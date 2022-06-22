# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt", "r") as f:
    names = f.readlines()
    f.close()
    for name in names:
        stripped = name.rstrip()
        with open("Input/Letters/starting_letter.txt", "r") as le:
            content = le.read()
            le.close()
        merged = content.replace("[name]", stripped)
        with open(f"Output/ReadyToSend/{stripped}.txt", "w") as r:
            r.write(merged)
            r.close()

