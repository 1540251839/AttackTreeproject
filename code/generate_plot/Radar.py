from pyecharts import options as opts
from pyecharts.charts import Radar

data0 = [{"value": [4, 2, 2, 3], "name": "图安全系数子指标"}]
c_schema0 = [
    {"name": "拓扑稳健度", "max": 4, "min": -4},
    {"name": "关键点防护能力", "max": 4, "min": -4},
    {"name": "结构合理性", "max": 4, "min": -4},
    {"name": "样本适量性", "max": 4, "min": -4},
]


def generate_radar(data=None, c_schema=None, series_name="指标"):
    if data is None:
        data = data0
    if c_schema is None:
        c_schema = c_schema0
    assert len(c_schema) == len(data[0]['value']), "c_schema length must equal data length"
    c = (
        Radar(init_opts=opts.InitOpts(width="45vh", height="40vh"))
        .set_colors(["#4587E7"])
        .add_schema(
            schema=c_schema,
            shape="circle",
            center=["50%", "50%"],
            radius="80%",
            angleaxis_opts=opts.AngleAxisOpts(
                min_=0,
                max_=360,
                is_clockwise=False,
                interval=5,
                axistick_opts=opts.AxisTickOpts(is_show=False),
                axislabel_opts=opts.LabelOpts(is_show=False),
                axisline_opts=opts.AxisLineOpts(is_show=False),
                splitline_opts=opts.SplitLineOpts(is_show=False),
            ),
            radiusaxis_opts=opts.RadiusAxisOpts(
                min_=-4,
                max_=4,
                interval=2,
                splitarea_opts=opts.SplitAreaOpts(
                    is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                ),
            ),
            axislabel_opt=opts.LabelOpts(is_show=False),
            textstyle_opts=opts.TextStyleOpts(color="white"),
            polar_opts=opts.PolarOpts(),
            splitarea_opt=opts.SplitAreaOpts(is_show=False),
            splitline_opt=opts.SplitLineOpts(is_show=False),
        )
        .add(
            series_name=series_name,
            data=data,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.1),
            linestyle_opts=opts.LineStyleOpts(width=1),
            color='blue'
        )
        .set_global_opts(
            legend_opts=opts.LegendOpts(
                is_show=True,
                orient='horizontal',
                align='right',
                pos_right='10%',
                textstyle_opts=opts.TextStyleOpts(color="white")
            )
        )
    )
    return c