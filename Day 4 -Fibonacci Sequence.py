# Fibonacci Sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,...

# let's make it 20 pieces fNumbers

x = 1
y = 1
fibonacci = [x, y]
for f in range(21):
    x, y = y, x + y
    fibonacci.append(y)

print(fibonacci)