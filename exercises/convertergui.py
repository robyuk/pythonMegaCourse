import PySimpleGUI as Gui
from bonus.converters import convert

message = ""
FeetLabel = Gui.Text("Enter feet")
FeetBox = Gui.InputText(tooltip="Enter the number of feet", key="feet")
InchesLabel = Gui.Text("Enter inches")
InchesBox = Gui.InputText(tooltip="Enter the number of inches", key="inches")
ConvertButton = Gui.Button("Convert")
MessageLabel = Gui.Text(key="message")

layout = [[FeetLabel, FeetBox], [InchesLabel, InchesBox],[ConvertButton, MessageLabel]]

window = Gui.Window('Convert to meters', layout=layout)

while True:
    event, values = window.read()
    match event:
        case "Convert":
            # print(values)
            message = str(convert(values)) + "m"
            # print(message)
            window["message"].update(value=message)
        case Gui.WINDOW_CLOSED:
            break

window.close()