from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline
from pyecharts.faker import Faker


def generate_timeline_pie(Y1_name="Y1_name", Y2_name="Y2_name", Y1=None, Y2=None, X=None):
    if Y1 is None or Y2 is None or X is None:
        X = Faker.choose()
        Y1 = [Faker.values() for _ in range(5)]
        Y2 = [Faker.values() for _ in range(5)]
    tl = Timeline(
        init_opts=opts.InitOpts(width="45vh", height="35vh")
    ).add_schema(
        is_auto_play=True,
        is_loop_play=True,
        pos_left='center',
        width="80%",
    )
    for i in range(len(Y1)):
        bar = (
            Bar()
            .add_xaxis(X)
            .add_yaxis(Y1_name, Y1[i])
            .add_yaxis(Y2_name, Y2[i])
            .set_global_opts(
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
        )
        tl.add(bar, "{}".format(i))
    return tl


"""
.set_global_opts(
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
"""
