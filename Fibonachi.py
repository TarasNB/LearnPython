num = int(input("Please enter a number "))

prevPrev = 0
print(prevPrev)
prev = 1
print(prev)

for iter in range(2, num) :
    fib = prevPrev + prev
    print(fib)

    prevPrev = prev
    prev = fib
