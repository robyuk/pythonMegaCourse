import PySimpleGUI as Gui
from pathlib import Path

import zipfile


def make_archive(file_paths, dest_filepath):
    try:
        with zipfile.ZipFile(dest_filepath, "w") as archive:
            for filepath in file_paths:
                filepath = Path(filepath)
                archive.write(filepath, arcname=filepath.name)
    except FileNotFoundError:
        print("FileNotFoundError")
        return FileNotFoundError
    return 0


FilesLabel = Gui.Text("Files to zip")
FilesBox = Gui.InputText(tooltip="Click browse button to select the files to zip", key="files")
FilesButton = Gui.FilesBrowse("Browse")
FolderLabel = Gui.Text("Destination folder")
FolderBox = Gui.InputText(tooltip="Click browse button to select the destination folder", key="folder")
FolderButton = Gui.FolderBrowse("Browse")
ZipLabel = Gui.Text("Archive file name")
ZipBox = Gui.InputText(default_text="compressed.zip", key="zipfile", tooltip="Enter zip file name")
ZipitButton = Gui.Button("Zip it!")
MsgLabel = Gui.Text(key="message")
message = ""

layout = [[FilesLabel, FilesBox, FilesButton],
          [FolderLabel, FolderBox, FolderButton],
          [ZipLabel, ZipBox, ZipitButton],
          [MsgLabel]]

window = Gui.Window('File Zipper', layout=layout)

while True:
    event, values = window.read()
    # print(event, values)

    match event:
        case "Zip it!":
            folder = values["folder"]
            filepaths = values["files"].split(";")
            zip_filename = values["zipfile"]

            if filepaths == [''] or folder == "" or zip_filename == "":
                message = "Please select files to zip, the destination folder, and enter a zip file name"
                print(message)
            #    print(f"|{filepaths}|")
            elif make_archive(filepaths, Path(folder, zip_filename)) == 0:
                message = "Zip successful"
            else:
                message = "A file to zip or the destination folder was not found"

        case Gui.WINDOW_CLOSED:
            break

    window["message"].update(value=message)

window.close()
