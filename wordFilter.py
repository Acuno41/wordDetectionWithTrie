
class Trie:

    badWordList = []
    def __init__(self):
        print("Trie Init ! ")
        
        self.readBadWords()

    def readBadWords(self):
        file = open("badWords.csv")
        self.badWordList = file.read().split("\n")
        
        


if __name__ == "__main__":
    
    filter = Trie()
    