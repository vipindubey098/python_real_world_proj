#spellchecker
from spellchecker import SpellChecker


spell = SpellChecker()
word = input("Enter the word: ")
corrected_word = spell.correction(word)
print(corrected_word)