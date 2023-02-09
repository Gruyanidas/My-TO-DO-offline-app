from moduls import functionsFromTO_DO
import PySimpleGUI as sg
import time

sg.theme("DarkTeal11")
clock = sg.Text('', key='clock')
label = sg.Text(" Type in a to-do: ")  # tekst label na window, mora da bude string
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functionsFromTO_DO.get_to_dos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label], [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))  # layout ocekuje litu, kada su u jednoj listi zajedno onda su istom redu
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)  # ADD
    print(values)  # recnik todo:input
    match event:
        case "Add":
            todos = functionsFromTO_DO.get_to_dos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functionsFromTO_DO.write_to_dos(todos)
            window['todos'].update(todos)
            window['todo'].update(value='')
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]  # index error se javlja
                new_todo = values['todo']

                to_dos = functionsFromTO_DO.get_to_dos()
                index = to_dos.index(todo_to_edit)
                to_dos[index] = new_todo

                functionsFromTO_DO.write_to_dos(to_dos)
                window['todos'].update(values=to_dos)
            except IndexError:
                sg.popup("Please select an item first!", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functionsFromTO_DO.get_to_dos()
                todos.remove(todo_to_complete)
                functionsFromTO_DO.write_to_dos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first!", font=("Helvetica", 20))
        case "Exit":
            break
        case "todos":
            try:
                window['todo'].update(value=values['todos'][0])
            except IndexError:
                sg.popup("Please select an item for further actions!", font=("Helvetica", 20))
        case sg.WIN_CLOSED:
            break
window.close()
