"""
**Task3: Simulate a football match ticket system**

- Store all seat numbers (1 to 50) in a set.

- Ask users to "book" a seat by entering the number.

- Remove booked seats from the set.

- Show remaining seats after each booking.
"""

seats = set()
seat_generator = range(1, 51)
for seat in seat_generator: 
    seats.add(seat)
    user_seat = int(input("Please book a seat (1-50)"))
    seats.remove(user_seat)
    print("Remaining Seats: \n", seats)
