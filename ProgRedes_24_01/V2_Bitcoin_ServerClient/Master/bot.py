import requests, json

# STATIC VARIABLES

TOKEN = '7281019772:AAEsW8LSoxz5BLl5zDGMCiAQrYhLZSIm9mw'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}'

def getUpdates(offset=None):
    url = f'{BASE_URL}/getUpdates'
    params = {'offset': offset}
    response = requests.get(url, params=params)
    return response.json()

def sendMessage(chat_id, text):
    url = f'{BASE_URL}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, json=payload)
    return response.json()

def startBot():
    offset = None
    while True:
        updates = getUpdates(offset)
        for update in updates.get('result', []):
            chat_id = update['message']['chat']['id']
            text = update['message']['text']
            if text == '/start':
                sendMessage(chat_id, 'Bitcoin Server Commands:\n/validtrans\n/pendtrans\n/clients')
            elif text == '/validtrans':
                sendMessage(chat_id, 'funcionou')
            elif text == '/pendtrans':
                sendMessage(chat_id, 'pendtrans')
            elif text == '/clients':
                sendMessage(chat_id, 'agents')
            else:
                sendMessage(chat_id, 'ERROR: Invalid command ...')
            offset = update['update_id'] + 1

startBot()