import Cryptodome.Cipher.AES as AES
import Cryptodome.Random as Random


class EncoDecode:
    def __init__(self):
        self._Key = None

    def setKey(self, key):
        self._Key=key
        value = Random.new().read(AES.block_size)
        self._aes = AES.new(self._Key, AES.MODE_CBC, value)

    def Encode(self, dataToEncode):
        encMsg = self._aes.encrypt(dataToEncode)

        return encMsg

    def Decode(self, dataToDecode):
        decMsg = self._aes.decrypt(dataToDecode)

        return decMsg

