import random
#a sample code that guesses based on the most common letters in the category given
#user inputs category, word and number of letters
#remove all words that are not the same length
#find the most common first letter


words = {"Buildings": ["wellman", "california", "young", "kemper"],
         "animals": ["cow", "horse", "squirrel", "sheep"],
         "majors": ["chemistry", "physics", "art", "history"],
         "events": ["picnic day", "earth day" , "orientation"]}

alphabet = set('abcdefghijklmnopqrstuvwxyz')

def get_words(category):
         return words[category]


def eliminate_words(length,category):
         new_words = get_words(category)
         for word in new_words:
                  if len(word) != length:
                           del new_words[word]
         return new_words


def nth_common_letter(length, category, letter_number):
         letter_frequency = {}
         
         eliminate_words(length, category)
         
         for word in new_words:
                  if word[letter_number] in alphabet:
                           letter_frequency[word[letter_number]] = letter_frequency.get(letter) + 1
                  
                  
                  
         
         
              
