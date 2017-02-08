
def words(string):
  """The function is meant to count the number of times that a word occurs in a string"""
  
  word_list = string.split() # creates a list from string
  #converts number strings into integers
  word_list = [int(word) if word.isdigit() else word for word in word_list]
  words_and_their_counts = {} #a dictionary that contains the words and their counts
  already_counted_words = [] #stores words that have already been counted
  
  for word in word_list:
    #this loop is to output the final dictionary that contains words and their counts
    if already_counted_words.count(word) == 0:
      already_counted_words.append(word)
      words_and_their_counts[word] = word_list.count(word)
  
  return words_and_their_counts
  


