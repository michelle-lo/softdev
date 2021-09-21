import random

pd1 = ["Michelle Lo", "Rayat Roy", "Theodore Fahey", "Naomi Narajo",
    "Lucas Lee", "William Chen", "Rengguang Zheng", "Owen Yaggy"]
pd2 = ["Joshua Kolepfer", "Alif Abdullah", "Yoonah Chang"]

total = pd1 + pd2
x = random.randint(0, len(total) - 1)
print(total[x])
