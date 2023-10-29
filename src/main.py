from customtkinter import set_appearance_mode, set_default_color_theme, filedialog
from pypdf import PdfMerger, PdfReader
from pathlib import Path
from src.component.MainWindow import MainWindow

set_appearance_mode('dark')
set_default_color_theme('dark-blue')

file_list = []
file_types = [('PDF files', '*.pdf')]
default_extension = '*.pdf'


def import_file() -> None:
    """
    Imports a file. Asks for a path through a filemanager
    :return: None
    """
    file_path = filedialog.askopenfilename(filetypes=file_types)
    if file_path == '':
        return

    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        pages = len(reader.pages)

    if pages <= 0:
        print('No pages found!')
        return

    add_file(file_path, pages)


def merge_files() -> None:
    """
    Merges all the observed pdf files to a new file. A new filepath is asked through a filemanager.
    Merging fails if there are no files to merge. If a file pages are not set correctly file cannot be merged,
    instead it is skipped so the result pdf will not contain the file
    :return: None
    """
    if len(file_list) <= 0:
        print('No files to merge')
        return

    file_path = filedialog.asksaveasfilename(filetypes=file_types, defaultextension=default_extension)
    if file_path == '':
        return

    merger = PdfMerger()
    for i in range(0, len(file_list)):
        pages = window.get_file(i).get_pages()
        if pages[0] >= pages[1]:
            print('Failed to append: ', file_list[i])
            continue

        merger.append(file_list[i], pages=pages)

    merger.write(file_path)
    merger.close()
    clear_files()


def add_file(file_path: str, pages: int) -> None:
    """
    Add a file to a list and to a window
    :param file_path: Path of the file (string)
    :param pages: Total amount of pages in file (int)
    :return: None
    """
    file_list.append(file_path)
    file_name = Path(file_path).name
    window.add_file(file_name, pages)


def remove_file(index: int) -> None:
    """
    Remove a file from a list and from a window
    :param index: File index to remove
    :return: None
    """
    file_list.pop(index)
    window.remove_file(index)


def clear_files() -> None:
    """
    Clear all files from a list and from a window
    :return: None
    """
    file_list.clear()
    window.clear_files()


window = MainWindow(on_import=import_file, on_generate=merge_files, on_remove_entry=remove_file)
window.mainloop()
