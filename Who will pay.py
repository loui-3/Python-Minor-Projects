# Side project: Who will pay?
import random
freinds = ["Carl", "Bryan", "Tol", "Kupal"]
print(random.choice(freinds))

# or 

random_freinds = random.randint(0, 3)
if random_freinds == 0:
    print(freinds[0])
elif random_freinds == 1:
    print(freinds[1])
elif random_freinds == 2:
    print(freinds[2])
else:
    print(freinds[3])

# or

random_freinds = random.randint(0, 3)
print(freinds[random_freinds])