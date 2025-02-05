# Lists - []. A set of items. It could be set of numbers or strings.

shopping_list = ['bread','butter','jam','peanut butter']
print(shopping_list);

print(shopping_list[0]);
print(shopping_list[-1]);

# Add to list - append() method
shopping_list.append('cheese');
print(shopping_list);

# Replace
shopping_list[3] = "eggs";
print(shopping_list);

# Delete Item - remove() method
shopping_list.remove('jam');
print(shopping_list);

# List Concatenate - Gives you 2D List (Lists inside List)
students = ['Siddhu','Vinay','Sabharish'];
scores = [60,80,100];

student_scores = [students,scores];
print(student_scores);
print(student_scores[0][2])
print(student_scores[1][2])

# Sort method returns None.
# Strings - Alphabetical order and Numbers - Ascending order.
students.sort()
print(students)

scores.sort();
print(scores);