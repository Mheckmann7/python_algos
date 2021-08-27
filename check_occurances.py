def is_isogram(string):
    letters = {} 
    # creates a dictionary 
    for i in string.lower(): 
        if i in letters:
            letters[i] += 1
        else: 
            letters[i] = 1
            
    for key in letters: 
        if letters[key] > 1:
            return False
    return True

print(is_isogram("Dermatoglyphics")) # True

