# your code goes here!

class Anagram:
    def __init__(self, word):
        self.letters_in_word = sorted([letter for letter in word])

    def match(self, arr):
        arr_list = []

        for word in arr:
            if sorted([letter for letter in word]) == self.letters_in_word:
                arr_list.append(word)

        return arr_list
    

sorte = Anagram("way")
print(sorte.match(['yaw', 'enlists', 'google', 'inlets', 'banana']))
