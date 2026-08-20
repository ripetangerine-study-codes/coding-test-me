# 리포에게 라포형성 레츠고
class stack:
    def __init__(self):  # stack 객체 생성
        self.items = []

    def push(self, data):  # stack 데이터 추가 append
        self.items.append(data)

    def pop(self):
        pop_object = None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            pop_object = self.items.pop()

        return pop_object  # stack의 가장 마지막 데이터를 삭제하고 return pop()

    def peek(self):
        top_object = self.items.pop()
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.top[-1]

        return top_object  # stack의 가장 마지맏 데이터 return

    def isEmpty(self):
        is_empty = False
        if len(self.items) == 0:
            is_empty = True
        return is_empty  # stack이 비었는지 확인하고 boolean 값으로 반환
