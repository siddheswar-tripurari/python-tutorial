for x in range(0,10, 1):
    print('Hi %s' % x)

# The first line creates a variable 'x' and initializes it value 0 (takes from range).
# range(0,10) -> (init,limit). similar to x = 0; x < 10
# python checks if the var is in the range. if true, it prints and increments the x by 1 and checks it.

count = 0
my_list = [1,2,3,4,5,6,7,8,9]
for x in my_list:
    my_list[count] = x*x
    count = count + 1

print(my_list)

# At each iteration in the list, x will hold the value of an element in the list.
# first ite - 1,sec - 2, third - 3........


# Loop through Maps

days = ('Mon','Tue','Wed','Thur','Fri','Sat','Sun')
activities = {days[0]:'swimming',days[1]:'cycling',days[2]:'reading',days[3]:'writing',days[4]:'walking',days[5]:'running',days[6]:'jogging'}

for x in activities:
    print("On %s I will be %s." % (x,activities[x]))

# x at each iteration will hold the value of the key.



# While loop

balance = 0

while(balance <= 1000):
    money = float(input("Add money: "));
    balance = balance + money
    print("Current Balance: %s " % balance);

print("You have reached your target.")