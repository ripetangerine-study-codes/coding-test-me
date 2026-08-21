stack = []
stack.append(6)  # 마지막에만 넣습니다
stack.append(7)
print(stack)
stack.append(6)
print(stack)

stack.pop()  # 스택은 대가리먼저 뽑습니다
print(stack)

top = stack[-1]  # 대가리 터트리지 않고 얌전히 가져오기만 합니다
print(top)
