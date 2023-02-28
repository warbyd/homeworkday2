users = {
    "Jonathan": {
        "twitter": "jonnyt",
        "lottery_numbers": [6, 12, 49, 33, 45, 20],
        "home_town": "Stirling",
        "pets": [
            {
              "name": "fluffy",
              "species": "cat"
            },
            {
              "name": "fido",
              "species": "dog"
            },
            {
              "name": "spike",
              "species": "dog"
            }
        ]
    },
    "Erik": {
        "twitter": "eriksf",
        "lottery_numbers": [18, 34, 8, 11, 24,],
        "home_town": "Linlithgow",
        "pets": [
            {
              "name": "nemo",
              "species": "fish"
            },
            {
              "name": "kevin",
              "species": "fish"
            },
            {
              "name": "spike",
              "species": "dog"
            },
            {
              "name": "rupert",
              "species": "parrot"
            },
            {
              "name": "fluffy",
              "species": "dog"
            }
        ]
    },
    "Avril": {
        "twitter": "bridgpally",
        "lottery_numbers": [12, 14, 33, 38, 9, 25],
        "home_town": "Dunbar",
        "pets": [
            {
              "name": "monty",
              "species": "snake"
            }
        ]
    },
    "Dale": {
        "twitter": "dale123",
        "lottery_numbers": [1, 2, 3, 4, 5],
        "home_town": "Cardiff",
        "pets": [
            {
              "name": "snuggles",
              "species": "dog"
            }
        ]
    }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
# 2. Get Erik's hometown
# 3. Get the list of Erik's lottery numbers
# 4. Get the species of Avril's pet Monty
# 5. Get the smallest of Erik's lottery numbers
# 6. Return an list of Avril's lottery numbers that are even
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
# 8. Change Erik's hometown to Edinburgh
# 9. Add a pet dog to Erik called "fluffy"
# 10. Add another person to the users dictionary

print(users["Jonathan"]["twitter"])

print(users["Erik"]["home_town"])

print(users["Erik"]["lottery_numbers"])


print(users["Avril"]["pets"])

if "species" in users:
    print("yes")
else:
    print("No")

print(users["Erik"]["lottery_numbers"][-3])

out = []
for num in (users["Avril"]["lottery_numbers"]):

    if num % 2 == 0:
        out.append(num)

print(out)

users["Erik"]["home_town"] = "Edinburgh"

print(users["Erik"]["home_town"])

users["Erik"]["lottery_numbers"] = 12, 14, 33, 38, 9, 25, 7


print(users["Erik"]["lottery_numbers"])







print(users["Erik"]["pets"])

print(users["Dale"])

# Question 4 and 9








