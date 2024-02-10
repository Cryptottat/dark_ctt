from flask import Flask, request, jsonify
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
    if not request.method == 'POST':
        return
    # POST 요청에서 JSON 데이터 인자를 받습니다.
    data = request.json  # JSON 데이터 전체를 파이썬 딕셔너리로 받습니다.
    symbol = data.get('symbol')
    price = data.get('price')
    qty = data.get('qty')
    print(f'Received: Symbol={symbol}, Price={price}, Quantity={qty}')
    response = {
        'status': 'success',
        'message': f'Received symbol: {symbol}, price: {price}, and quantity: {qty}'
    }
    # 여기에 나머지 코드를 작성합니다.
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)