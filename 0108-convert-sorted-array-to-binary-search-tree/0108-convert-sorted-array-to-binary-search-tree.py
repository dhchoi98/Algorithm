# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(lo: int, hi: int) -> Optional[TreeNode]:
            # 종료 조건: 구간이 비면 None 반환
            if lo > hi:
                return None

            mid = (lo + hi) // 2
            node = TreeNode(nums[mid])  # 현재 구간의 중앙값으로 노드 생성

            # 분할 정복 (좌/우 서브트리 구성)
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)

            return node
        
        # 전체 구간(0 ~ len(nums)-1)으로 시작
        return build(0, len(nums) - 1)
