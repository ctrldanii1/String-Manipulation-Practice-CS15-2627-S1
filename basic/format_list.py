string_to_process = "eggs,cheese,milk,bread,cereal"

clean = string_to_process.split(',')
uppercase_items = [item.upper() for item in clean]
result = " | ".join(uppercase_items)
print(result)

# Expected Output: "EGGS | CHEESE | MILK | BREAD | CEREAL"