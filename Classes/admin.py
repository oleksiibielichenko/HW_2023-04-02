from user import User


class Admin (User):
    def __init__(self, name, password, age, card, isAdmin):
        super().__init__(name, password, age, card)
        self._isAdmin = isAdmin
