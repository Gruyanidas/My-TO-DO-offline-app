from moduls import functionsFromTO_DO
import PySimpleGUI as sg

label = sg.Text(" Type in a to-do: ")  # tekst label na window, mora da bude string
input_box = sg.InputText(tooltip="Enter to-do")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button]])  # layout ocekuje litu, kada su u jednoj listi zajedno onda su istom redu u app
window.read()  # display a window on the screen
window.close()
