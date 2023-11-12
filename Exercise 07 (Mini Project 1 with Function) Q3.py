# Exit completely
def exit_program():
    import sys
    print("-----------------bye-------------------")
    print(".... Thank you to choose my program ....")
    sys.exit(0)

# HELP : Displays this help text
def help():
    help_text = """
      Tasks:
      - help: Displays this help text.
      - add: Adds a new task on the list.
      - set: Marks a task as done and record the tasktime.
      - edit: Edits the name, the start time or the end time of an existing task
      - remove: Removes a Task from the list.
      - search: Searches for a task by name.
      - display: Displays all completed tasks.
      - details: Displaye all tasks by details. The number of completed and uncompleted tasks, duration of any tasks and total duration. 
      - exit: Exits the program.
      """
    print(help_text) 
    return

# ADD : Adds a new task on the list  
def add(name):
    if name not in tasks_names:
        tasks_names.append(name)
        tasks_statuses.append(False)
        tasks_durations_hours.append(None)
        tasks_durations_minutes.append(None)
        start_time_hour.append(None)
        end_time_hour.append(None)
        start_time_minutes.append(None)
        end_time_minutes.append(None)

        print("--- added! ---")
    else:
        print(f"--- {name}:already exists! ---") 
    return

# REMOVE : Removes a Task from the list
def remove(name):
    if name in tasks_names:
      ind = tasks_names.index(name)
      tasks_names.pop(ind)
      tasks_durations_hours.pop(ind)
      tasks_durations_minutes.pop(ind)
      tasks_statuses.pop(ind)
      print("--- removed! ---")
    else:
      print(f"--- {name} => not found! ---") 
    return

# SEARCH : Searches for a task by name
def search(name):
    if name in tasks_names:
      ind = tasks_names.index(name)
      if tasks_durations_hours[ind] != None:
        print(f"{tasks_names[ind]} ==> Statuse: completed, Duration time: Duration time: {tasks_durations_hours[ind]} hours and {tasks_durations_minutes} minutes")
      else:
        print(f"{tasks_names[ind]} ==> Statuse: uncompleted, Duration time: 0")
    else:
      print(f"{name} => --- not found! ---") 
    return

