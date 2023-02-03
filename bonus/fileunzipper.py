import PySimpleGUI as Gui
from pathlib import Path

import zipfile


def extract_archive(file_path, dest_folder):
    try:
        with zipfile.ZipFile(file_path, "r") as archive:
            archive.extractall(path=dest_folder)
    except FileNotFoundError:
        print("FileNotFoundError")
        return FileNotFoundError
    return 0


ZipLabel = Gui.Text("Archive file", justification='right')
ZipFileBox = Gui.InputText(tooltip="Click browse button to select the archive file to unzip", key="zipfile")
ZipFileButton = Gui.FileBrowse("Browse")
FolderLabel = Gui.Text("Destination folder")
FolderBox = Gui.InputText(tooltip="Click browse button to select the destination folder for the files", key="folder")
FolderButton = Gui.FolderBrowse("Browse")
ExtractButton = Gui.Button("Extract")
MsgLabel = Gui.Text(key="message")
message = ""

col1 = Gui.Column([[ZipLabel], [FolderLabel]])
col2 = Gui.Column([[ZipFileBox], [FolderBox]])
col3 = Gui.Column([[ZipFileButton], [FolderButton]])

layout = [[col1, col2, col3],
          [ExtractButton, MsgLabel]]

window = Gui.Window('File Unzipper', layout=layout)

while True:
    event, values = window.read()
    # print(event, values)

    match event:
        case "Extract":
            folder = values["folder"]
            zip_filename = values["zipfile"]

            if folder == "" or zip_filename == "":
                message = "Please archive to unzip, and the destination folder"
                print(message)
            #    print(f"|{filepaths}|")
            elif extract_archive(zip_filename, folder) == 0:
                message = "Extract successful"
            else:
                message = f"The archive file was not found: {zip_filename}"

        case Gui.WINDOW_CLOSED:
            break

    window["message"].update(value=message)

window.close()
