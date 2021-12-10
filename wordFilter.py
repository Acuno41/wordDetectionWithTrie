class Node():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    badWordList = []
    resultText = ["No Bad Word Detected !", "Bad Word Detected !"]

    def __init__(self,badWordCsvFileName):
        print("Trie Init !", end="\n\n")
        
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

    
    def search(self, inputTxt):
        tempTrie = self.wordTrie
        for letter in inputTxt:
            if not(letter in tempTrie.children.keys()):
                tempTrie = self.wordTrie
                continue
            tempTrie = tempTrie.children[letter]
            if tempTrie.isEnd: return tempTrie.isEnd
            
        return tempTrie.isEnd


    def searchInText(self, inputTxt):
        result = self.search(inputTxt)
        print(inputTxt)
        print(self.resultText[result], end="\n\n")  


if __name__ == "__main__":
    
    filterTrie = Trie("badWords.csv")

    inputTxt = "this is the dumbest thought i've ever seen"
    filterTrie.searchInText(inputTxt)

    inputTxt = "this is the most beautiful thing i've ever seen"
    filterTrie.searchInText(inputTxt)

    
    