customers = {}
for i in range(int(input())):
    customers.update({name:amount for name, amount in tuple([input().split()])})
change_q = []
fifties = 0
for name, amount in customers.items():
    if amount == "100":
        change_q.append(name)
    elif amount == "50":
        fifties += 1
    while fifties and change_q:
        change_q.pop(0)
        fifties -= 1
print(" ".join(change_q) if change_q else None)