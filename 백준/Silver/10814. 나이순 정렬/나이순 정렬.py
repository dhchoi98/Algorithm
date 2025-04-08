A=int(input())
user = []
for _ in range(A):
    age, name = input().split()
    user.append([int(age),name])

    # Timsort의 안정정렬 방식으로 인해 먼저 들어온 순서 보장
for i in sorted(user,key=lambda x : x[0]):
    print(i[0],i[1])
