PLACE_HOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    name = names.readlines()
    
with open("./Input/Letters/starting_letter.txt") as later:
    massage = later.read()
    
for name_ in name:
    striped_name = name_.strip()
    new_later = massage.replace(PLACE_HOLDER, striped_name)
    
    with open(f"./Output/ReadyToSend/New_Latter_For_{striped_name}", "w") as new:
        new.write(new_later)

    import panda