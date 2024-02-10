from flask import Flask, request, jsonify
import ccxt

app = Flask(__name__)

with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()
with open('secret_key.txt', 'r') as file:
    secret_key = file.read().strip()

exchange = ccxt.bybit({
    'apiKey': api_key,
    'secret': secret_key,
})

@app.route('/do_something', methods=['GET', 'POST'])
def do_something():
    if not request.method == 'POST':
        return
    # POST 요청에서 JSON 데이터 인자를 받습니다.
    data = request.json  # JSON 데이터 전체를 파이썬 딕셔너리로 받습니다.
    req_type = data.get('type')
    suc_fail = False
    details = {}
    req_response = None
    if req_type == 'order':
        side = data.get('side')
        symbol = data.get('symbol')
        price = data.get('price')
        qty = data.get('qty')
        details = {'symbol': symbol, 'price': price, 'qty': qty}
        if side == 'buy' or side == 'BUY':
            try:
                req_response = exchange.create_limit_buy_order(symbol,qty,price)
                print(req_response)
                suc_fail = True
            except Exception as e:
                print('Error:',e)
                req_response = str(e)
        elif side == 'sell' or side == 'SELL':
            try:
                req_response = exchange.create_limit_buy_order(symbol,qty,price)
                print(req_response)
                suc_fail = True
            except Exception as e:
                print('Error:',e)
                req_response = str(e)
    elif req_type == 'cancel':
        id = data.get('id')
        symbol = data.get('symbol')
        details = {'id':id,'symbol': symbol}
        try:
            req_response = exchange.cancel_order(id, symbol)
            print(req_response)
            suc_fail = True
        except Exception as e:
            print('Error:',e)
            req_response = str(e)
    elif req_type == 'cancel_all':
        symbol = data.get('symbol')
        details = {'symbol':symbol}
        try:
            req_response = exchange.cancel_all_orders(symbol)
            print(req_response)
            suc_fail = True
        except Exception as e:
            print('Error:',e)
            req_response = str(e)
    if suc_fail:
        status = 'success'
    else:
        status = 'fail'
    response = {
        'status': status,
        'req_type' : req_type,
        'details': details,
        'response': req_response
    }
    # 여기에 나머지 코드를 작성합니다.
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)