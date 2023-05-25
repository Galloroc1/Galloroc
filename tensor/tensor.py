import numpy as np
from numpy import ndarray
from FL_Paillier.paillier.paillier import PaillierPublicKey, PaillierPrivateKey, EncryptedNumber
from communicate.config import Config


class SingleTensor(ndarray, EncryptedNumber):

    def __new__(cls, value, role=None):
        obj = np.asarray(value).view(cls)
        obj.role = role
        return obj

    def __init__(self, value, role=None):
        pass

    def send(self):
        pass

    def rec(self):
        pass

    def toDecrypt(self, private_key: PaillierPrivateKey):
        self.real = private_key.decrypt(self.real)
        self.is_encrypt = False

    def toEncrypt(self, public_key: PaillierPublicKey):
        self.real = public_key.encrypt(value=self.real)
        self.is_encrypt = True

    def get_it(self, other):
        # todo:just test
        self = np.asarray([test(),test(),test()])
        return self


class test:

    def __init__(self):
        pass

def tensor(value):
    assert Config.role != str, f'init communicate first plz'
    x = SingleTensor(value = value, role=Config.role)
    return x

Config.init()
data = tensor([1,2,3])
print(data)
print(data.get_it(2))
