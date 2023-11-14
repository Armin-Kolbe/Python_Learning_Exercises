#---------------------Exercise 09 (Mini Project 02: Booking Car)-------------------------
# Question 02 >>>
# This block of the code is repeated several times, fix the issue by function.
# print(5*"*" + str(code) + "+")</p>
# print(f"name : {booking['name]}")
# print(f"start data : {booking['start_date]"})
# print(f"end data : {booking['end_date]"})

# Question 03 >>>
# Create an update_booking function, allowing changes to the 'name',
# 'start date', and# 'end date' of bookings. Users should be able to select 
#a booking by its unique code and enter new details.

# Question 04 >>>
# Develop a sort_bookings function that organizes bookings based on their 'start date'.
# The function should offer options for both ascending and descending order sorting.
# ---------------------------------------------------------------------------------------

# Importing necessary liberaries
import datetime

# Dictionary to save booking information
bookings = {}
# Constant for total number of cars
total_cars = 10
# Variable to generate unique booking codes
code = 1

# ----------------Functions----------------
# Function to display help information
# update and sort NEW Question 03 and Question 04
def help():
  help_text = """
    booking: Make a Booking
    display: show all Booking
    search: Search Booking
    cancel: Cancel Booking
    details: show details of the project
    update: update the Booking by names or start date or end date 
    sort: sort by new date to old date or reverse   
    exit: exit\n"""
  print (help_text)

def validate_date(input_date):
  c = input_date.count("-")
  # Check format of date
  if c != 2 or len(input_date) != 10 or input_date[4] != "-" or input_date[7] != "-":
    return False, "Invalid Format (YYYY-MM-DD)"
  # Check if year, month, and day are all digits
  parts = input_date.split("-") # [2020, 12, 15]
  if not (parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit()):
    return False, "should be numbers"
  # Validate the range of year, month, and day
  year, month, day = list(map(int, parts))
  if year < 1 or not (1 <= month <= 12) or not (1 <= day <= 31):
    return False, "Invalid date"
  return True, "Valid date"

# Function to handle booking of cars
def booking():
  global code # Declare code as global since we're modifying it
  # Check if all cars are already booked
  if len(bookings) >= total_cars:
    print("all cars are booked!")
    return
  name = input("enter you name: ")
  start_date = input("start date: ")
  end_date = input("end date: ")
  # Validate the provided dates
  is_valid, msg = validate_date(start_date)
  if not is_valid:
    print(msg)
    return
  is_valid, msg = validate_date(end_date)
  if not is_valid:
    print(msg)
    return
  # Convert string dates to datetime
  start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
  end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
  count_days = (end_date - start_date).days
  # Check if the end date comes before the start date
  if start_date > end_date:
    print("Error!")
    return
  # Create new booking
  new_booking = {
    "name" : name, 
    "start_date" : start_date,
    "end_date" : end_date,
    "days" : count_days
  }
  print(new_booking)
  # save with new code
  bookings[code] = new_booking
  # Increment the booking code for the next booking
  code += 1
  print("Done!")

# Function to cancel a booking
def cancel(code_del):
  bookings.pop(code_del, "not found!")

# Function to print (Question 02)        <----  NEW Question 02

def print_d(booking):
    print(5*"*" + str(code) + 5*"*")
    print(f"name : {booking['name']}")
    print(f"start date : {booking['start_date']}")
    print(f"end date : {booking['end_date']}")
    print(f"days : {booking['days']}")


# Function to display all current bookings
def display():
  if len(bookings) != 0:
    for code, booking in bookings.items():
        print_d(booking)   ## <----------------------- Changed Question 02
  else:
    print("empty")

# Function to search for a booking using its code
def search_by_code(code_s):
  if code_s in bookings:
    booking = bookings[code_s]
    print_d(booking)   ## <----------------------- Changed Question 02
  else:
    print("not found!")

def search_by_name(name):
  found = False
  for code, booking in bookings.items():
    if booking["name"] == name:
      print_d(booking)   ## <----------------------- Changed Question 02
      found = True
  if not found:
    print(f"{name}: not found!")
  

def search():
  cmd = input("search by 'name' or 'code': ")
  if cmd == "name":
    name = input("name for search: ")
    search_by_name(name)
  if cmd == "code":
    code_s = int(input("code for search: "))
    search_by_code(code_s)
  else:
    print("not found!")

