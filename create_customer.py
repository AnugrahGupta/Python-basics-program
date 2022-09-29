from sys import argv
customerinfo = argv[1]

name = input("Customer Name:")
id = input("Customer ID:")
book = open(customerinfo, "a")
CustomerName = book.writelines(name + id + "\n")
book.close()


