from pyecharts import options as opts
from pyecharts.charts import Gauge


def generate_gauge(seriesName="seriesName", safetyIndex=80):
    c = (
        Gauge(init_opts=opts.InitOpts(width="45vh", height="45vh"))
        .add(
            seriesName,
            [("安全指数", safetyIndex)],
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color=[(0.3, "#fd666d"), (0.7, "#37a2da"), (1, "#67e0e3")], width=30
                )
            ),
            axislabel_opts=opts.LabelOpts(
                color='white'
            ),
            title_label_opts=opts.GaugeTitleOpts(
                is_show=False
            ),
            detail_label_opts=opts.GaugeDetailOpts(
                is_show=True,
                color='white',
                font_size=20,
            ),
            progress=opts.GaugeProgressOpts(
                is_round_cap=True
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
            )
        )
        .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
        )
        .set_series_opts(label_opts=opts.TextStyleOpts(color='white'))
    )
    return c