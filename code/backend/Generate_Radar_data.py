"""
本文件主要目的为给出的图计算拓扑稳健度、关键点防护能力、结构合理性、样本适量性四个指标

**输入数据格式详解**

- **nodes**: 一个列表，其中每个元素都是一个字典，表示一个节点。每个节点具有以下两个属性：
  - `"name"`: 字符串类型，表示节点的唯一标识或名称。
  - `"symbolSize"`: 整数类型，表示节点的大小或视觉重要性，具体含义取决于后续的图表渲染库。

- **links**: 一个列表，其中每个元素也是一个字典，表示一条连接两个节点的边。每条边具有以下两个属性：
  - `"source"`: 字符串类型，引用`nodes`列表中某个节点的`"name"`属性，表示这条边的起始节点。
  - `"target"`: 字符串类型，引用`nodes`列表中另一个节点的`"name"`属性，表示这条边的目标节点。

nodes输入类似如下：
[
  {'name': '结点1', 'symbolSize': 10},
  {'name': '结点2', 'symbolSize': 20},
  {'name': '结点3', 'symbolSize': 30}
]

links输入类似如下：
[
  {'source': '结点1', 'target': '结点1'},
  {'source': '结点1', 'target': '结点2'},
  {'source': '结点1', 'target': '结点3'},
  {'source': '结点1', 'target': '结点4'},
  {'source': '结点1', 'target': '结点5'}
]

**各指标计算方法**

- 拓扑稳健度： 通过计算网络的最大割(MST Edge-Cut)来衡量，最大割值越小，拓扑稳健度越高。
- 关键点防护能力：通过计算symbolSize值高的节点和平均节点的symbolSize值的差距占最大symbolSize和最小symbolSize值的百分比来衡量。
- 结构合理性：通过计算网络中任意两点之间的平均最短路径的倒数来衡量。
- 样本适量性：令点的数量和14的差值的绝对值=a，计算1/(a+1)来衡量
"""
import networkx as nx

# 从节点列表和边列表创建图
def create_graph(nodes, links):
    G = nx.Graph()
    # 添加节点
    for node in nodes:
        G.add_node(node['name'], symbolSize=node['symbolSize'])
    # 添加边
    for link in links:
        G.add_edge(link['source'], link['target'])
    return G

# 计算拓扑稳健度
def compute_topology_robustness(graph):
    mst_edges = nx.minimum_spanning_tree(graph).edges()
    mst_weight = len(mst_edges)  # 最小生成树的边数作为拓扑稳健度指标
    return mst_weight

# 计算关键点防护能力
def compute_critical_node_protection(nodes):
    max_size = max([node['symbolSize'] for node in nodes])
    min_size = min([node['symbolSize'] for node in nodes])
    avg_size = sum([node['symbolSize'] for node in nodes]) / len(nodes)
    critical_nodes_diff = (max_size - avg_size) / (max_size - min_size)
    return critical_nodes_diff

# 计算结构合理性
def compute_structural_reasonableness(graph):
    avg_shortest_path_length = nx.average_shortest_path_length(graph)
    return 1 / avg_shortest_path_length

# 计算样本适量性
def compute_sample_adequacy(nodes):
    num_nodes = len(nodes)
    adequacy = 1 / (abs(num_nodes - 14) + 1)
    return adequacy

# 示例节点列表
nodes = [
    {'name': '结点1', 'symbolSize': 10},
    {'name': '结点2', 'symbolSize': 20},
    {'name': '结点3', 'symbolSize': 30},
    {'name': '结点4', 'symbolSize': 40},
    {'name': '结点5', 'symbolSize': 50}
]

# 示例边列表
links = [
    {'source': '结点1', 'target': '结点1'},
    {'source': '结点1', 'target': '结点2'},
    {'source': '结点1', 'target': '结点3'},
    {'source': '结点1', 'target': '结点4'},
    {'source': '结点1', 'target': '结点5'}
]

# 创建图
G = create_graph(nodes, links)

# 计算各指标
topology_robustness = compute_topology_robustness(G)
critical_node_protection = compute_critical_node_protection(nodes)
structural_reasonableness = compute_structural_reasonableness(G)
sample_adequacy = compute_sample_adequacy(nodes)

# 构建结果字典
result = {
    "拓扑稳健度": topology_robustness,
    "关键点防护能力": critical_node_protection,
    "结构合理性": structural_reasonableness,
    "样本适量性": sample_adequacy
}

print("计算结果:", result)


'''def calc_metrics(Nodes, Links):
    """
    计算网络的四个关键指标：拓扑稳健度、关键点防护能力、结构合理性、样本适量性。

    参数:
    Nodes: 包含网络节点信息的列表，每个节点是一个字典。
    Links: 包含网络连接信息的列表，每个连接是一个字典。

    返回值:
    一个字典，包含计算得到的四个指标的结果。
    """
    # 确保输入数据的格式正确
    assert isinstance(Nodes, list) and isinstance(Links, list), "输入数据格式错误"
    assert all(isinstance(node, dict) for node in Nodes), "输入数据格式错误"
    assert all(isinstance(link, dict) for link in Links), "输入数据格式错误"

    robustness = None  # 拓扑稳健度初始化
    critical_point = None  # 关键点防护能力初始化
    structure = None  # 结构合理性初始化
    sample_quality = None  # 样本适量性初始化

    # 在这里完成计算四个指标的代码。

    # 确保所有指标都成功计算
    assert robustness is not None and critical_point is not None and structure is not None and sample_quality is not None, "计算指标失败"
    return {"robustness": robustness, "critical_point": critical_point, "structure": structure, "sample_quality": sample_quality}


if __name__ == '__main__':
    nodes = [
        {'name': '结点1', 'symbolSize': 10},
        {'name': '结点2', 'symbolSize': 20},
        {'name': '结点3', 'symbolSize': 30}
    ]

    links = [
        {'source': '结点1', 'target': '结点1'},
        {'source': '结点1', 'target': '结点2'},
        {'source': '结点1', 'target': '结点3'},
        {'source': '结点1', 'target': '结点4'},
        {'source': '结点1', 'target': '结点5'}
    ]
    print(calc_metrics(nodes, links))
    '''