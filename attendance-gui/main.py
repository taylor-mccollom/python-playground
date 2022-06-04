
import PySimpleGUI as sg

student_list = ['Phteven', 'Gregg', 'Ally', 'George']

sg.theme('DarkAmber')

# Window contents
layout = [[sg.Text('Attendance Roster')]]
for student in student_list:
    selection = [sg.Text(student), sg.Button('Present', key=student)]
    layout.append(selection)
layout_output = [sg.Output(size=(20, 10))]
layout.append(layout_output)
layout_last_row = [sg.Button('Exit')]
layout.append(layout_last_row)

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    print(event)

window.close()