# SET : Marks a task as done and record the tasktime
def set(name):
    if name in tasks_names :
      inx = tasks_names.index(name)
      if not tasks_statuses[inx]:
        f = False
        start_time = input("Start time: in 24 hour format (hh:mm) or x to exit:  ")
        while ((not f) and (start_time.lower() != "x")):
          st_h = start_time[:2]
          st_m = start_time[3:]
          if len(start_time) != 5:
            print(">>> Error: Please enter Start time in 24 hour format (hh:mm)")
            start_time = input("Start time: in 24 hour format (hh:mm) or x to exit:  ")
          elif start_time[2:3] != ":":
            print(">>> Error: Please enter : between hh and mm)")
            start_time = input("Start time: in 24 hour format (hh:mm) or x to exit:  ")
          elif not st_h.isdigit():
            print(">>> Error: Please enter Start time without Alphabet ")
            start_time = input("Start time: in 24 hour format (hh:mm) or x to exit:  ")
          elif not st_m.isdigit():
            print(">>> Error: Please enter Start time without Alphabet ")
            start_time = input("Start time: in 24 hour format (hh:mm) or x to exit:  ")
          elif int(st_h) > 23:
            print(">>> Error: hh must be between 0 and 23: ")
            start_time = input("Start time: in 24 hour format (hh:mm) or x to exit:  ")
          elif int(st_m) > 59:
            print(">>> Error: mm must be between 0 and 59: ")
            start_time = input("Start time: in 24 hour format (hh:mm) or x to exit:  ")
          else:
            f = True
        
        end_time = ""
        if start_time.lower() == "x":      
          h = True
        else:
          end_time = input("End time: in 24 hour format (hh:mm) or x to exit:  ") 
          h = False
        
        if end_time.lower() != "x":
          while (not h):
            et_h = end_time[:2]
            et_m = end_time[3:]
            if len(end_time) != 5:
              print(">>> Error: Please enter End time in 24 hour format (hh:mm)")
              end_time = input("End time: in 24 hour format (hh:mm) or x to exit:  ")
            elif end_time[2:3] != ":":
              print(">>> Error: Please enter : between hh and mm)")
              end_time = input("End time: in 24 hour format (hh:mm) or x to exit:  ")
            elif not et_h.isdigit():
              print(">>> Error: Please enter End time without Alphabet ")
              end_time = input("End time: in 24 hour format (hh:mm) or x to exit:  ")
            elif not et_m.isdigit():
              print(">>> Error: Please enter End time without Alphabet ")
              end_time = input("End time: in 24 hour format (hh:mm) or x to exit:  ")
            elif int(et_h) > 23:
              print(">>> Error: hh must be between 0 and 23: ")
              end_time = input("End time: in 24 hour format (hh:mm) or x to exit:  ")
            elif int(et_m) > 59:
              print(">>> Error: mm must be between 0 and 59: ")
              end_time = input("End time: in 24 hour format (hh:mm) or x to exit:  ")
            else:
              h = True
          
            st_h = int(st_h)
            st_m = int(st_m)
            et_h = int(et_h)
            et_m = int(et_m)
                  
            if (et_m < st_m):
              d_h = et_h - st_h - 1
              d_m = et_m + 60 - st_m
            else:
              d_h = et_h - st_h 
              d_m = et_m - st_m

            if d_h < 0 or d_m < 0:
              print(">>> Error: The End time must be greater than The Start time")
              print("--- not saved! ---")
            elif d_h == 0 and d_m == 0:
              print(">>> Error: The End time must not be equal to Start time")
              print("--- not saved! ---")         
            else:
              ind = tasks_names.index(name)
              tasks_durations_hours[ind] = d_h
              tasks_durations_minutes[ind] = d_m
              tasks_statuses[ind] = True
              start_time_hour[ind] = st_h   
              start_time_minutes[ind] = st_m
              end_time_hour[ind] = et_h
              end_time_minutes[ind] = et_m
              print("--- saved! ---")
      else:
        print(f"--- {name} => already exists! ---")  
    else:
      print(f"--- {name} => not found! ---") 
    return

