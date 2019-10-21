from pip._vendor.distlib.compat import raw_input

from GetMessage.AboutMessage import Message

import os

if __name__ == '__main__':
    mes = Message(os.path.join(os.path.abspath('.'), 'Apks'))
    print(mes.getAllApks_Permission())

raw_input('Press Enter to exit...')
