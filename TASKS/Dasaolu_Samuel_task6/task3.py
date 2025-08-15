"""
**Task3: Simulate a football match ticket system**

- Store all seat numbers (1 to 50) in a set.

- Ask users to "book" a seat by entering the number.

- Remove booked seats from the set.

- Show remaining seats after each booking.
"""

seats = set(range(1, 51))
print(seats)

for seat in range(1,51): 
    user_seat = int(input("Please book an available seat (1-50): "))
    seats.discard(user_seat)
    print("Remaining Seats: \n", seats)