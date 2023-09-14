"""
A SIMPLE TO-DO APP

"""

import datetime as dt

# This class adds a task to the task list
class Add:
    def __init__(self, a, b):
        self.task = a
        self.time = b
    
    def add_tasks(self, task_input, time_input):
        tasks[task_input] = time_input

    def due_date(self, task_input, time_input=None):
        if time_input is None:
            pass
        else:
            print("Due time for", task_input, "is", time_input)

    def show_time_left(self, time_input):
        now = dt.datetime.now()
        parsed_time = dt.datetime.strptime(time_input, "%H:%M")
        time_left = parsed_time - now
        return time_left


# This class adds a priority task to the priority task list
class Priority:
    def __init__(self, a):
        self.task = a

    def prioritize_task(self, priority_task):
        if priority_task in tasks:
            priority_tasks[priority_task] = tasks[priority_task]
            del tasks[priority_task]


# This class removes a task from the task list
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
        
        # This if block checks user input and acts according to the instructions provided
        if menu_input == "1":
            task_input = input("Add a task: ")
            time_input = input("Add the due time (HH:MM format, leave empty for no due time): ")
            add = Add(task_input, time_input)
            add_task = add.add_tasks(task_input, time_input)
            if time_input:
                add.due_date(task_input, time_input)
                time_left = add.show_time_left(time_input)
                print("Time left until due:", time_left)
            other_task = input("Would you like to add another task: ")
            if other_task == "y":
                task_input = input("Add a task: ")
                time_input = input("Add the due time (HH:MM format, leave empty for no due time): ")
                add = Add(task_input, time_input)
                add_task = add.add_tasks(task_input, time_input)
                if time_input:
                    add.due_date(task_input, time_input)
                    time_left = add.show_time_left(time_input)
                    print("Time left until due:", time_left)
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
            print("Remaining tasks:")
            for task, due_time in tasks.items():
                if due_time:
                    time_left = Add.show_time_left(due_time)
                    print(f"{task} (Due in {time_left})")
                else:
                    print(task)
        
        elif menu_input == "6":
            print("Finished tasks:", finished_tasks)
        
        elif menu_input == "7":
            print("Prioritized tasks:", priority_tasks)
        
        elif menu_input == "8":
            print("Thank you for using the to-do app, if you have any suggestions or ways of improving this, please do!")
            program_done = True


if __name__ == "__main__":
    main_program()
