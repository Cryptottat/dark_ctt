from flask import Flask, request
app = Flask(__name__)

with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()
with open('secret_key.txt', 'r') as file:
    secret_key = file.read().strip()

# exchange = ccxt.bybit({
#     'apiKey': api_key,
#     'secret': secret_key,
# })

@app.route('/do_something', methods=['GET', 'POST'])
def do_something():
    # 여기에 특정 기능을 수행하는 코드를 작성합니다.
    print('do_someting')
    # exchange.cancel_all()
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)