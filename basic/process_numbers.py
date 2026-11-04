string_to_process = "  18,27,35,20  "

cleaned = string_to_process.strip()
parts = cleaned.split(',')
numbers = [int(num) for num in parts]

sum = sum(numbers)
average = sum / len(numbers)

print(f"total: {sum}")
print(f"average: {average}")

# Expected Output:
# "Total: 100"
# "Average: 25.0"