def isAlphabeticPalindrome(code):
    # Write your code here
    pass
if __name__ == '__main__':
    digits = [str(x) for x in range(10)]
    arr = list(input())
    arr = [x for x in arr if x not in digits]
    for item in arr:
        print(item)