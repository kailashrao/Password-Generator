def shuffle(pass1, num1):
    import random as rd
    list1 = pass1
    for j in range(0, len(list1), 1):
        str1 = list1[j]
        pos = []
        for i in range(0, num1, 1):
            pos.append(i)
        nummix = rd.sample(pos, num1)
        mix = []
        for i in range(0, num1, 1):
            mix.append(str1[nummix[i]])
        final = "".join(mix)
        with open("passgen.txt", "a") as pass1:
            pass1.write(str(j+1) + ". " + final + "\n")

def main(ml, u1, l1, n1, s1, e1):
    
    with open("passgen.txt", "w") as pass1:
        pass1.write("")
    ml = int(ml)
    u1 = int(u1)
    l1 = int(l1)
    n1 = int(n1)
    s1 = int(s1)
    e1 = int(e1)

    import random as rd
    list1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    list2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    list3 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    list4 = ["&", "$", "%", "#", "@", "!", "?", ":", ";", ".", ",", "\"", "\'", "/", "\\", "<", ">", "(", ")", "[", "]", "{", "}", "|", "*", "=", "+", "-", "_", "^", "`", "~"]
    list5 = list1 + list2 + list3 + list4
    total = l1 + u1 + n1 + s1 + e1
    passlist = []
    for j in range(0, ml, 1):
        password = ""
        for i in range(0, u1, 1):
            password += rd.choice(list1)
        for i in range(0, l1, 1):
            password += rd.choice(list2)
        for i in range(0, n1, 1):
            password += rd.choice(list3)
        for i in range(0, s1, 1):
            password += rd.choice(list4)
        for i in range(0, e1, 1):
            password += rd.choice(list5)
        passlist.append(password)
    shuffle(passlist, total)

main(10, 10, 10, 10, 10, 10)