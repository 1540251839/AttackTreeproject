from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline
from pyecharts.faker import Faker


def generate_tab(graph1, graph2):
    tl = (
        Timeline(init_opts=opts.InitOpts(width="45vh", height="40vh"))
        .add_schema(
            pos_left='center',
            width="50%",
        )
    )
    tl.add(graph1, 1)
    tl.add(graph2, 2)
    return tl
