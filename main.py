from bot import Bot

key = '492849753:AAHVNZvwPs_AfxYX3hGVybnI_fBEmlumQ7M'

WMHBot = Bot(key)
greeting = ('hello','hi','good morning')

def main():
    new_offset = None
    factorial  = False
    fibonacci  = False
    while True:
        WMHBot.get_updates(new_offset)

        last_update = WMHBot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greeting:
            WMHBot.send_mess(last_chat_id, f'{last_chat_text}, {last_chat_name}')
        elif "factorial" in last_chat_text.lower():
            factorial = True
            WMHBot.send_mess(last_chat_id,"Number:")
        elif factorial and int(last_chat_text):
            WMHBot.send_mess(last_chat_id ,f'Factorial from {last_chat_text}: {WMHBot.factorial(int(last_chat_text))}')
            factorial = False
        elif "fibonacci" or "fibo" in last_chat_text.lower():
            fibonacci = True
            WMHBot.send_mess(last_chat_id,"Number:")
        elif fibonacci and int(last_chat_text):
            WMHBot.send_mess(last_chat_id ,f'{last_chat_text}th fibonacci number is {WMHBot.fibonacci(int(last_chat_text))}')
            fibonacci = False



        new_offset = last_update_id + 1



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
