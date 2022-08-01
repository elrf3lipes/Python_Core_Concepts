is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a male or tall or both")
elif is_male and not is_tall:
    print("You are a short male")
elif not (is_male) and is_tall:
    print ("you are not a male but you're tall")
else:
    print("You are not a male and not tall")

#should print (you are a short male)