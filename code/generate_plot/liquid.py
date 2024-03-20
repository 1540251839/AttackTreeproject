from pyecharts import options as opts
from pyecharts.charts import Liquid


def generate_liquid():
    c = (
        Liquid(init_opts=opts.InitOpts(width="400px", height="320px"))
        .add("lq", [0.6, 0.7, 0.8], is_outline_show=False)
        .set_series_opts(label_opts=opts.TextStyleOpts(color='white'))
    )
    return c