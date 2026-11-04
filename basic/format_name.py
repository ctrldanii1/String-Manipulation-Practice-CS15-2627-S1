string_to_process = "   sMitH, aLeX    "

fix_string = string_to_process.strip()
parts = fix_string.split(',')
first_part = parts[1].strip().title()
second_part = parts[0].strip().title()
print(f"{first_part} {second_part}")

# Expected output: "Alex Smith"