class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode) # 다음 노드로 연결되는 딕셔너리
        self.word_id = -1 # 각 단어가 끝나는 지점, -1 일경우 아직 단어가 끝나지 않음(중간 노드), 아닐 경우 해당 단어의 입력 시 인덱스
        self.palindrome_word_ids = [] # 

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1] # 슬라이싱(slicing) 을 이용한 역순 문자열 생성을 통해 펠린드롬 판별

    # 단어 삽입
    def insert(self, index, word) -> None:                                        
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):# 단어를 거꾸로 넣으면서, 아직 넣지 않은 앞부분(word[0:len(word)-i])이 회문이면,
                node.palindrome_word_ids.append(index)
            node = node.children[char] 
            node.val = char
        node.word_id = index
    
    def search(self, index, word) -> List[List[int]]:
        result = []
        node = self.root

        while word:
            # 판별 로직
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        # 판별 로직
        if node.word_id >= 0 and node.word_id != index: # word_id가 -1이 아니고, 현재 인덱스와 다르면
            result.append([index, node.word_id])

        # 판별 로직
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])
        
        return result



class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)
        
        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))
        
        return results