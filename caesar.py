def alphabet_position(letter):
    """ finds the position of a 'letter' in the string 'alpha' """
    letter = letter.lower()
    alpha = ("abcdefghijklmnopqrstuvwxyz")
    return alpha.find(letter)

def rotate_character(char, rot):
    """ rotates 'char' to a 'new_char' based on it's 'idx' via 'alphabet_position' plus 'rot' divided by (modulo) 26 """
    alpha = ("abcdefghijklmnopqrstuvwxyz")
    new_char = ""
    idx = 0
    if alphabet_position(char) == -1:
        return char
    else:
        idx = (alphabet_position(char) + rot) % 26
        new_char = alpha[idx]
        if char == char.lower():
            return new_char.lower()
        else:
            return new_char.upper()
            
def encrypt(text, rot):
    """ receives 'text' and iterates through each 'char' to 'rotate_character' and update 'new_text' """
    new_text = ""
    for char in text:
        new_text += rotate_character(char, rot)
    return new_text
