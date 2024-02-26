#Continue by removing the odd numbers from the list and replacing the even numbers with their double value

#print the list at the end

import random
random_numbers = []
new_list = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
for i in range(len(random_numbers)):
    if random_numbers[i] % 2 == 0:
        j = random_numbers[i] = 2*i
        new_list.append(j)

print(new_list)










