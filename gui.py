from moduls import functionsFromTO_DO
import PySimpleGUI as sg

label = sg.Text(" Type in a to-do: ")  # tekst label na window, mora da bude string
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))  # layout ocekuje litu, kada su u jednoj listi zajedno onda su istom redu
while True:
    event, values = window.read()
    print(event)  # ADD
    print(values)  # recnik todo:input
    match event:
        case "Add":
            todos = functionsFromTO_DO.get_to_dos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functionsFromTO_DO.write_to_dos(todos)
        case sg.WIN_CLOSED:
            break
window.close()
