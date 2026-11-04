class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name should be a string')
        if not value.strip():
            raise ValueError('name cannot be empty string')
        self._name = value

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError('email should be a string')
        if not value.strip():
            raise ValueError('email cannot be empty')
        self._email = value

    @property
    def address(self):
        return self._address
    @address.setter
    def address(self, value):
        if not isinstance(value, str):
            raise TypeError('address should be a string')
        if not value.strip():
            raise ValueError('address cannot be empty')
        self._address = value