#!/user/bin/python
#-*- coding:utf-8 -*-

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = '#'
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node[self.end_of_word] = self.end_of_word
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return self.end_of_word in node
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True

import unittest
class SolutionTestCase(unittest.TestCase):
    def testCaseSolution(self):        
        trie = Trie()
        trie.insert("apple")
        trie.insert("app")
        trie.insert("cat")
        self.assertTrue(trie.search("apple"))
        self.assertTrue(not trie.search("dog"))
        self.assertTrue(trie.startsWith("app"))


if __name__ == "__main__" : unittest.main()