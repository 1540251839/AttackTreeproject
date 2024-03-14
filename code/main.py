from flask import Flask, render_template
from utils.pathConfig import *
app = Flask(__name__, template_folder=frontEndPath, static_folder=frontEndPath)  # 开头必写，创建一个Flask对象从而进行后续操作
app.config["SECRET_KEY"] = "ABCDFWA"  # 为防CSRF提供一个密匙


@app.route('/')
def hello_world():  # 这是视图函数
    # 控制相关的代码写在这里面
    return render_template("detailPage.html")


if __name__ == '__main__':
    app.run(debug=True)
    # 用刚刚创建的Flask对象控制程序运行
