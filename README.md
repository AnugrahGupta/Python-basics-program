## Question 1: Write a Python program that reads two decimal values as program argu-
ments, and prints the following output (e.g. by passing the arguments 13
and 5, such as python program.py 13 5):
13.0 + 5.0 = 18.0
13.0 - 5.0 = 8.0
13.0 * 5.0 = 65.0
13.0 / 5.0 = 2.6
13.0 ** 5.0 = 371293.0
(a) Pass different values as arguments to your program, and check that
the output is still correct.

## Question 2: Write a Python program called create customer.py that everytime it is
executed, appends a new customer to a file passed as a program argu-
ment (e.g. customers.txt), containing a customer name and ID per line.
Your program should read the customer details (using input()), and write
those details into the specified file. Example execution:
$ python create customer.py customers.txt
Costumer name: John Smith
Costumer ID: 123
$ python create customer.py customers.txt
Costumer name: James Bond
Costumer ID: 007

## Qustion 3: Write a Python program called list customers.py that accepts a file-
name as an argument, and prints the contents of that file. Example exe-
cution (using the file created in the previous exercise):
$ python list customers.py customers.txt
Costumers saved in file ’customers.txt’:
John Smith 123
James Bond 007
