# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = sorted([letter for letter in word])

    def match(self, arr):
        matched_words = []

        for word in arr:
            if sorted([letter for letter in matched_words]) == self.word_letters:
                matched_words.append(word)

        return matched_words
    

sorte = Anagram("way")
print(sorte.match(['yaw', 'enlists', 'google', 'inlets', 'banana']))