# DETAILS : Displaye all tasks by details. The number of completed and uncompleted tasks, duration of any tasks and total duration
def details():
    print("------------------------------------------------------------------------------------------------------------")
    print(f"There is {tasks_statuses.count(False)} uncompleted Tasks")
    print(f"There is {len(tasks_statuses) - tasks_statuses.count(False)} completed Tasks")
    print("------------------------------------------------------------------------------------------------------------")

    t_tdh = 0
    t_tdm = 0

    if len(tasks_names) == 0:
      print("--- Empty! ---")
    for i in range(len(tasks_names)):
      if tasks_statuses[i]:
        sth1 = start_time_hour[i]
        stm1 = start_time_minutes[i]
        eth1 = end_time_hour[i]
        etm1 = end_time_minutes[i]
        tdh1 = tasks_durations_hours[i]
        tdm1 = tasks_durations_minutes[i]
        t_tdh = tdh1 + t_tdh
        t_tdm = tdm1 + t_tdm

        print("------------------------------------------------------------------------------------------------------------")
        print(f"Task {i+1}) {tasks_names[i]} ==> Statuse: completed, Start: {sth1}:{stm1} , End: {eth1}:{etm1} , Duration time: {tdh1} hours and {tdm1} minutes")
        print("------------------------------------------------------------------------------------------------------------")      
      else:
        print("------------------------------------------------------------------------------------------------------------")
        print(f"Task {i+1}) {tasks_names[i]} ==> Statuse: uncompleted , Duration time: 0")
        print("------------------------------------------------------------------------------------------------------------")
    total_tdm = t_tdm - ((t_tdm//60)*60)
    total_tdh = t_tdh + (t_tdm//60)
    print("------------------------------------------------------------------------------------------------------------")
    print (f"Duration of All completed Tasks: {total_tdh} hours and {total_tdm} minutes")
    print("------------------------------------------------------------------------------------------------------------")
    return

# DISPLAY : Displays all completed tasks
def display():
    a = tasks_statuses.count(False)
    if len(tasks_names) == 0:
       print("------------------------------------------------------------------------------------------------------------")
       print("-------------- Empty! ---------------")
       print("------------------------------------------------------------------------------------------------------------")
    elif  a == len(tasks_names):
       print("------------------------------------------------------------------------------------------------------------")
       print(f"--------- There is {a} uncompleted Tasks ---------")
       print("------------------------------------------------------------------------------------------------------------") 
    for i in range(len(tasks_names)):
      if tasks_statuses[i] != False:
        tdh = tasks_durations_hours[i]
        tdm = tasks_durations_minutes[i]
        print("------------------------------------------------------------------------------------------------------------")
        print(f"{tasks_names[i]} ==> Statuse: completed, Duration time: {tdh} hours and {tdm} minutes") 
        print("------------------------------------------------------------------------------------------------------------")
    return

# EDIT : Edits the name, the start time or the end time of an existing task
def edit():
  if answer.lower() == "edit":
    print("Please select what you want to edit:  ")
    name1 = input("press n for name, s for start time, e for end time or x for exit:  ")
    if name1.lower() == "x":
       exit_program()
    elif name1.lower() == "n":
      old_name = input("The Task you want to edit:  ") 
      if old_name in tasks_names:
        new_name = input("new Task:  ") 
        if new_name not in tasks_names: 
          ind = tasks_names.index(old_name) 
          tasks_names[ind] = new_name 
          print("--- edited! ---")
        else:
          print(f"--- {new_name} : already exists! ---")
      else:
        print(f"--- {old_name}: not found! ---")
    elif name1.lower() == "s":
      name2 = input("The Task:  ")
      if name2 in tasks_names:
        j = tasks_names.index(name2) 
        if tasks_statuses[j] == False:
           print("--- This Task ist not completed! First set it ---")
        else:   
          f = False
          start_time = input("Start time: in 24 hour format (hh:mm) or x to exit:  ")
          while ((not f) and (start_time.lower() != "x")):
            st_h = start_time[:2]
            st_m = start_time[3:]
            if len(start_time) != 5:
              print(">>> Error: Please enter Start time in 24 hour format (hh:mm)")
              start_time = input("Start time: in 24 hour format (hh:mm) or x to exit:  ")
            elif start_time[2:3] != ":":
              print(">>> Error: Please enter : between hh and mm)")
              start_time = input("Start time: in 24 hour format (hh:mm) or x to exit:  ")
            elif not st_h.isdigit():
              print(">>> Error: Please enter Start time without Alphabet ")
              start_time = input("Start time: in 24 hour format (hh:mm) or x to exit:  ")
            elif not st_m.isdigit():
              print(">>> Error: Please enter Start time without Alphabet ")
              start_time = input("Start time: in 24 hour format (hh:mm) or x to exit:  ")
            elif int(st_h) > 23:
              print(">>> Error: hh must be between 0 and 23: ")
              start_time = input("Start time: in 24 hour format (hh:mm) or x to exit:  ")
            elif int(st_m) > 59:
              print(">>> Error: mm must be between 0 and 59: ")
              start_time = input("Start time: in 24 hour format (hh:mm) or x to exit:  ")
            else:
              f = True
         
          st_h = int(st_h)
          st_m = int(st_m)      
          ind = tasks_names.index(name2) 
          et_h = end_time_hour[ind]
          et_m = end_time_minutes[ind]

          if (et_m < st_m):
            d_h = et_h - st_h - 1
            d_m = et_m + 60 - st_m
          else:
            d_h = et_h - st_h 
            d_m = et_m - st_m
      
          if d_h < 0 or d_m < 0:
            print(">>> Error: The End time must be greater than The Start time")
            print("--- not edited! ---")
          elif d_h == 0 and d_m == 0:
            ind = tasks_names.index(name2)
            tasks_statuses[ind] = False 
            print(f"** The Start and End time are equal, than Task {tasks_names[ind]} changed to uncompleted **") 
            print("--- edited! ---")      
          else:
            ind = tasks_names.index(name2)
            start_time_hour[ind] = st_h   
            start_time_minutes[ind] = st_m
            tasks_durations_hours[ind] = d_h
            tasks_durations_minutes[ind] = d_m
            print("--- edited! ---")
      else:
        print(f"--- {name2} => not found! ---")  

    elif name1.lower() == "e":
      name3 = input("The Task:  ")
      if name3 in tasks_names:
        k = tasks_names.index(name3) 
        if tasks_statuses[k] == False:
           print("--- This Task ist not completed! First set it ---")
        else: 
          h = False
          end_time = input("End time: in 24 hour format (hh:mm) or x to exit:  ")
          while ((not h) and (end_time.lower() != "x")):
            et_h = end_time[:2]
            et_m = end_time[3:]
            if len(end_time) != 5:
              print(">>> Error: Please enter End time in 24 hour format (hh:mm)")
              end_time = input("End time: in 24 hour format (hh:mm) or x to exit:  ")
            elif end_time[2:3] != ":":
              print(">>> Error: Please enter : between hh and mm)")
              end_time = input("End time: in 24 hour format (hh:mm) or x to exit:  ")
            elif not et_h.isdigit():
              print(">>> Error: Please enter End time without Alphabet ")
              end_time = input("End time: in 24 hour format (hh:mm) or x to exit:  ")
            elif not et_m.isdigit():
              print(">>> Error: Please enter End time without Alphabet ")
              end_time = input("End time: in 24 hour format (hh:mm) or x to exit:  ")
            elif int(et_h) > 23:
              print(">>> Error: hh must be between 0 and 23: ")
              end_time = input("End time: in 24 hour format (hh:mm) or x to exit:  ")
            elif int(et_m) > 59:
              print(">>> Error: mm must be between 0 and 59: ")
              end_time = input("End time: in 24 hour format (hh:mm) or x to exit:  ")
            else:
              h = True

          et_h = int(et_h)
          et_m = int(et_m)      
          ind = tasks_names.index(name3) 
          st_h = start_time_hour[ind]
          st_m = start_time_minutes[ind]
               
          if (et_m < st_m):
            d_h = et_h - st_h - 1
            d_m = et_m + 60 - st_m
          else:
            d_h = et_h - st_h 
            d_m = et_m - st_m
      
          if d_h < 0 or d_m < 0:
            print(">>> Error: The End time must be greater than The Start time")
            print("--- not edited! ---")
          elif d_h == 0 and d_m == 0:
            ind = tasks_names.index(name3)
            tasks_statuses[ind] = False 
            print(f"** The Start and End time are equal, than Task {tasks_names[ind]} changed to uncompleted **")
            print("--- edited ---")      
          else:
            ind = tasks_names.index(name3)
            end_time_hour[ind] = et_h   
            end_time_minutes[ind] = et_m
            tasks_durations_hours[ind] = d_h
            tasks_durations_minutes[ind] = d_m
            print("--- edited! ---")
      else:
        print(f"--- {name3} => not found! ---")       

    else:
      print(f"--- {name1} => command not found! ---")    
    
# -----------------------------main----------------------------
tasks_names = []
tasks_durations_hours = []
tasks_durations_minutes = []
tasks_statuses = []
start_time_hour = []
end_time_hour = []
start_time_minutes = []
end_time_minutes = []

for i in range(200):
  answer = input("Please select: (help, add, set, edit, remove, search, display, details, exit: )  ")
  if answer.lower() == "help":
    help()  
  elif answer.lower() == "add":
    name = input("Enter your new task:  ")
    add(name) 
  elif answer.lower() == "remove":
    name = input("Task:  ")
    remove(name)  
  elif answer.lower() == "search":
    name = input("Task:  ")
    search(name)
  elif answer.lower() == "set":
    name = input("Task:  ")
    set(name)
  elif answer.lower() == "details":
    details()
  elif answer.lower() == "display":
    display()
  elif answer.lower() == "edit":
    edit()
  elif answer == "":
    continue
  elif answer.lower() == "exit":
    break
  else:
    print(f"--- {answer} => command not found! ---")