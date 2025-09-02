# class NigerianBankAccount:
#     def __init__(self, owner, initial_balance=0):
#         self.owner = owner
#         self._balance = initial_balance        # Protected attribute
#         self.__pin = "1234"                   # Private attribute
#         self._transaction_history = []        # Protected attribute

#     # Public methods - anyone can use these
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             self._transaction_history.append(f"Deposited ₦{amount:,}")
#             return f"₦{amount:,} deposited successfully"
#         return "Invalid deposit amount"

#     def withdraw(self, amount, pin):
#         if self.__verify_pin(pin):  # Uses private method
#             if amount <= self._balance:
#                 self._balance -= amount
#                 self._transaction_history.append(f"Withdrew ₦{amount:,}")
#                 return f"₦{amount:,} withdrawn successfully"
#             return "Insufficient funds"
#         return "Invalid PIN"

#     def check_balance(self, pin):
#         if self.__verify_pin(pin):
#             return f"Current balance: ₦{self._balance:,}"
#         return "Invalid PIN"

#     # Private method - only the class can use this
#     def __verify_pin(self, entered_pin):
#         return entered_pin == self.__pin

#     # Protected method - subclasses can use this
#     def _get_transaction_history(self):
#         return self._transaction_history.copy()

#     # Using the encapsulated account
# ibrahim_account = NigerianBankAccount("Ibrahim Orekunrin", 50000)

# # These work - public interface
# print(ibrahim_account.deposit(10000))      # ₦10,000 deposited successfully
# print(ibrahim_account.withdraw(5000, "1234"))  # ₦5,000 withdrawn successfully
# print(ibrahim_account.check_balance("1234"))   # Current balance: ₦55,000

# # print(str(ibrahim_account.__pin).copy())           # Error! Cannot access private attribute
# print(ibrahim_account._get_transaction_history() \
# )

# from abc import ABC, abstractmethod

# # Abstract base class - defines what a Nigerian student should do
# class NigerianStudent(ABC):
#     def __init__(self, name, course, level):
#         self.name = name
#         self.course = course
#         self.level = level
#         self.fees_paid = False
    
#     # Concrete method - all students can do this
#     def pay_school_fees(self, amount):
#         self.fees_paid = True
#         return f"{self.name} paid ₦{amount:,} school fees"
    
#     # Abstract method - each type of student implements differently
#     @abstractmethod
#     def study_method(self):
#         pass
    
#     @abstractmethod
#     def take_exam(self):
#         pass

# # Concrete classes - specific implementations
# class MedicalStudent(NigerianStudent):
#     def study_method(self):
#         return f"{self.name} studies anatomy books and practices on cadavers"
    
#     def take_exam(self):
#         return f"{self.name} takes practical exam in the anatomy lab"

# class EngineeringStudent(NigerianStudent):
#     def study_method(self):
#         return f"{self.name} solves mathematical problems and builds prototypes"
    
#     def take_exam(self):
#         return f"{self.name} takes exam with calculations and technical drawings"

# class ComputerScienceStudent(NigerianStudent):
#     def study_method(self):
#         return f"{self.name} codes programs and debugs software"
    
#     def take_exam(self):
#         return f"{self.name} takes practical programming exam on computer"
    
    
#     # Using abstraction
# students = [
#     MedicalStudent("Dr.Adeyinka Ogunsanya", "Medicine", 400),
#     EngineeringStudent("Dr. Ajala Gift", "Mechanical Engineering", 300),
#     ComputerScienceStudent("Fatima Hassan", "Computer Science", 200)
# ]


# # Same interface, different implementations
# for student in students:
#     print(student.pay_school_fees(150000))  # Same for all
#     print(student.study_method())           # Different for each
#     print(student.take_exam())              # Different for each
#     print("---")

#Simple abstraction for phone interface

class SimplePhone:
    def __init__(self, brand):
        self.brand = brand
        self._complex_internal_system = "Very complicated stuff"
    
    # Simple interface - user doesn't need to know internal complexity
    def make_call(self, number):
        self._establish_network_connection()
        self._encode_voice_signal()
        self._transmit_to_tower()
        return f"Calling {number} from {self.brand} phone..."
    
    def send_sms(self, message, number):
        self._connect_to_sms_center()
        self._format_message()
        self._send_through_network()
        return f"SMS sent to {number}: '{message}'"
    
    # Complex internal methods - hidden from user
    def _establish_network_connection(self):
        # Complex networking code here
        pass
    
    def _encode_voice_signal(self):
        # Complex audio processing here
        pass
    
    def _transmit_to_tower(self):
        # Complex radio transmission here
        pass
    
    def _connect_to_sms_center(self):
        # complex code
        pass
    
    def _format_message(self):
        pass
    
    def _send_through_network(self):
        pass
    # User only needs to know the simple interface
my_phone = SimplePhone("Tecno")
print(my_phone.make_call("08012345678"))  # Simple to use
print(my_phone.send_sms("How far?", "08098765432"))  # Don't need to know internals