from flask import Flask, render_template
from utils.pathConfig import *
from generate_plot.treeMap import *
from jinja2 import Markup, Environment, FileSystemLoader
app = Flask(__name__, template_folder=frontEndPath, static_folder=frontEndPath)  # 开头必写，创建一个Flask对象从而进行后续操作
app.config["SECRET_KEY"] = "ABCDFWA"  # 为防CSRF提供一个密匙


@app.route('/')
def hello_world():
    c = generateTreeMap(flare_path=dataPoolPath)
    return render_template(
        'detailPage.html',
        MainMap=c.render_embed()
    )


if __name__ == '__main__':
    app.run(debug=True)
    # 用刚刚创建的Flask对象控制程序运行
