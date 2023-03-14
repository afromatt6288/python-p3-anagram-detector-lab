# your code goes here!

class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, word_list,):
        sorted_words = []
        for words in word_list:
            sorted_words.append(sorted(words))
        print(sorted_words)
        print(sorted(self.word))
        anagram_word = []            
        for n in range(len(sorted_words)):
            if sorted(self.word) == sorted_words[n]:
                anagram_word.append(word_list[n])
                print(f"yes, {anagram_word}")
            else:
                print("no")
        print(anagram_word)        
        return anagram_word


##########################
# Their Answer - much more concise than my own... even without all the prints i did...

# class Anagram:
#     def __init__(self, word):
#         self.word_letters = sorted([letter for letter in word])

#     def match(self, word_list):
#         match_word_list = []

#         for word in word_list:
#             if sorted([letter for letter in word]) == self.word_letters:
#                 match_word_list.append(word)

#         return match_word_list