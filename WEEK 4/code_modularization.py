# numbers = (2, 6, 9, 9, 0)
# print(enumerate(numbers)) 

# # map()
# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, nums)) #Anonymous function
# print(squared)  # [1, 4, 9, 16]

# # filter()
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums)  # [2, 4]

# Student Performance & Feedback System

# Step 1: Input student data
# names = [input(f"Enter name for student {i}: ") for i in range(1, 4)]

# name1 = input("Enter first student name: ")
# score1 = int(input("Enter score for " + name1 + ": "))

# name2 = input("Enter second student name: ")
# score2 = int(input("Enter score for " + name2 + ": "))

# name3 = input("Enter third student name: ")
# score3 = int(input("Enter score for " + name3 + ": "))

# # Step 2: Store in lists
# names = [name1, name2, name3]
# scores = [score1, score2, score3]

# # Step 3: Display data
# print("\nStudent Data:")
# for index, (n, s) in enumerate(zip(names, scores)):
#     print(f"{index + 1}. {n} - {s}")

# # Step 4: Summary using built-ins
# total = sum(scores)
# average = round(total / len(scores), 2)
# highest = max(scores)
# lowest = min(scores)

# print("\nPerformance Summary:")
# print("Total Score:", total)
# print("Average Score:", average)
# print("Highest Score:", highest)
# print("Lowest Score:", lowest)

# # Step 5: Ranking (using sorted and zip)
# ranked = sorted(zip(scores, names), reverse=True)
# print("\nRanking:")
# for rank, (score, name) in enumerate(ranked, 1):
#     print(f"{rank}. {name} - {score}")

# # Step 6: Check data types
# print("\nData Type Checks:")
# print("Type of names:", type(names))
# print("Type of scores:", type(scores))
# print("ID of names list:", id(names))
# print("ID of scores list:", id(scores))

# # Step 7: Filter passing students (>=50)
# passing = list(filter(lambda s: s >= 50, scores))
# print("\nPassing Scores:", passing)

# # Step 8: Map names to uppercase
# upper_names = list(map(lambda n: n.upper(), names))
# print("Uppercase Names:", upper_names)

# # Step 9: Use help() to show documentation of len
# print("\nHelp on len():")
# help(len)


# # I just made use of most of the built-in functions. You can write your own version of this code. Just think through it.

# def count_up_to(n):
#     i = 1
#     print("11111")
#     while i <= n:
#         print("2222")
#         yield i   # pause and return i
#         i += 1
#         print("3333")

# # Using the generator
# for number in count_up_to(7):
#     print(number)

# # Note the output: Instead of giving all numbers at once, the function yields them one at a time.

# def introduce(name, track = "AI Engineering"):
#     print("My name is", name)
#     print("I am learning", track+".")

# # function call
# # Without specifying the default argument, but watch the ouput
# introduce("Paul", "AI Development")  

# def add_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     print("Sum:", total)

# # function call 
# # Take note of the output
# add_numbers(2, 4, 6)
# add_numbers(10, 20, 30, 40, 50)

# def student_details(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)


# # function call - Take note of the output
# student_details(name="Peter", track = "AI Engineering", interest="Block Chain")

# Define student profile function

# Ensure to not the order of arrangement of the types of arguments used.
# This is how to arrange it of you are using everything or some of the together

# def participant_profile(name, age, track="AI Development", *skills, **extra_info):
#     """
#     Generate a profile for a bootcamp participant using different types of arguments.
#     """
#     profile = f"\n--- Bootcamp Participant Profile ---\n"
#     profile += f"Name: {name}\n"
#     profile += f"Age: {age}\n"
#     profile += f"Track: {track}\n"

#     # Skills (from *args)
#     if skills:
#         profile += "Skills: " + ", ".join(skills) + "\n"
#     else:
#         profile += "Skills: Not yet specified\n"

#     # Extra info (from **kwargs)
#     if extra_info:
#         profile += "Additional Info:\n"
#         for key, value in extra_info.items():
#             profile += f" - {key.capitalize()}: {value}\n"

#     return profile  # Do you remember `return` and why it is used? We are using it so it can be reused in other places

# profile1 = participant_profile("Dasaolu Samuel", 19, skills = ['hacker', 'coder'], dream = 'item3')
# print((profile1))

# # ---------- LEts test ----------

# # Example 1: Using only positional arguments
# print(participant_profile("Peter", 24))

# # Example 2: Adding keyword/default argument
# print(participant_profile("Ridwan", 29, track="AI Engineering"))

# # Example 3: Adding variable-length positional arguments (*args)
# print(participant_profile("David", 27, "Data Science", "Python", "SQL", "Machine Learning"))

# # Example 4: Adding variable-length keyword arguments (**kwargs)
# print(participant_profile(
#     "Sophia", 30, "Cybersecurity",
#     "Networking", "Ethical Hacking", "Python",
#     interest="Blockchain", city="Shagamu", phone="08123456789"
# ))

# x = "global x"   # Global Namespace

# def outer():
#     x = "enclosing x"  # Enclosing Namespace
    
#     def inner():
#         x = "local x"  # Local Namespace
#         print("Inside inner:", x)  # Local wins
    
#     inner()
#     print("Inside outer:", x)  # Enclosing
    
# outer()
# print("In global:", x)  # Global

# # Watch the output
# # Notice how Python searches in the order Local → Enclosing → Global → Built-in (LEGB).

### Global keyword

# Used when you want to modify a global variable inside a function.

# x = 5

# def change_global():
#     global y  #Actually creates a new global variable
#     y = 10   # modifies the global x

# change_global()
# print(y)  # Output: 10

# # Watch the output

# nonlocal keyword

#Used in nested functions when you want to modify the variable from the enclosing scope (not global).

def outer():
    x = "outer x"
    
    def inner():
        nonlocal x
        x = "changed by inner"
        print("Inside inner:", x)
    
    inner()
    print("Inside outer:", x)

outer()

# Watch the output