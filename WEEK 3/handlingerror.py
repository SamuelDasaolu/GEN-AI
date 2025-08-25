# for i in range(3):
# print(i)   # Wrong indentation

# if 5 > 3   # Missing colon
#     print("Hello")

# print "Hello"   # Missing parentheses in Python 3

# x = 10 / 0   # This will throw error

try: 
    print("Hello Try")
    number = int("abc")   # ValueError
    x = 10 / 0
    print(x)


except ZeroDivisionError:
    print("Hellow Except")
    
except:
    print("Invalid conversion to integer.")