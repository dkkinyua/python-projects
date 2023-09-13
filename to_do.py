import datetime as dt
import time as t

# This class adds a task to the task list
class Add:
    def __init__(self, a, b):
        self.task = a
        self.time = b
    
    def add_tasks(self, task_input, time_input):
        tasks[task_input] = time_input

# This class adds a priority task to the priority task list
class Priority:
    def __init__(self, a):
        self.task = a
        
    def prioritize_task(self, priority_task):
        if priority_task in tasks:
            priority_tasks[priority_task] = tasks[priority_task]
            del tasks[priority_task]


# This class removes a task to the task list      
class Remove:
    def __init__(self, a):
        self.task = a
        
    def remove_task(self, remove_task):
        del tasks[remove_task]


# This class adds a finished task to the finished tasks      
class Finish:
    def __init__(self, a):
        self.task = a
        
    def finished_task(self, finished_task):
        if finished_task in tasks:
            finished_tasks[finished_task] = tasks[finished_task]
            del tasks[finished_task]



tasks = {}
priority_tasks = {}
finished_tasks = {}
    
    
# The main program
def main_program():
    print("Welcome to the Python To-Do app!")
    program_done = False

    while not program_done:
        menu_input = input("Would you like to:\n1.Add tasks\n2.Remove tasks\n3.Prioritize tasks\n4.Remove Finished tasks\n5.Show remaining tasks\n6.Show finished tasks\n7.Show prioritized tasks\n8.Exit the program entirely.:\n")
        
        #This if block check user input and acts according to the instructions provided
        if menu_input == "1":
            task_input = input("Add a task: ")
            time_input = input("Add the time to start task: ")
            add = Add(task_input, time_input)
            add_task = add.add_tasks(task_input, time_input)
            other_task = input("Would you like to add another task: ")
            if other_task == "y":
                    add = Add(task_input, time_input)
                    add_task = add.add_tasks(task_input, time_input)
            else:
                continue
            
        elif menu_input == "2":
            remove_task = input("Which task would you like to remove from the to-do list: ")
            remove = Remove(remove_task)
            remove_task = remove.remove_task(remove_task)
            
        
        elif menu_input == "3":
            priority_task = input("Which task would you like to prioritize: ")
            priority = Priority(priority_task)
            prioritize_task = priority.prioritize_task(priority_task)
        
        elif menu_input == "4":
            finished_task = input("Which task have you finished: ")
            finish = Finish(finished_task)
            finished_task = finish.finished_task(finished_task)
            
            
        elif menu_input == "5":
            print(tasks)
            
        elif menu_input == "6":
            print(finished_tasks)
            
        elif menu_input == "7":
            print(priority_tasks)
            
        elif menu_input == "8":
            program_done = True
            
            
if __name__ == "__main__":
    main_program()
