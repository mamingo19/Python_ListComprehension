import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(data_dict)

name = input("Enter your names or somethings IDK: ").upper()

result = [data_dict[letter] for letter in name]
print(result)
