import requests

TOKEN = '1388382662:AAFStKNIIECt2W3y6AWuBA13qn0_gi7cCFc'

URL = 'https://api.telegram.org/bot{TOKEN}'.format(TOKEN=TOKEN)

r = requests.get(f'{URL}/getUpdates')

print(r.json())