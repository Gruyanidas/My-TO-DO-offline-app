from moduls.functionsFromTO_DO import get_to_dos, write_to_dos  # local modul
import time

now = time.strftime("%b, %d, %Y %H:%M:%S")
print("It is", now)
text = """ Program which provides simple TO_DO LIST """
while True:
    user_action = input("Type add, show, edit, complete or exit,\n"
                        "To complete all tasks - type delete: ")
    user_action = user_action.lower().strip()

    if user_action.startswith('add'):

        to_dos = get_to_dos()

        todo = user_action
        if todo == 'add':
            print("Enter a task name after typing 'add'")
        elif len(user_action) > 3:
            todo = user_action[3:]
            to_dos.append(todo + '\n')
        else:
            print("Please enter a to-do task on the list")

        write_to_dos(to_dos)

    elif user_action.startswith('show'):
        to_dos = get_to_dos()
        # new_todos = []
        # for item in to_dos: #ili comprehension new_todos = [new_item.replace('\n', '') for new_item in to_dos]
        #   new_item = item.replace('\n', '')
        #    new_todos.append(new_item)
        if not to_dos:
            print("Your to-do list is empty. Input some tasks.")
        else:
            print("Here is your personal list of stuff to do: ")
            for index, item in enumerate(to_dos):
                item = item.replace('\n', '')
                print(f"\t{index + 1}.{item.capitalize()}")

    elif user_action.startswith("edit"):
        try:
            to_dos = get_to_dos()

            if user_action == 'edit':
                print('After edit, please enter a number of a task...')
            elif len(user_action) >= 4:
                number = int(user_action[4:])
                number = number - 1
                new_todo = input("Enter the new task: ")
                to_dos[number] = new_todo + '\n'

                write_to_dos(to_dos)

        except ValueError or IndexError:
            print("Your command is not valid. Type show for checking task numbers!")
        continue

    elif user_action.startswith('complete'):
        try:
            to_dos = get_to_dos()
            number = int(user_action[8:])
            removed_task = to_dos.pop(number - 1)
            print(f"Nice! You completed task {number}. Keep it up!")
            if len(to_dos) == 1:
                print("\tWell done, 1 more left.")
            if len(to_dos) == 0:
                print("You completed all of them! Congrats!")
        except IndexError or ValueError:
            print("There is no task with such number or you forgot to input a number.\n"
                  "Check tasks with 'show' command.")
        continue

    elif user_action == 'delete':
        to_dos = get_to_dos()
        to_dos.clear()
        write_to_dos(to_dos)
    elif user_action == 'exit':
        break
    else:
        print("Invalid input! Please type add, show, edit, delete or exit.")
print("Thank you for using my software!")
