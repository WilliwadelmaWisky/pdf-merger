from customtkinter import CTk, CTkButton, CTkFrame
from src.component.File import File


class MainWindow(CTk):
    """
    Main window of the application
    """

    def __init__(self, on_import, on_generate, on_remove_entry):
        """
        Constructor
        :param on_import: a callback to import-button click (No arguments)
        :param on_generate: a callback to generate-button click (No arguments)
        :param on_remove_entry: a callback to file-remove-button click (args: int)
        """
        CTk.__init__(self)
        self.title('PDF merger')
        self.geometry('400x500')
        self.resizable(False, False)
        self.on_remove_entry = on_remove_entry

        CTkButton(self, 200, 35, text='Import', command=on_import).pack(pady=10)

        self.filebox = CTkFrame(self)
        self.filebox.pack(padx=10, fill='both', expand=1)

        CTkButton(self, 200, 35, text='Generate', command=on_generate).pack(pady=10)

    def add_file(self, text: str, pages: int) -> None:
        """
        Add file to window
        :param text: name of the file (string)
        :param pages: total amount of pages (int)
        :return:
        """
        def remove():
            index = self.filebox.winfo_children().index(file)
            self.on_remove_entry(index)

        file = File(self.filebox, file_name=text, pages=pages, on_remove=remove)
        file.pack(padx=5, pady=2, fill='x')

    def remove_file(self, index: int) -> None:
        """
        Remove a file from window
        :param index: index of the file
        :return: None
        """
        child = self.filebox.winfo_children().pop(index)
        child.destroy()

    def clear_files(self) -> None:
        """
        Clear all files from window
        :return: None
        """
        for child in self.filebox.winfo_children():
            child.destroy()

    def get_file(self, index: int) -> File:
        """
        Get a file from window
        :param index: index of the file
        :return: file (File)
        """
        return self.filebox.winfo_children()[index]
