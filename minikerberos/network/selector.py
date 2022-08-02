from minikerberos.network.clientsocket import KerberosClientSocket
from minikerberos.network.aioclientsocket import AIOKerberosClientSocket
from minikerberos.network.aioclientsockssocket import AIOKerberosClientSocksSocket

class KerberosClientSocketSelector:
    def __init__(self):
        pass
    
    @staticmethod
    def select(target, is_async = False):
        if is_async is False:
            return KerberosClientSocket(target)
        if target.proxy is None:
            return AIOKerberosClientSocket(target)
        else:
            return AIOKerberosClientSocksSocket(target)