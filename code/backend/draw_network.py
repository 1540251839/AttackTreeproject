import matplotlib.pyplot as plt
import networkx as nx
import random
import time
import numpy as np


def generate_special_graph(n, core_node_ratio=0.1, relay_node_ratio=0.3, avg_degree_core=5, avg_degree_relay=3, avg_degree_service=2, allow_self_loops=False):
    """
    生成一个具有特殊拓扑结构的无向图。

    参数:
    n (int): 图中节点总数。
    core_node_ratio (float, optional): 核心节点占总节点数的比例，默认为0.1。
    relay_node_ratio (float, optional): 中继节点占总节点数的比例，默认为0.3。
    avg_degree_core (int, optional): 核心节点平均出度（只针对中继节点），默认为5。
    avg_degree_relay (int, optional): 中继节点平均出度（针对核心节点和服务节点），默认为3。
    avg_degree_service (int, optional): 服务节点平均出度（仅用于统计中继节点连接服务节点的数量，核心节点不与服务节点直接相连），默认为1。
    allow_self_loops (bool, optional): 是否允许自环，默认为False。

    返回:
    G (networkx.Graph): 具有特殊拓扑结构的无向图。

    注：节点类型按照核心、中继、服务顺序排列，且比例之和应小于等于1。
    """

    assert core_node_ratio + relay_node_ratio + (1 - core_node_ratio - relay_node_ratio) <= 1, "节点比例之和必须小于等于1！"

    G = nx.Graph()

    # 添加节点并分类
    core_count = int(n * core_node_ratio)
    relay_count = int(n * relay_node_ratio)
    service_count = n - core_count - relay_count
    node_types = ["core"] * core_count + ["relay"] * relay_count + ["service"] * service_count
    G.add_nodes_from([(i, {"type": t}) for i, t in enumerate(node_types)])

    # 为各类型节点添加合适的出边
    degrees = {"core": avg_degree_core, "relay": avg_degree_relay, "service": avg_degree_service}

    # 核心节点仅连接中继节点
    for core_node in range(core_count):
        for _ in range(degrees["core"]):
            while True:
                target = random.randint(core_count, n-1)  # 确保目标节点是中继或服务节点
                if G.nodes[target]["type"] == "relay" and (core_node != target or allow_self_loops):
                    if not G.has_edge(core_node, target):
                        G.add_edge(core_node, target)
                        break

    # 中继节点可以连接核心节点和服务节点
    for relay_node in range(core_count, core_count + relay_count):
        for _ in range(degrees["relay"]):
            node_type_to_connect = random.choices(["core", "service"], weights=[core_count, service_count])[0]
            if node_type_to_connect == "core":
                valid_targets = list(range(core_count))
            else:
                valid_targets = list(range(core_count + relay_count, n))

            while True:
                target = random.choice(valid_targets)
                if (relay_node != target or allow_self_loops) and not G.has_edge(relay_node, target):
                    G.add_edge(relay_node, target)
                    break

    return G


def draw_graph(G, k=0.2, scale=20):
    """
    绘制无向图G并显示图形，核心节点位于中间区域，relay节点围绕在核心节点外围，service节点位于图的边缘。

    参数:
    G (networkx.Graph): 待绘制的无向图，其中节点应包含"type"属性来标识其类型（"core", "relay", "service"）。
    k (float): 用于布局算法中的节点间距离控制，默认值为0.2。
    scale (int): 用于布局算法中的全局缩放因子，默认值为20。

    返回值:
    无
    """

    plt.figure(figsize=(40, 40))

    # 假设我们设定整个绘图区域的中心点和半径
    center = (500, 500)  # 假设中心点坐标
    radius_core = 40  # 核心节点分布半径
    radius_relay = 150  # 中继节点分布半径
    radius_service = 360  # 服务节点分布半径

    pos = {}
    for node in G.nodes(data=True):
        theta = 2 * np.pi * np.random.rand()  # 随机角度
        if node[1]["type"] == "core":
            r = radius_core + random.randint(0, 90)
        elif node[1]["type"] == "relay":
            r = radius_relay + random.randint(0, 90)
        else:  # service节点
            r = radius_service + random.randint(0, 120)
        pos[node[0]] = (center[0] + r * np.cos(theta), center[1] + r * np.sin(theta))  # 根据极坐标生成随机位置


    # 使用力导向布局优化节点位置，同时保持手动设置的核心节点在中间
    fixed = {node: True if G.nodes[node]["type"] == "core" else False for node in G.nodes()}
    pos = nx.spring_layout(G, pos=pos, k=k, scale=scale, fixed=fixed)

    # 定义不同类别节点间边的宽度及节点颜色
    edge_widths = {("core", "core"): 6, ("core", "relay"): 4, ("core", "service"): 2,
                   ("relay", "relay"): 1.5, ("relay", "service"): 1.5, ("service", "service"): 1}
    node_colors = {"core": 'r', "relay": 'orange', "service": 'lightblue'}

    # 根据定义的颜色和宽度绘制节点和边，并设置节点透明度
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color=[node_colors[node[1]["type"]] for node in G.nodes(data=True)], alpha=0.7)
    nx.draw_networkx_edges(G, pos, width=[edge_widths[(G.nodes[edge[0]]["type"], G.nodes[edge[1]]["type"])]
                                          for edge in G.edges()], alpha=0.7)

    # 添加节点标签
    nx.draw_networkx_labels(G, pos, font_size=20)

    # 显示绘制的图形
    plt.show()


# 示例
X = generate_special_graph(
    350,
    core_node_ratio=0.02,
    relay_node_ratio=0.2,
    avg_degree_core=13,
    avg_degree_relay=8,
    avg_degree_service=4
)
draw_graph(X)
print("end")

# git add .
# git commit -m "add"
# git push origin master
#git pull