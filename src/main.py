import customtkinter as ctk
from customtkinter import filedialog
from pypdf import PdfMerger

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

file_list = []
file_types = [('PDF files', '*.pdf')]
default_extension = '*.pdf'

window = ctk.CTk()
window.title('PDF merger')
window.geometry('400x500')
window.resizable(False, False)


def import_file() -> None:
    file_path = filedialog.askopenfilename(filetypes=file_types)
    if file_path == '':
        return

    print('Import ', file_path)
    add_file(file_path)


def merge_files() -> None:
    if len(file_list) <= 0:
        print('No files to merge')
        return

    file_path = filedialog.asksaveasfilename(filetypes=file_types, defaultextension=default_extension)
    if file_path == '':
        return

    print('Export ', file_path)
    merger = PdfMerger()

    for file in file_list:
        merger.append(file)

    merger.write(file_path)
    merger.close()
    clear_files()


import_button = ctk.CTkButton(window, text='Import', width=250, height=40, command=import_file)
import_button.pack(pady=10)
frame = ctk.CTkFrame(window)
frame.pack(padx=10, fill='both', expand=1)

merge_button = ctk.CTkButton(window, text='Merge', width=250, height=40, command=merge_files)
merge_button.pack(pady=10)


def add_label(text: str) -> None:
    entry_frame = ctk.CTkFrame(frame)
    entry_frame.pack(padx=5, pady=2, fill='x')

    name_label = ctk.CTkLabel(entry_frame, text=text, wraplength=300, justify='left', anchor='w')
    name_label.pack(padx=10, pady=5, side='left', fill='x', expand=1)

    remove_button = ctk.CTkButton(entry_frame, text='-', width=40, command=lambda: remove_entry(entry_frame))
    remove_button.pack(padx=5, side='left')


def remove_entry(entry) -> None:
    index = frame.winfo_children().index(entry)
    remove_file(index)


def add_file(file_path: str):
    file_list.append(file_path)
    add_label(file_path)


def remove_file(index: int) -> None:
    file_list.pop(index)
    child = frame.winfo_children().pop(index)
    child.destroy()


def clear_files():
    file_list.clear()
    for child in frame.winfo_children():
        child.destroy()


window.mainloop()
