import csv


with open("data.csv", "w") as file:  # To open and I write to CSV file
    writer = csv.writer(file)  # This allows you to write into the file
    # This how to write to rows in csv
    writer.writerow(["transaction_id", "transaction_date", "customers_name"])
    writer.writerow([1001, "02-02-2020", "samson"])
    writer.writerow([1001, "02-02-2020", "samson"])
    writer.writerow([1001, "02-02-2020", "samson"])
    writer.writerow([1001, "02-02-2020", "samson"])


with open("data.csv", "r") as file:
    reader = csv.reader(file)
    # print(list(reader)) # You can also print the reader out as list
    for row in reader:  # You can iterate over the reader
        print(row)
    file.close()

"""
Alternatively
"""
# Writing
with open("test.csv", "w") as newTestfile:
    if newTestfile.mode == "w":
        for i in range(5):
            newTestfile.write("new attributes")
    newTestfile.close()


# Closing of the file is not necessary when With is used to Open the file
# Reading
with open("test.csv", "r") as newTestfile2:
    if newTestfile2.mode == " r":
        newTestfile2 = newTestfile2.readlines()
        for i in newTestfile2:
            print(i)
    newTestfile2.close()

    """
    OR
    """
    #  These reads the entire file at a go
    newTestfile2 = newTestfile2.read()
    print(newTestfile2)


