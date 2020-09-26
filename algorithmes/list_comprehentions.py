A = [1, 2, 3, 4, 5]

B = []
for x in A:
    if x % 2 == 0:
        B.append(x ** 2)
# equal to:
C = [x + 2 for x in A if x % 2 == 0]

print(B)
print(C)
print(B == C)
