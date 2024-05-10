import random as rd

def shuffle(passwords, numchar):
    for j in range(0, len(passwords), 1):
        pass1 = passwords[j]
        pos = []
        for i in range(0, numchar, 1):
            pos.append(i)
        nummix = rd.sample(pos, numchar)
        mix = []
        for i in range(0, numchar, 1):
            mix.append(pass1[nummix[i]])
        final = "".join(mix)
        with open("passgen.txt", "a") as f1:
            f1.write(str(j+1) + ". " + final + "\n")

def generatePasswords(inputs):
    with open("passgen.txt", "w") as f1:
        f1.write("")

    upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    number = [str(num) for num in range(10)]
    special = ["&", "$", "%", "#", "@", "!", "?", ":", ";", ".", ",", "\"", "\'", "/", "\\", "<", ">", "(", ")", "[", "]", "{", "}", "|", "*", "=", "+", "-", "_", "^", "`", "~"]
    extra = upper + lower + number + special
    total = sum(inputs) - inputs[0]
    passlist = []
    for j in range(0, inputs[0], 1):
        password = ""
        for i in range(0, inputs[1], 1):
            password += rd.choice(upper)
        for i in range(0, inputs[2], 1):
            password += rd.choice(lower)
        for i in range(0, inputs[3], 1):
            password += rd.choice(number)
        for i in range(0, inputs[4], 1):
            password += rd.choice(special)
        for i in range(0, inputs[5], 1):
            password += rd.choice(extra)
        passlist.append(password)
    shuffle(passlist, total)