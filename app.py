from flask import Flask, request
app = Flask(__name__)

@app.route('/do_something', methods=['GET', 'POST'])
def do_something():
    # 여기에 특정 기능을 수행하는 코드를 작성합니다.
    print('do_someting')
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)