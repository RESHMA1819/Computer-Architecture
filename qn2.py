print("LOGICAL SHIFT OPERATIONS")

# Logical Left Shift
num = 0b10110110

print("\nLogical Left Shift")
print("Original Number:", format(num, '08b'))

for i in range(3):
    num = (num << 1) & 255
    print("After shift", i + 1, ":", format(num, '08b'))

print("Final Result:", format(num, '08b'))


# Logical Right Shift
num = 0b11010100

print("\nLogical Right Shift")
print("Original Number:", format(num, '08b'))

for i in range(3):
    num = num >> 1
    print("After shift", i + 1, ":", format(num, '08b'))

print("Final Result:", format(num, '08b'))