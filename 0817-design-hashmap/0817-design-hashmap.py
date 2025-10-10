import collections

class MyHashMap:
    class ListNode:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(lambda: MyHashMap.ListNode())

    # 삽입
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        head = self.table[index]
        if head.key is None:                 # 빈 버킷
            head.key = key
            head.value = value
            return

        p = head
        while p:
            if p.key == key:                 # 업데이트
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = MyHashMap.ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        p = self.table[index]
        if p.key is None:
            return -1
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        p = self.table[index]
        if p.key is None:
            return

        if p.key == key:                     # 버킷 헤드 삭제
            self.table[index] = (MyHashMap.ListNode() if p.next is None else p.next)
            return

        prev = p
        p = p.next
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
