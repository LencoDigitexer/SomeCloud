from telethon import TelegramClient, events, sync, connection
# для создания приватного канала
from telethon.tl.functions.channels import CreateChannelRequest, CheckUsernameRequest, UpdateUsernameRequest
from telethon.tl.types import InputChannel, InputPeerChannel

import re # для поиска канала в списке

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 713781
api_hash = '0c51c4c50d0587d53526c7ee082b3e65'
HaveChannel = False
client = TelegramClient(
    'session_name',
    api_id,
    api_hash,

    # Use one of the available connection modes.
    # Normally, this one works with most proxies.
    connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,

    # Then, pass the proxy details as a tuple:
    #     (host name, port, proxy secret)
    #
    # If the proxy has no secret, the secret must be:
    #     '00000000000000000000000000000000'
    proxy=('tg-3.rknsosatb.pw', 443, 'dde99993ad3d7146fcf8f3baa789cc62ac')
)
client.start()
def search_channel(): #поиск канала ///SomeCloud///
    for dialog in client.iter_dialogs():
        allDialog = dialog.name + "\n"
        #print(allDialog)
        if re.search("///SomeCloud///", allDialog):
            HaveChannel = True


if HaveChannel:
    print("Канал уже создан")
else:
    print("Надо создать канал")
    createdPrivateChannel = client(CreateChannelRequest("///SomeCloud///","FileCloud",megagroup=False))
    print("Канал успешно создан")
