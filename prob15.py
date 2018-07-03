operations_count = 0
stacks = None

def main():
    global stacks, operations_count
    stacks_count = int(input())
    stacks = []
    for _ in range(stacks_count):
        stacks.append([int(val) for val in input().split()[1:]])
    sorted_stacks = sorted([plate for stack in stacks for plate in stack])
    _min = min(sorted_stacks)
    stack_no = find_stack(_min)
    for val in sorted_stacks:
        if val not in stacks[stack_no]:
            find_and_merge(val, stack_no)
            stack_no = find_stack(val)
    print(operations_count)

def find_and_merge(val, stack_no):
    global operations_count
    target_stack_no = find_stack(val)
    while not join_stacks(stack_no, target_stack_no):
        stacks.append(split_stack(stack_no))
        stack_no = -1

def split_stack(stack_no):
    global operations_count
    operations_count += 1
    stack = stacks[stack_no]
    x, y = stack[0], stack[1]
    if y != x + 1:
        return [stack.pop(0)]
    i = 1
    while y == x + 1 and i < len(stack):
        x = stack[i]
        y = stack[i+1]
        i += 1
    return [stack.pop(0) for _ in range(i)]

def join_stacks(stack_a, stack_b):
    global operations_count
    if stacks[stack_b][0] > stacks[stack_a][-1]:
        operations_count += 1
        stacks[stack_a] += stacks[stack_b]
        stacks.pop(stack_b)
        return 1

def find_stack(val):
    return [i for i, stack in enumerate(stacks) if val in stack][0]

if __name__ == "__main__":
    main()