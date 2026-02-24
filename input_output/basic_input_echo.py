"""
Task 4 - Basic input echo (easy)
Take input: name, city and print: Hello <name> from <city>
Updated task - make the first letter of name and city uppercase
"""
name_input = input("Enter you name: ")
city_input = input("Enter the name of your city: ")

name = name_input.capitalize()
city = city_input.capitalize()

print(f"Hello {name} from {city}")
