# Task 10
print("This is Task 0")
school_name = input("Enter the school name: ")
tuition_fee = float(input("Enter the tuition fee: "))
hostel_fee = float(input("Enter the hostel fee: "))
feeding_fee = float(input("Enter the feeding fee: "))
total_fee = tuition_fee + hostel_fee + feeding_fee
print(f"\n--- {school_name} School Fees Receipt ---\n\tTuition Fee: {tuition_fee:,.2f}\n\tHostel Fee: {hostel_fee:,.2f}\n\tFeeding Fee: {feeding_fee:,.2f}\n\t \n\tTotal Fee: {total_fee:,.2f}")
