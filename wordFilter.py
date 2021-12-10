class Node():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    badWordList = []
    
    def __init__(self,badWordCsvFileName):
        print("Trie Init ! ")
        
        self.wordTrie = Node()
        self.badWordList = self.readBadWords(badWordCsvFileName)
        self.insert(self.wordTrie, self.badWordList)
        

    def readBadWords(self, csvFileName):
        file = open(csvFileName)
        return file.read().split("\n")

    def getNode(self):
        return Node()

    def insert(self,rootNode,  badWords):
        
        for word in badWords:
            tempNode = rootNode
            for letter in word:
                
                if not(letter in tempNode.children.keys()):
                    tempNode.children[letter] = self.getNode()
                
                tempNode = tempNode.children[letter]
            tempNode.isEnd = True
                
            
        
            
     
        
    


if __name__ == "__main__":
    
    filterTrie = Trie("badWords.csv")
    