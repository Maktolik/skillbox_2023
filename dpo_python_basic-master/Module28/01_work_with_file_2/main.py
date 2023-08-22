class File:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
        except IOError:
            self.file = open(self.filename, 'w+')
        return self.file

    def __exit__(self, exp_type, exp_value, exp_tr):
        self.file.close()
        if exp_type and issubclass(exp_type, IOError):
            return True


with File('example.txt', 'a+') as file:
    file.write('example!\n')