import Cryptodome.Cipher.AES as AES
from Cryptodome import Random


class EncoDecode:
    def __init__(self):
        self._Key = None

    def setKey(self, key):
        self._Key=key
        generatedValue = Random.new().read(AES.block_size)
        self._aes = AES.new(self._Key, AES.MODE_CBC, generatedValue)

    def Encode(self, dataToEncode):
        encMsg = self._aes.encrypt(dataToEncode)

        return encMsg

    def Decode(self, dataToDecode):
        decMsg = self._aes.decrypt(dataToDecode)

        return decMsg

