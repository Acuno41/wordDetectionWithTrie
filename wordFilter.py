class Node():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    badWordList = []
    
    def __init__(self,badWordCsvFileName):
        print("Trie Init ! ")
        
        self.rootNode = Node()
        self.badWordList = self.readBadWords(badWordCsvFileName)
        

    def readBadWords(self, csvFileName):
        file = open(csvFileName)
        return file.read().split("\n")
     
        
    


if __name__ == "__main__":
    
    filterTrie = Trie("badWords.csv")
    