def solution(number, k):
    stack = []
    for n in number:
        #print("n : ", n)
        while len(stack)>0 and k>0 and stack[-1]<n:
            pop = stack.pop()
            #print("Pop : ", pop)
            k -= 1
        stack.append(n)
        #print("stack:", stack)
    if k:
        return number[:-k]
    else:
        return "".join(stack)