class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['#'] = True  # End of word marker

    def search(self, word):
        def dfs(i, node):
            if i == len(word):
                return '#' in node
            
            ch = word[i]
            
            if ch == '.':
                for child in node:
                    if child != '#' and dfs(i + 1, node[child]):
                        return True
                return False
            else:
                if ch not in node:
                    return False
                return dfs(i + 1, node[ch])
        
        return dfs(0, self.root)