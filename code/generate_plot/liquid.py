from pyecharts import options as opts
from pyecharts.charts import Liquid


def generate_liquid(percentage=0.6):
    assert 0 <= percentage <= 1, "percentage must be in [0, 1]"
    c = (
        Liquid(init_opts=opts.InitOpts(width="55vh", height="55vh"))
        .add("lq", [percentage, percentage, percentage], is_outline_show=False)
        .set_series_opts(label_opts=opts.TextStyleOpts(color='white'))
    )
    return c