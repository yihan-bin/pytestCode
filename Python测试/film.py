from flask import Flask, render_template, jsonify
import pandas as pd


app = Flask(__name__)

# 请求默认发送到这里
@app.route("/")
def show():  # show函数负责处理浏览器发送过来的请求
    data = pd.read_csv("abc.csv")
    data = data.rename(columns={"type":"name", "money":"value"})
    data = data.to_dict(orient="records")
    return render_template("show.html", data=data)



# 跳转到高级版页面. 由高级版页面重新发送一个ajax请求. 由下面的getData来完成数据的处理. 并返回
@app.route("/gaoji")
def gaoji():  # 高级版
    return render_template("show_高级版.html")

# 处理ajax请求
@app.route("/getData")
def getData():  # show函数负责处理浏览器发送过来的请求
    data = pd.read_csv("abc.csv")
    data = data.rename(columns={"type":"name", "money":"value"})
    data = data.to_dict(orient="records")
    return jsonify(data)  # 直接返回json数据


if __name__ == '__main__':
    app.run()


