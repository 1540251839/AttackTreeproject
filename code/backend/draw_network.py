import matplotlib.pyplot as plt
import networkx as nx
import random


def generate_special_graph(n, core_node_ratio=0.1, relay_node_ratio=0.3, avg_degree_core=5, avg_degree_relay=3, avg_degree_service=1, allow_self_loops=False):
    """
    生成一个具有特殊拓扑结构的无向图。

    参数:
    n (int): 图中节点总数。
    core_node_ratio (float, optional): 核心节点占总节点数的比例，默认为0.1。
    relay_node_ratio (float, optional): 中继节点占总节点数的比例，默认为0.3。
    avg_degree_core (int, optional): 核心节点平均出度，默认为5。
    avg_degree_relay (int, optional): 中继节点平均出度，默认为3。
    avg_degree_service (int, optional): 服务节点平均出度，默认为1。
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
    for node in G.nodes():
        node_type = G.nodes[node]["type"]
        for _ in range(degrees[node_type]):
            while True:
                target = random.randint(0, n-1)
                if node != target or allow_self_loops:  # 避免自环或根据allow_self_loops选择是否允许自环
                    if not G.has_edge(node, target):  # 避免重复边
                        G.add_edge(node, target)
                        break

    return G


def draw_graph(G):
    """
    绘制无向图G并显示图形。

    参数:
    G (networkx.Graph): 待绘制的无向图。
    """
    # 使用nx.draw进行基本绘图
    pos = nx.spring_layout(G)  # 使用spring布局算法生成节点位置
    nx.draw(G, pos, with_labels=True)

    # 或者，如果您想要使用更丰富的样式选项，可以使用nx.draw_networkx
    # 注意：通常只需选择一种绘图方式即可
    # pos = nx.kamada_kawai_layout(G)  # 可以尝试其他布局算法
    # nx.draw_networkx(G, pos, with_labels=True, font_size=10, node_color='lightblue', edge_color='gray')

    # 显示图形
    plt.show()


# 示例
X = generate_special_graph(50)
draw_graph(X)



print("end")