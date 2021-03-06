my_input = """
15335876
15086442
"""

test_input = """
5764801
17807724
"""

my_input=my_input.split("\n")[1:-1]


card_pkey = int(my_input[0])
door_pkey = int(my_input[1])


card_loopsize = 0

temp = 1
while temp != card_pkey:
	temp = (temp * 7) % 20201227
	card_loopsize += 1
print(f"Card's Loopsize: {card_loopsize}")

door_loopsize = 0
temp = 1
while temp != door_pkey:
	temp = (temp * 7) % 20201227
	door_loopsize += 1
print(f"Door's Loopsize: {door_loopsize}")

temp = 1
for i in range(card_loopsize):
	temp = temp * door_pkey % 20201227
print(f'Part 1: {temp} (card -> door)')
