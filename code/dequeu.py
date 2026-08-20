from collections import deque

ls = deque([6, 7, 6, 7])
ls.append(6)
ls.append(7)
print(ls)

ls.popleft()
print(ls)
# ls.pop(0) 이러면 멍 청 그자체; 인수 없이만 쓸 수 있다.
print(ls)

ls.appendleft(6)
print(ls)
