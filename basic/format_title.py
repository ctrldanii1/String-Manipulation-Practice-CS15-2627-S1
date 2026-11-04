string_to_process = "t H e , T a L e :: O f , T w O :: c I t I e S"

clean = string_to_process.replace(',', ' ').replace('::', ' ').title()
print(clean)

# Expected Output: The Tale Of Two Cities