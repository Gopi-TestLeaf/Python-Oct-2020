# Way 1
file = open('text1.txt', mode='w')
for i in range(1, 11):
     file.write(f"Hello {i}, pls wake-up..... \n")
print(file.closed)
file.close()
print(file.closed)

# Way 2
with open('text2.txt', mode='w') as file:
    for i in range(1, 11):
        file.write(f"Hello {i}, pls wake-up..... \n")
