"""
**Task1: Your Favorite Life Quote**
- Ask the user to input their favorite quote.

- Convert it to title case.

- Print it with quotation marks using escape sequences.
"""
user_quote = input("Please enter your favorite quote: ")
formatted_quote = user_quote.title()
print("\""+formatted_quote+"\"")