# Details to show a details of the cars
def details():
  num_booked_cars = len(bookings)
  num_available_cars = total_cars - num_booked_cars
  print(f"Total number of cars: {total_cars}")
  print(f"number of booked: {num_booked_cars}")
  print(f"number of availabel: {num_available_cars}")

# Function to update (Question 03)     <------ NEW Question 03

# Editing Name                    <------ NEW Question 03
def editing_name(nname,code_up):  
  bookings[code_up]["name"] = nname

# Editing Start date               <------ NEW Question 03
def editing_sd(nsd,code_up):
  is_valid, msg = validate_date(nsd)
  if not is_valid:
    print(msg)
    return
  n_start_date = datetime.datetime.strptime(nsd, "%Y-%m-%d").date()
  n_end_date = bookings[code_up]["end_date"]
  n_count_days = n_end_date - n_start_date
  n_count_days = n_count_days.days
  if n_start_date > n_end_date:
    print("Error!")
    return
  bookings[code_up]["start_date"] = n_start_date
  bookings[code_up]["days"] = n_count_days
  print ("Start date updated!")


# Editing End date                          <------ NEW Question 03
def editing_ed(ned,code_up):
  is_valid, msg = validate_date(ned)
  if not is_valid:
    print(msg)
    return
  ne_end_date = datetime.datetime.strptime(ned, "%Y-%m-%d").date()
  ne_start_date = bookings[code_up]["start_date"]
  ne_count_days = ne_end_date - ne_start_date
  ne_count_days = ne_count_days.days
  if ne_start_date > ne_end_date:
    print("Error!")
    return
  bookings[code_up]["end_date"] = ne_end_date
  bookings[code_up]["days"] = ne_count_days
  print ("End date updated!")
  

# Editing                                       <------ NEW Question 03
def editing(code_up):
  cmd1 = input ("update name (Y/N): ")
  if cmd1.lower() == "n":
    pass
  elif cmd1.lower() == "y":
    nname = input("Please enter your new name: ")
    editing_name(nname,code_up)
  else:
    print("not valid")
  cmd2 = input ("update start date (Y/N): ")  
  if cmd2.lower() == "n":
    pass
  elif cmd2.lower() == "y":
    nsd = input("Please enter your new start date: ")
    editing_sd(nsd,code_up)
  else:
    print("not valid")
  cmd3 = input ("update end date (Y/N): ")
  if cmd3.lower() == "n":
    pass
  elif cmd3.lower() == "y":
    ned = input("Please enter your end date: ")
    editing_ed(ned,code_up)
  else:
    print("not valid")

# Update                                      <------ NEW Question 03
def update_booking(code_up):
  if code_up.isdigit():
    code_up = int(code_up)
    if code_up in bookings:
        editing(code_up)  
    else:
        print("not found!")
  else: 
    print("Error: you have to enter a code number")


# Function to sort (Question 04)     <------ NEW Question 04

def sorting():
  a = []
  b = []

  for key, value in bookings.items():
      a.append(value)

  for i in range(len(a)):
      b.append(a[i]["start_date"])
  
  
  ans = input("sorting bye new start date to old date: Y or old start date to new: N (Y/N): ")

  if ans.lower() == "n":
    b.sort()
  elif ans.lower() == "y":
    b.sort(reverse=True)
  else:
    print("not valid")
    return

  for i in range(len(b)):  
      for code, booking in bookings.items():
          if booking['start_date'] == b[i]:
              print(f"code => {code} , start date => {booking['start_date']} ,  end date => {booking['end_date']} , rent duration => {booking['days']} days")
  

# ----------------Main----------------
while True:
  command = input("Enter your option: ")
  if command == "help":
    help()
  elif command == "booking":
    booking()
  elif command == "display":
    display()
  elif command == "search":
    search()
  elif command == "cancel":
    code_del = int(input("enter your code: "))
    cancel(code_del)
  elif command == "details":
    details()
  elif command == "update":             #            <------ NEW Question 03
    code_up = input("enter the code that you want to updat: ")
    update_booking(code_up)
  elif command == "sort":                #          <----- NEW Question 04
    sorting()                            
  elif command == "exit":
    break
  elif command == "":
    continue
  else:
    print("command not found!")