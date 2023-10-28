from customtkinter import CTk, CTkButton, CTkFrame
from src.component.File import File


class MainWindow(CTk):
    def __init__(self, on_import, on_merge, on_clear, on_remove_entry):
        CTk.__init__(self)
        self.title('PDF merger')
        self.geometry('400x500')
        self.resizable(False, False)
        self.on_remove_entry = on_remove_entry

        CTkButton(self, 200, 35, text='Import', command=on_import).pack(pady=10)

        self.filebox = CTkFrame(self)
        self.filebox.pack(padx=10, fill='both', expand=1)

        CTkButton(self, 200, 35, text='Generate', command=on_merge).pack(pady=10)

    def add_file(self, text: str, pages: int) -> None:
        def remove():
            index = self.filebox.winfo_children().index(file)
            self.on_remove_entry(index)

        file = File(self.filebox, file_name=text, pages=pages, on_remove=remove)
        file.pack(padx=5, pady=2, fill='x')

    def remove_file(self, index: int) -> None:
        child = self.filebox.winfo_children().pop(index)
        child.destroy()

    def clear_files(self):
        for child in self.filebox.winfo_children():
            child.destroy()

    def get_file(self, index: int) -> File:
        return self.filebox.winfo_children()[index]
