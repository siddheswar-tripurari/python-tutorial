# Maps - like a dictionary
# They are a collection of Lists and Tuples.
# They allow you to specify lists in a form of key-value pair.

student_scores  ={'Siddhu':60,'Vinay':80,'Sabharish':100};
print(student_scores)
print(student_scores['Siddhu'])

# Change value
student_scores['Siddhu'] = 75
print(student_scores)


# Tuple in Maps
days = ('Mon','Tue','Wed','Thur','Fri','Sat','Sun')
activities = {days[0]:'swimming',days[1]:'cycling',days[2]:'reading',days[3]:'writing',days[4]:'walking',days[5]:'running',days[6]:'jogging'}
print(activities);
print(activities['Tue']);

# Delete key
del activities['Tue']
print(activities)

# Create key
# If key is there, it will update the value, otherwise it will create a new key with given value.
activities['Tue'] = 'cycling'
print(activities);