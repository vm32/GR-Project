def check_accident(input_value):
    if input_value > 1:
        print("Accident detected")
    else:
        print("No accident detected")

input_value = float(input("Enter a value from the web page: "))
check_accident(input_value)
