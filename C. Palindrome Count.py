def is_palindrome(num):
    return str(num) == str(num)[::-1]

k = int(input())
count = 0
for i in range(1, k + 1):
    if is_palindrome(i):
        count += 1
print(count)