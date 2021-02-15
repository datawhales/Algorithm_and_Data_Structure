def recursive(data):
    if data < 0:
        print("ended")
    else:
        print(data)
        recursive(data - 1)
        print("returned", data)

recursive(4)

data_stack = []
data_stack.append(1)
data_stack.append(2)

print(data_stack)

data_stack.pop()

print(data_stack)

stack_list = []
def push(data):
    stack_list.append(data)

def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data

for idx in range(10):
    push(idx)

print(stack_list)

pop()

print(stack_list)