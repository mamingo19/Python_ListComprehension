import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(data_dict)

def generate():
    name = input("Enter your names or somethings IDK: ").upper()
    try:
        result = [data_dict[letter] for letter in name]
    except KeyError:
        print("Please only LETTERS")
        generate()
    else:
        print(result)

generate()

#I did not know the code a function can run it own function in python skull*