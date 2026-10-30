def binary(n):
    return format(n & 255, '08b')


def signed_value(n):
    if n >= 128:
        return n - 256
    return n


def addition(a, b):
    print("\nFirst Number:", a)
    print("Second Number:", b)

    print("Binary of First Number:", binary(a))
    print("Binary of Second Number:", binary(b))

    result = a + b
    final = result & 255

    print("Binary Addition:", binary(final))
    print("Final Binary Result:", binary(final))
    print("Final Decimal Result:", signed_value(final))

    if (a >= 0 and b >= 0 and signed_value(final) < 0) or \
       (a < 0 and b < 0 and signed_value(final) >= 0):
        print("Overflow: Yes")
    else:
        print("Overflow: No")


print("8-BIT SIGNED BINARY ARITHMETIC")

print("\nExpression 1: 120 + (+62)")
addition(120, 62)

print("\nExpression 2: (-120) + (-62)")
addition(-120, -62)