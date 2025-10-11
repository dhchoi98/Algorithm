class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {}
        count = 0

        # 돌 (S)의 빈도 수 계산
        for char in stones:
            if char not in freqs: # 처음
                freqs[char] = 1
            else: # 존재 하면
                freqs[char] += 1
        # 보석 (J)의 빈도 수 합산
        for char in jewels:
            if char in freqs:
                count += freqs[char]

        return count
        