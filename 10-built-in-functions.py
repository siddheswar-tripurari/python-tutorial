# Len function - takes any string, list, map, tuple as an argument and returns its length.

def calc_length(argument):
    print(len(argument))

calc_length("Siddheswar Tripurari")
calc_length([1,2,3,45])
calc_length({'wf':1,'gwg':2})


# Example

# Count the particular letters and return a map

char_map = {}
def count_letters(args):
    for x in range(0,len(args)):
        for y in range(0,len(args[x])):
            key = args[x][y]
            if(key in char_map):
                char_map[key] += 1
            else:
                char_map[key] = 1
    print(char_map)

count_letters(['arwrwrwrwa','rrwrwrbb','ccrwwegweijgkewrg'])



# Max and min methods. pass the list as an argument to the methods

test_scores = [12,324,53,53,131]
print(max(test_scores))
print(min(test_scores))


# Sum methods
print(sum(test_scores))

# dir method tells us what method we can use for a value
print(dir([1,2,3]))
print(dir("Siddhu"))

# help method gives us the function description
print(help("Siddhu".lower))
