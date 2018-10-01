class Parser:

    def __init__(self):
        self._file = None

    def read_file(self, name_file):
        self._file = open(name_file, 'rt')

        credentials = self._file.read()
        self._file.close()

        return credentials

    def write_file(self, name_file, credentials):
        self._file = open(name_file, 'wt')

        self._file.write(credentials)
        self._file.close()
