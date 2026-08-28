numbers = list(map(int, input().split()))
def fun(numbers):
    for i in range(len(numbers)):
        if numbers[i]==8:
            return i
print(fun(numbers))
