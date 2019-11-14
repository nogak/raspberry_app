# -*- coding: utf-8 -*-
from flask import Flask


# flaskのインスタンスを作成
app = Flask(__name__)

# root(/)にアクセスした時の処理
# hello worldを表示
@app.route("/")
def hello():
    return "昔々あるところに、おじいさんとおばあさんがいましたとさ。　めでたしめでたし。"

# main関数
if __name__ == "__main__":
    #app.run("126.116.22.130")
    app.run(debug=True, host="192.168.10.50", port=8080)
