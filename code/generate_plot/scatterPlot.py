from pyecharts import options as opts
from pyecharts.charts import EffectScatter
from pyecharts.faker import Faker


def generate_scatter_plot():
    c = (
        EffectScatter(init_opts=opts.InitOpts(width="500px", height="390px"))
        .add_xaxis(Faker.choose())
        .add_yaxis("", Faker.values())
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True), axislabel_opts=opts.LabelOpts(color="white")),
            yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True), axislabel_opts=opts.LabelOpts(color="white")),
        )
        .set_series_opts(
            label_opts=opts.LabelOpts(color="white"),  # 数据标签颜色
            legend_text_color="white",  # 图例文字颜色
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{b}: {c}"),
        )
    )
    return c
