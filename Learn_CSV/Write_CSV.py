import csv


with open('test.csv', 'w', newline="") as file:
    write = csv.writer(file)

    heading = ["S.No", "Name", "Email"]
    write.writerow(heading)

    data = [
            [1, "Divya", "divya@gmail.com"],
            [2, "Sarath", "sarath@gmail.com"],
            [3, "Babu", "babu@gamil.com"]
            ]
    write.writerows(data)
