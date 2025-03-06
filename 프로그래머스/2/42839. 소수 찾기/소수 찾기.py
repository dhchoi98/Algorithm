from itertools import permutations

def solution(numbers):
    
    # 소수 : 1과 자신 이외는 어떤수로도 나눌수 없는 수
    answer = 0
    """
    아이디어 : numbers 문자열을 list로 변환하여 하나하나의 문자로 나눈다.
    여기서 소수가 될만한 수를 추려 조합한다. -> 어떻게?
    
    1. 숫자 조합을 만들어서 리스트에 저장
    2. 리스트를 순회하며 해당 숫자가 소수인지 확인
    """
    
    
    def generate_numbers(s):
        unique_numbers = set()  # 중복 제거를 위한 집합

        # 숫자의 길이를 1부터 전체 길이까지 증가시키며 조합 생성
        for r in range(1, len(s) + 1):
            # 해당 길이의 모든 순열 생성
            perm_list = permutations(s, r)

            for perm in perm_list:
                # print(perm)
                number = "".join(perm)  # 튜플을 문자열로 변환
                unique_numbers.add(int(number))  # 숫자로 변환하여 집합에 추가

        return sorted(unique_numbers)  # 정렬하여 반환
    
    all_numbers_list = generate_numbers(numbers)
    
    for num in all_numbers_list: # 리스트에 들어있는 원소가 소수인지 확인
        is_prime = True
        
        if num < 2: # 0, 1 은 소수가 아님
            is_prime = False
            
            
        for i in range(2, int(num ** 0.5) + 1): # 자기 자신이나 1이 아닌 다른 수로 나누어지면 소수가 아님
            if num % i == 0:           # 소수의 제곱근까지만 확인하면 판별 가능
                is_prime = False
                
        if is_prime: # 소수가 맞다면 정답체크
            answer += 1
    
    return answer