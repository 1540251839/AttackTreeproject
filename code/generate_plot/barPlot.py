from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType
import pyecharts.options as opts


"""
def generateBarPlot():
    c = (
        Bar(
            init_opts=opts.InitOpts(width="500px", height="420px")
        )
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_series_opts(
            label_opts=opts.LabelOpts(color="#ff0000"),  # 数据标签颜色
            legend_text_color="#00ff00",  # 图例文字颜色
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{b}: {c}"),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(color="#0000ff")),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(color="#ffff00")),
        )
        # .render("bar_base_dict_config.html")
    )
    return c
"""


def generateBarPlot():
    c = (
        Bar(init_opts=opts.InitOpts(width="500px", height="390px"))
        .add_xaxis(Faker.days_attrs)
        .add_yaxis("Y_Value", Faker.days_values, color="skyblue")
        .set_global_opts(
            # title_opts=opts.TitleOpts(title="Bar-DataZoom（slider+inside）"),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(color="white")),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(color="white")),
        )
        .set_series_opts(
            label_opts=opts.LabelOpts(color="white"),  # 数据标签颜色
            legend_text_color="white",  # 图例文字颜色
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{b}: {c}"),
        )
    )
    return c