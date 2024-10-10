from logging import raiseExceptions


class User:
    def __init__(self, first_name, last_name):
        self.validation(first_name)
        self.validation(last_name)
        self._first_name = first_name
        self._last_name = last_name


    def _user_to_string(self):
        return f"{self._first_name}, {self._last_name}"


    def validation(self, name):
        for char in name:
            if char.isnumeric():
                raise ValueError("Name incorrect")
