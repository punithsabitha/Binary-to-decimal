# Binary To Decimal Converter

binary = input("Enter your Binary: ")

decimal = 0
power = 0

# Process binary from right to left
for digit in reversed(binary):
    if digit == '1':
        decimal += 2 ** power
    power += 1

print("Decimal :", decimal)
