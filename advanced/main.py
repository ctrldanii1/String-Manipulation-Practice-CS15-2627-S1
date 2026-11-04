print("1. Format Name")
print("2. Format Title")
print("3. Format List")
print("4. Process Numbers")

choice = input("Choose an option (1-4): ")

if choice == "1":
    print("Format Name")
    name = input("Enter a name (like: Daniella Adegun): ")
    parts = name.split(" ")
    if len(parts) == 2:
        last_name = parts[1]
        first_name = parts[0]
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")

elif choice == "2":
    print("Format Title")
    title = input("Enter a title: ")
    clean = title.replace(',', ' ').replace('::', ' ').title()
    print(clean)

elif choice == "3":
    print("Format List")
    list = input("Enter a list: ")
    items = [item.strip().upper() for item in list.split(',')]
    Final_list = " | ".join(items)
    print(Final_list)

elif choice == "4":
    print("Process Numbers")
    number = input("Enter a number: ")
    clean = number.split(',')
    cleaned_number = [int(num) for num in clean]

    total = sum(cleaned_number)
    average = (total / len(cleaned_number))

    print(total)
    print(average)

else:
    print("Please choose numbers 1 - 4")