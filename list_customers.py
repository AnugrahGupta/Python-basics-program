from sys import argv
filename = argv[1]
listcontent = open(filename, "r")
content = listcontent.read()
print("Customers saved in file 'customers.txt':\n",content)

