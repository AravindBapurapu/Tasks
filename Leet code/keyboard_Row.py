# Q-500: 
# class solution:
# define rows as sets in lowercase for o(1) membership test - because if we use list or string then 
# python will loop through each word and takes longer time, but set is a special data structure that know where exactly each letter is.

def Keyboard_row(words):                # ["alaska", "dad", "peace"]
    row1 = set("qwertyuiop")
    row2 = set('asdfghjkl')
    row3 = set("zxcvbnm")

    res = []
    for word in words:
        # define lower to make it normalize to avoid case sensitivity
        lower = word.lower()
        # choosing a row by first charecter - 
        if lower[0] in row1:
            row = row1
        elif lower[0] in row2:
            row = row2
        else:
            row = row3
        # check all charecters belongs to the choosen row
        all_in_row = True
        for char in lower:
            if char not in row:
                all_in_row = False
                break
        if all_in_row:
            res.append(word)
    return res
print(Keyboard_row(['Alaska','dad','peace']))