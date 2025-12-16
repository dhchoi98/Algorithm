class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1 # target 값 보다 작으므로 총 합 증가
            elif numbers[left] + numbers[right] > target:
                right -= 1 # target 값 보다 크므로 총 합 감소
            else:
                return left + 1, right + 1 # 배열 인덱스가 1부터 시작하므로 인덱스에 각 + 1
        