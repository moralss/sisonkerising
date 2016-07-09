def test_recursion(n):
    print(n)
    total = 0
    if n > 0:
        return n + test_recursion(n-1)
    else:
        return 0

result = test_recursion(12)

print("blah")
print(result)

