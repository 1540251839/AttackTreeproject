from flask import Flask, render_template
from utils.pathConfig import *
from generate_plot.treeMap import *
from generate_plot.barPlot import *
from generate_plot.scatterPlot import *
from generate_plot.sunBurst import *
from generate_plot.multiCharts import *
from generate_plot.liquid import *
from jinja2 import Markup, Environment, FileSystemLoader
app = Flask(__name__, template_folder=frontEndPath, static_folder=frontEndPath)  # 开头必写，创建一个Flask对象从而进行后续操作
app.config["SECRET_KEY"] = "ABCDFWA"  # 为防CSRF提供一个密匙


@app.route('/')
def hello_world():
    TreeMap = generateTreeMap(flare_path=dataPoolPath)
    barPlot1 = generateBarPlot()
    scatterPlot = generate_scatter_plot()
    sunBurst = generateSunBurst()
    mult = generate_muti()
    mult2 = generate_muti_reverse()
    liquid = generate_liquid()
    return render_template(
        'detailPage.html',
        MainMap=TreeMap.render_embed(),
        BarPlot1=barPlot1.render_embed(),
        scatterPlot=scatterPlot.render_embed(),
        sunBurst=sunBurst.render_embed(),
        mult=mult.render_embed(),
        mult2=mult2.render_embed(),
        liquid=liquid.render_embed()
    )


if __name__ == '__main__':
    app.run(debug=True)
    # 用刚刚创建的Flask对象控制程序运行
