def t(str):
    return str[0]+str[1]

def main():
    lst = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
    file = open(input("What file do ya want to open? ")).read()
    sentence = file.split()
    for k in range(len(sentence)):
        i = sentence[k]
        if i[0] in ['a', 'e', 'i', 'o', 'u']:
            sentence[k] = i+'ay'
        elif len(i) == 1:
            sentence[k] = i[0] + "yay"
        elif t(i) in lst:
            sentence[k] = i[2:]+i[:2]+'ay'
        elif i.isalpha() == False:
            sentence[k] = i
        else:
            sentence[k] = i[1:]+i[0]+'ay'
    print(' '.join(sentence))
    outfile = open(input("Where do you want to write this?")).write(' '.join(sentence))


if __name__ == "__main__":
    main()