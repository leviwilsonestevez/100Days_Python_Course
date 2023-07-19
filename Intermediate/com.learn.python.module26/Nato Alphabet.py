import pandas

word = input(f"Enter a word :")
word_list = list(word)
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_rules = {row.letter.lower(): row.code for (index, row) in data.iterrows()}
result = [phonetic_rules[letter] for letter in word_list]
print(result)
