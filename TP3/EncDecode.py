import Cryptodome.Cipher.AES as AES
from Cryptodome.Random import get_random_bytes


class EncoDecode:
    def __init__(self):
        self._Key = None

    def setKey(self, key):
        self._Key=key
        print(self._Key)
        print(len(self._Key))
        value = get_random_bytes(32)
        print(value)
        self._aes = AES.new(self._Key, AES.MODE_CBC, value)

    def Encode(self, dataToEncode):
        encMsg = self._aes.encrypt(dataToEncode)

        return encMsg

    def Decode(self, dataToDecode):
        decMsg = self._aes.decrypt(dataToDecode)

        return decMsg

