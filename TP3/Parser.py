class Parser:

    def __init__(self):
        self._file = None

    def read_file(self, name_file):
        self._file = open(name_file, "rt")

        credentials = self._file.read()
        self._file.close()

        return credentials

    def write_file(self, name_file, credentials):
        _varToReturn = None
        self._file = open(name_file, "wt")

        if self._file.write(credentials) > 0:
            _varToReturn = 1
        else:
            _varToReturn = 0

        self._file.close()

        return _varToReturn


