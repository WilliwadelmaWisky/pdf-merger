from customtkinter import CTkEntry, StringVar


class IntEntry(CTkEntry):
    """
    Whole-number entry widget
    """

    def __init__(self, root, placeholder: str, value: int, min_value: int = 0, max_value: int = 1,
                 width: int = 40, height: int = 28):
        """
        Constructor
        :param root: parent of the widget
        :param placeholder: placeholder of the entry
        :param value: default-value (int)
        :param min_value: min-value (int)
        :param max_value: max-value (int)
        :param width: width of the widget (int)
        :param height: height of the widget (int)
        """
        CTkEntry.__init__(self, root, width, height, placeholder_text=placeholder, textvariable=StringVar())
        self.value = value
        self.min_value = min_value
        self.max_value = max_value

        self._textvariable.trace_add('write', self.validate)
        self._textvariable.set(str(self.value))

    def get_value(self) -> int:
        """
        Get the value of the widget
        :return: value (int)
        """
        return self.value

    def validate(self, *args) -> None:
        """
        Validates input of the entry
        :param args: tuple of required arguments (var_name, index, mode)
        :return: None
        """
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
