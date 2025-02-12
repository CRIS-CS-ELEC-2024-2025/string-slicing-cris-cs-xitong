'''
Arsher, Grade 9 CS Elec
Assignment: String Slicing
This assignment will demonstrate how to manipulate and print strings.
'''

# DO NOT EDIT THIS LINE
country = "the united states of america"

# 1. print the country in *lower case*
print(country.lower())

# 2. print country in *title case*
print(country.title())

# 3. print country in *upper case*
print(country.upper())

# 4. print the length of the country string as:
#    string length of country: <length>
print("string length of country: " + str(len(country)))

# 5. slice the string "america" from country, upper case the 'a',
#    and store it in a variable named `short_name` with a value "America"
short_name = country[-7:].capitalize()
print(short_name)

# 6. concantentate a string value with `short_name` to
#    produce the name of the continent where the country resides
#    and print the result:
#    <title case country> is located within <title case continent>
continent = "North " + short_name
print(country.title() + " is located within " + continent)

# 7. print a statement how we refer to people from the country:
#    People from <title case country> are called <title case of people in plural>
people = short_name + "ns"
print("People from " + country.title() + " are called "  + people)
