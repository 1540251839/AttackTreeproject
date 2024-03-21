from pyecharts import options as opts
from pyecharts.charts import Graph

js_func = """
        console.log('hello world')
    """


def generate_demo_relation_graph():
    nodes = [
        {"name": "结点1", "symbolSize": 10},
        {"name": "结点2", "symbolSize": 20},
        {"name": "结点3", "symbolSize": 30},
        {"name": "结点4", "symbolSize": 40},
        {"name": "结点5", "symbolSize": 50},
        {"name": "结点6", "symbolSize": 40},
        {"name": "结点7", "symbolSize": 30},
        {"name": "结点8", "symbolSize": 20},
    ]
    links = []
    for i in nodes:
        for j in nodes:
            links.append({"source": i.get("name"), "target": j.get("name")})
    return nodes, links


def generate_relation_graph(InputGraph=None):
    if InputGraph is None:
        nodes, links = generate_demo_relation_graph()
    else:
        assert isinstance(InputGraph,
                          dict) and 'nodes' in InputGraph and 'links' in InputGraph, 'InputGraph must be a dict with keys "nodes" and "links"'
        nodes = InputGraph['nodes']
        links = InputGraph['links']
    c = (
        Graph(init_opts=opts.InitOpts(width="85vh", height="80vh", chart_id='relationship'))
        .add("",
             nodes,
             links,
             repulsion=8000,
             edge_length=300,
             linestyle_opts=opts.LineStyleOpts(width=2, curve=0.1, opacity=1),
             label_opts=opts.LabelOpts(is_show=True),
             gravity=0.1
             )
        .set_global_opts(title_opts=opts.TitleOpts(title="Graph-基本示例", is_show=False))
        .add_js_funcs(js_func)

    )
    return c
