import  csv

# Way 1
# with open('test.csv') as file:
#     data = csv.reader(file)
#     for i in data:
#         for j in i:
#             print(j)

# Way 2
# with open('test.csv') as file:
#     data = csv.reader(file)
#     for i in data:
#         print(i[0].ljust(10), i[1].ljust(15), i[2])

# Way 3
with open('test.csv') as file:
    data = csv.DictReader(file)
    for i in data:
        print(i['S.No'].ljust(10), i['Name'].ljust(15), i['Email'])