"""
********************************************************************************
* Project Name:  NATO Phonetic Alphabet
* Description:   The NATO Alphabet Generator is a Python program that converts a word into its corresponding NATO phonetic alphabet code
* Author:        ziqkimi308
* Created:       2024-12-05
* Updated:       2024-12-05
* Version:       1.0
********************************************************************************
"""

import pandas

# Constant
PATH = r"E:\Learning\Python\Python_Projects\NATO Alphabet Project [Improved with Exception Handling]\nato_phonetic_alphabet.csv"

# Read csv using pandas
data = pandas.read_csv(PATH)

# Make dictionary using dict comprehension and iterrows
dict_data = {row.letter:row.code for (index, row) in data.iterrows()}

# User input and transform
def generate_phonetic():
	user_input = input("Enter a word: ").upper()
	try:
		word_list = [dict_data[letter] for letter in user_input]
	except KeyError:
		print("We accept only alphabets!")
		# Recall function to not end the session
		generate_phonetic()
	else:
		print(word_list)

generate_phonetic()