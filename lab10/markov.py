import numpy as np

def make_pairs(splits):
    for i in range(len(splits)-1):\
        yield (splits[i], splits[i+1])

def main():
    file = open(input("What file do ya want to open? ")).read()
    splits = file.split()
    pairs = make_pairs(splits)
    word_dict = {}
    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]
    first_word = np.random.choice(splits)

    while first_word.islower():
        first_word = np.random.choice(splits)

    chain = [first_word]

    n_words = 100

    for i in range(n_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))

    print(' '.join(chain))
if __name__ == "__main__":
    main()