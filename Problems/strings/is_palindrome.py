def is_palindrome(s):
    return s == s[::-1]


# Driver code
s = "malayalam"
ans = is_palindrome(s)

if ans:
    print("Yes")
else:
    print("No")

print("Not mutable example:")
test_str = "Katya"
print(test_str[2])
# test_str[2] = "N"
# print(test_str[2])
test_str.replace(test_str, "N")
print(test_str[2])

