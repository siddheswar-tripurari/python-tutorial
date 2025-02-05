# Fuctions
# Some pre built functions - print(), input()
# Functions can be built-in or user defined



def sayHello():
    print("Hello World")

# sayHello()

def sayMyName(name):
    print("Person X: You are %s" % name)
    print("Walter white: You are goddamn right!!")

# sayMyName("Siddhu")

# Example - Sort with out using method

def array_sort(num_array):
    for i in range(0,len(num_array)):
        for j in range(i+1,len(num_array)):
            if(num_array[i] > num_array[j]):
                temp = num_array[i]
                num_array[i] = num_array[j]
                num_array[j] = temp
    return num_array

sort_array = array_sort([1,3,4,2,1,7,0])
print(sort_array)

