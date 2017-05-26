from BigInteger.biginteger import BigInteger
Tests = 0
Passed = 0
for x in range(-50,50):
    for y in range(-50, 50):
        Tests+=7
        if (BigInteger(x) + BigInteger(y) == x+y):
            Passed += 1
        if (BigInteger(x) - BigInteger(y) == x-y):
            Passed += 1
        if (BigInteger(x) * BigInteger(y) == x*y):
            Passed += 1
        if (BigInteger(x) ** BigInteger(y) == x**y):
            Passed += 1
        if (BigInteger(x) // BigInteger(y) == x//y):
            Passed += 1
        if (BigInteger(x) << BigInteger(y) == x<<y):
            Passed += 1
        if (BigInteger(x) >> BigInteger(y) == x >>y):
            Passed += 1
print("Tests: ",Tests, "Passed: ", Passed)