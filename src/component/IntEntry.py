from customtkinter import CTkEntry, StringVar


class IntEntry(CTkEntry):
    def __init__(self, root, placeholder: str, value: int, min_value: int = 0, max_value: int = 1, width=40, height=28):
        CTkEntry.__init__(self, root, width, height, placeholder_text=placeholder, textvariable=StringVar())
        self.value = value
        self.min_value = min_value
        self.max_value = max_value

        self._textvariable.trace_add('write', self.callback)
        self._textvariable.set(str(self.value))

    def get_value(self) -> int:
        return self.value

    def callback(self, *args) -> None:
        text = self._textvariable.get()
        if text == '':
            self.value = self.min_value
            return

        if str.isdigit(text):
            new_value = int(text)

            if new_value > self.max_value:
                new_value = self.max_value
                self.value = new_value
                self._textvariable.set(str(self.value))
                return

            if new_value < self.min_value:
                new_value = self.min_value
                self.value = new_value
                self._textvariable.set(str(self.value))
                return

            self.value = new_value
            return

        print('Non-digit: ', text, ', validating...')
        self._textvariable.set(str(self.value))
