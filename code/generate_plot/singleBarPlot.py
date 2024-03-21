from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode


def generate_single_barPlot(Y_Name="Y_name", title="title", Y=None, X=None):
    if X is None:
        X = Faker.days_attrs
    if Y is None:
        Y = Faker.days_values
    assert len(X) == len(Y), "X and Y must have the same length"
    c = (
        Bar(init_opts=opts.InitOpts(width="45vh", height="40vh"))
        .add_xaxis(X)
        .add_yaxis(Y_Name, Y)
        .set_global_opts(
            title_opts=opts.TitleOpts(title=title, is_show=False),
            datazoom_opts=opts.DataZoomOpts(),
            xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True),
                                     axislabel_opts=opts.LabelOpts(color="white")),
            yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True),
                                     axislabel_opts=opts.LabelOpts(color="white")),
            legend_opts=opts.LegendOpts(
                is_show=True,
                orient='horizontal',
                align='right',
                pos_right='10%',
                textstyle_opts=opts.TextStyleOpts(color="white")
            )
        )
        .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "color": JsCode(
                        """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: 'rgba(0, 244, 255, 1)'
                }, {
                    offset: 1,
                    color: 'rgba(0, 77, 167, 1)'
                }], false)"""
                    ),
                    "barBorderRadius": [30, 30, 30, 30],
                    "shadowColor": "rgb(0, 160, 221)",
                }
            }
        )
    )
    return c
