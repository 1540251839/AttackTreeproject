from flask import Flask, render_template
from utils.pathConfig import *
from generate_plot.treeMap import *
from generate_plot.multiCharts import *
from generate_plot.liquid import *
from generate_plot.relationShipGraph import *
from generate_plot.singleBarPlot import *
from generate_plot.timeLine import *
app = Flask(__name__, template_folder=frontEndPath, static_folder=frontEndPath)  # 开头必写，创建一个Flask对象从而进行后续操作
app.config["SECRET_KEY"] = "ABCDFWA"  # 为防CSRF提供一个密匙


@app.route('/detail')
def detailPage():
    instrument_name = "instrument_name"
    instrument_detail_name = "instrument_detail_name"
    instrument_detail_type = "instrument_detail_type"
    instrument_detail_status = "instrument_detail_status"
    instrument_protection_advise = 'instrument_protection_advise'
    percentage_of_instrument = 0.54

    TreeMap = generateTreeMap()
    mult = generate_muti()
    mult2 = generate_muti_reverse()
    liquid = generate_liquid(percentage_of_instrument)
    return render_template(
        'detailPage.html',
        MainMap=TreeMap.render_embed(),
        mult=mult.render_embed(),
        mult2=mult2.render_embed(),
        liquid=liquid.render_embed(),
        instrument_name=instrument_name,
        instrument_detail_name=instrument_detail_name,
        instrument_detail_type=instrument_detail_type,
        instrument_detail_status=instrument_detail_status,
        instrument_protection_advise=instrument_protection_advise
    )


@app.route('/')
def MainPage():
    relationShipGraph = generate_relation_graph()
    barPlot = generate_single_barPlot()
    timeLine = generate_timeline_pie()
    return render_template(
        'MainPage.html',
        relationShipGraph=relationShipGraph.render_embed(),
        barPlot=barPlot.render_embed(),
        timeLine=timeLine.render_embed()
    )


if __name__ == '__main__':
    app.run(debug=True)
    # 用刚刚创建的Flask对象控制程序运行
