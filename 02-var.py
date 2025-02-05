# Two types of variables

# 1) String variables
# 2) Number variables

user_name = "Siddhu";
print(user_name);

user_id = 109756;
print(user_id);


# Placeholders (%s) - allows us to print variables in print statement. 
# %s - it is the placeholder, it holds the place of a variable.
# % <variable_name>
# Similar to concatenation, but In python concatenate wont work with string and num.

print('Welcome %s' % user_name);
print("ID %s" %user_id);

# For multiple placeholders
print("Welcome %s and your ID is %s." % (user_name,user_id));