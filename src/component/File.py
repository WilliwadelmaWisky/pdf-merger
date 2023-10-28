from customtkinter import CTkFrame, CTkLabel, CTkButton
from src.component.IntEntry import IntEntry


class File(CTkFrame):
    def __init__(self, root, file_name: str, pages: int, on_remove):
        CTkFrame.__init__(self, root)
        name_label = CTkLabel(self, text=file_name, wraplength=200, justify='left', anchor='w')
        name_label.pack(padx=10, pady=5, side='left', fill='x', expand=1)

        self.start_entry = IntEntry(self, 'start...', value=0, max_value=pages)
        self.start_entry.pack(side='left', padx=2)
        self.end_entry = IntEntry(self, 'end...', value=pages, max_value=pages)
        self.end_entry.pack(side='left', padx=2)

        remove_button = CTkButton(self, text='-', width=40, command=on_remove)
        remove_button.pack(padx=5, side='left')

    def get_pages(self) -> (int, int):
        return self.start_entry.get_value(), self.end_entry.get_value()
