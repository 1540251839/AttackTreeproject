from pyecharts import options as opts
from pyecharts.charts import Graph

# 定义一个JavaScript函数，用于在控制台输出"hello world"
js_func = """
        console.log('hello world')
    """


def generate_demo_relation_graph():
    """
    生成一个演示用的关系图的节点和边。

    返回:
    - nodes: 节点列表，每个节点包含"name"和"symbolSize"属性。
    - links: 边列表，每条边包含"source"和"target"属性，分别表示源节点和目标节点的名称。
    """
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
    # 为每个节点生成与其他所有节点的连接
    for i in nodes:
        for j in nodes:
            links.append({"source": i.get("name"), "target": j.get("name")})
    return nodes, links


def validate_relation_graph_data(nodes, links):
    """
    检查关系图的节点和边数据格式是否符合标准。

    参数:
    - nodes: 待验证的节点列表，每个节点应包含"name"和"symbolSize"属性。
    - links: 待验证的边列表，每条边应包含"source"和"target"属性，分别表示源节点和目标节点的名称。

    返回:
    - True: 如果nodes和links的数据格式均符合标准。
    - False: 如果nodes或links中有任何一个元素不符合上述格式标准。

    注意：此函数仅验证数据结构格式，不检查逻辑关联（如：是否存在循环引用、不存在孤立节点等）。
    """

    # 验证节点列表
    for node in nodes:
        if not isinstance(node, dict) or "name" not in node or "symbolSize" not in node:
            return False

    # 验证边列表
    for link in links:
        if not isinstance(link, dict) or "source" not in link or "target" not in link:
            return False
        # 检查source和target是否存在于节点列表中
        source_exists = any(node["name"] == link["source"] for node in nodes)
        target_exists = any(node["name"] == link["target"] for node in nodes)
        if not (source_exists and target_exists):
            return False

    return True


def generate_relation_graph(InputGraph=None):
    """
    根据提供的图数据或生成的演示数据，生成关系图。

    参数:
    - InputGraph: 字典，可选，包含"nodes"和"links"键，分别对应节点和边的数据。

    返回:
    - c: Graph对象，表示生成的关系图。
    """
    if InputGraph is None:
        # 如果没有提供图数据，使用演示数据
        nodes, links = generate_demo_relation_graph()
    else:
        # 确认InputGraph是包含"nodes"和"links"键的字典
        assert isinstance(InputGraph,
                          dict) and 'nodes' in InputGraph and 'links' in InputGraph, 'InputGraph must be a dict with keys "nodes" and "links"'
        assert validate_relation_graph_data(nodes=InputGraph['nodes'], links=InputGraph['links']), 'InputGraph data is invalid'
        nodes = InputGraph['nodes']
        links = InputGraph['links']
    # 创建Graph对象，并配置其各项属性
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
        .add_js_funcs(js_func)  # 添加JavaScript函数，在图加载时执行
    )
    return c
