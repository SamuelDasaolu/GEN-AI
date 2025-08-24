"""
**Task1: Fruit collector**
- Ask the user to enter 5 favourite fruits. Store them in a set and display the set.
"""

i = 1
fruits = set()
try:
    while i <= 5:
        try:
            favorite_fruit = input(f"Favorite Fruit {i}: ")
            if not favorite_fruit.strip():
                print("Fruit name cannot be empty. Please enter a valid fruit name.")
                continue
            if favorite_fruit.strip() in fruits:
                print('That fruit has been entered before')
                continue
            else:
                fruits.add(favorite_fruit.strip())
                i += 1
        except EOFError:
            print("\nEnd of file reached. Stopping input.")
            break
        except KeyboardInterrupt:
            print("\nInput cancelled by user. Stopping input.")
            break
        except Exception as e:
            print(f"An unexpected error occurred during input: {e}")
            break
    print(fruits)
except Exception as e:
    print(f"An unexpected error occurred during the fruit collection process: {e}")
    print(f"Fruits collected so far: {fruits}")
finally:
    print("\nFruit collection process finished.")