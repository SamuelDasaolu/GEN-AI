"""
**Task3: Simulate a football match ticket system**

- Store all seat numbers (1 to 50) in a set.

- Ask users to "book" a seat by entering the number.

- Remove booked seats from the set.

- Show remaining seats after each booking.
"""

seats = set(range(1, 5))

while True:
    print("\n Remaining Seats: \n", seats)
    user_seat = int(input("Please book an available seat (1-50): "))
    if len(seats) == 0:
        print(" \n No More Seats Available for Booking")
        break
    
    elif user_seat not in seats:
        print("\n Invalid Selection You can only select from the available seats below")
        continue
    print(f"Seat {user_seat} booked successfully")
    seats.discard(user_seat)
    