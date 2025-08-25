"""
**Task3: Simulate a football match ticket system**

- Store all seat numbers (1 to 50) in a set.
- Ask users to "book" a seat by entering the number.
- Remove booked seats from the set.
- Show remaining seats after each booking.
"""

seats = set(range(1, 51))  # seats from 1 to 50

try:
    while True:
        if len(seats) == 0:
            print("\n No More Seats Available for Booking")
            break

        print("\n Remaining Seats: \n", seats)

        try:
            user_seat = int(input("Please book an available seat (1-50) or enter 0 to quit: "))
        except ValueError:
            print("Invalid input. Please enter a valid seat number.")
            continue

        if user_seat == 0:  # Exit condition
            break

        if user_seat not in seats:
            print("\n Invalid Selection. You can only select from the available seats.")
            continue

        print(f"Seat {user_seat} booked successfully")
        seats.discard(user_seat)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Ticket booking session ended.")
    print(f"Final Remaining Seats: {seats}")
