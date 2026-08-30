def is_even(num):
    if num%2==0:
        return True
    else:
        return False

def main():
    t=int(input())
    for i in range(t):
        num=int(input())
        if is_even(num):
            print("Even")
        else:
            print("Odd")
if __name__ == "__main__":
    main()
