import Cryptodome.Cipher.AES as AES


class EncoDecode:
    def __init__(self):
        self._Key = None

    def setKey(self, key):
        self._Key=key
        self._aes = AES.new(self._Key, AES.MODE_CBC, len(self._Key))

    def Encode(self, dataToEncode):
        encMsg = self._aes.encrypt(dataToEncode)

        return encMsg

    def Decode(self, dataToDecode):
        decMsg = self._aes.decrypt(dataToDecode)

        return decMsg
