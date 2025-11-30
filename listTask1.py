import random

friends = ["Alice", "Bob", "charlie", "David", "Emanual"]

print("option 1")

rand_name_from_list = random.choice(friends)
print(rand_name_from_list)

print("option 2")

rand_list = random.randint(0, 4)
print(friends[rand_list])


us_states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California",
    "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
    "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
    "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

print(len(us_states))
fruits = ["Strawberries", "Grapes", "Peaches", "Cherries",  "Pears", "Apples", "Blackberries", "Blueberries"]
vegies = ["Spinach", "Kale", "Nectarines", "Potatoes"]


dirty_dozen = [fruits, vegies]

print(dirty_dozen[1][1])
