from bot import Bot

key = '492849753:AAHVNZvwPs_AfxYX3hGVybnI_fBEmlumQ7M'

WMHBot = Bot(key)
greeting = ('hello','hi','good morning')

def main():
    new_offset = None

    while True:
        WMHBot.get_updates(new_offset)

        last_update = WMHBot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greeting:
            WMHBot.send_mess(last_chat_id, 'Hello, {}'.format(last_chat_name))

        new_offset = last_update_id + 1



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
