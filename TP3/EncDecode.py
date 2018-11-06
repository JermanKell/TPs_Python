import Cryptodome.Cipher.AES as AES
import Cryptodome.Random as Random


class EncoDecode:
    def __init__(self):
        self._Key = None
        self.bs = 32

    def setKey(self, key):
        #self._Key=key

        self._Key = Random.new().read(32)

        self._value = Random.new().read(AES.block_size)
        self._aes = AES.new(self._Key, AES.MODE_CBC, self._value)

    def Encode(self, dataToEncode):
        dataToEncode = dataToEncode.encode('utf-8')
        data = self._add_padding(dataToEncode)

        encMsg = self._value + self._aes.encrypt(data)
        encMsg = str(encMsg)

        return encMsg

    def Decode(self, dataToDecode):
        if len(dataToDecode) <= AES.block_size:
            raise Exception("Invalid ciphertext.")
        self._value = dataToDecode[:AES.block_size]
        data = dataToDecode[AES.block_size:]

        decMsg = self._aes.decrypt(data)
        decMsg = self._remove_padding(decMsg)

        return decMsg.decode('utf-8')

    def _add_padding(self, dataToEncode):
        # si le msg est deja encode sur 16 octets, aucun ajout
        if len(dataToEncode) % 16 == 0:
            return dataToEncode

        # On enlève un byte pour ajouter le 0x80
        dataToAdd = 16 - (len(dataToEncode) % 16)

        dataToEncode += bytes([dataToAdd])*dataToAdd

        return dataToEncode

    def _remove_padding(self, dataToDecode):
        if not dataToDecode:
            return dataToDecode

            dataToDecode = dataToDecode.rstrip('\x00')
        if dataToDecode[-1] == '\x80':
            return dataToDecode[:-1]
        else:
            return dataToDecode