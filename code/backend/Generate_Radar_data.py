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
import math
import random
import networkx as nx


def f(x: float):
    # 输入x，输出f(x)，保留1位小数
    return round(15 * math.log2(x), 1)


def generate_topo_random():
    """
    生成随机拓扑结构。

    无参数。

    返回值:
    - dict: 包含生成的拓扑结构的字典，其中包括 "nodes" 和 "links" 两个键。
            "nodes" 键对应的值是一个包含节点信息的列表，每个节点是一个字典，包括节点名称和大小。
            "links" 键对应的值是一个包含边信息的列表，每个边是一个字典，包括源节点和目标节点的名称。
    """

    # 更改划分线###############################################################
    # 设定节点数量和边数量
    num_nodes = random.randint(18, 24)
    num_edges = int(num_nodes * random.uniform(1.2, 1.8))

    # 创建节点
    nodes = [{'name': f'结点{i}', 'symbolSize': 10} for i in range(1, num_nodes + 1)]

    # 随机选择一个节点，确保每个点至少有一条边
    start_node = random.choice(nodes)

    # 创建边
    edges = []

    # 确保每个点至少有一条边
    for node in nodes:
        if node != start_node and random.randint(1, 6) % 3:
            edges.append((start_node['name'], node['name']))

    # 继续生成其他的边
    remaining_edges = num_edges - (num_nodes - 1)
    for _ in range(remaining_edges):
        i = random.randint(1, num_nodes)
        while i == int(start_node['name'][2:]):  # 当 i 等于起始节点的编号时，重新生成 i
            i = random.randint(1, num_nodes)
        j = random.randint(1, num_nodes)
        while i == j:  # 当 i 等于 j 时，重新生成 j
            j = random.randint(1, num_nodes)
        edges.append((f'结点{i}', f'结点{j}'))

    # 调整节点的大小
    node_degrees = {node['name']: 0 for node in nodes}
    for link in edges:
        node_degrees[link[0]] += 1
        node_degrees[link[1]] += 1

    for node in nodes:
        if node_degrees[node['name']] == 0:
            edges.append((f'结点{random.randint(1, num_nodes)}', node['name']))

    node_degrees = {node['name']: 0 for node in nodes}
    for link in edges:
        node_degrees[link[0]] += 1
        node_degrees[link[1]] += 1

    out_node_degrees = {node['name']: 0 for node in nodes}
    for link in edges:
        out_node_degrees[link[0]] += 1

    for node in nodes:
        node_name = node['name']
        node['symbolSize'] = 10 + out_node_degrees[node_name] * 5

    # 对边缘节点进行随机化扰动
    for node in nodes:
        if node_degrees[node['name']] == 1:
            node['symbolSize'] += random.randint(-2, 2)

    for node in nodes:
        # 对nodes中多个node['symbolSize']对应的数进行归一化
        node['symbolSize'] = f(node['symbolSize'])

    # 将边的列表转换成所需的格式
    links = [{'source': source, 'target': target} for source, target in edges]
    # 更改划分线###############################################################
    return {"nodes": nodes, "links": links}


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


def calc_average_metrix():
    metrix_range = {}
    for T in range(100, 800, 400):
        summary = {}
        for _ in range(T):
            # print(_)
            g = generate_topo_random()
            nodesE, linksE = g['nodes'], g['links']
            try:
                res = calc_metrics(nodesE, linksE)
            except:
                continue
            for name in res[0]:
                if name not in summary:
                    summary[name] = []
                summary[name].append(res[0][name])
        # for name in summary:
        # print(f"name:{name} average: {sum(summary[name])/len(summary[name])} max: {max(summary[name])} min: {min(summary[name])}")
        for name in summary:
            if name not in metrix_range:
                metrix_range[name] = []
            metrix_range[name].append(
                [
                    sum(summary[name]) / len(summary[name]),  # avg value
                    max(summary[name]),  # max value
                    min(summary[name])  # min value
                ]
            )
    c_schema0 = []
    c_schema_with_average = []
    for name in metrix_range:
        max_values = [Ins[1] for Ins in metrix_range[name]]
        min_values = [Ins[2] for Ins in metrix_range[name]]
        average_values = [Ins[0] for Ins in metrix_range[name]]
        c_schema0.append({
            "name": name,
            "max": max(max_values),
            "min": min(min_values)
        })
        c_schema_with_average.append({
            "name": name,
            "max": max(max_values),
            "min": min(min_values),
            'average': sum(average_values) / len(average_values)
        })
    # data0 = [{"value": [values for values in result.values()], "name": "图安全系数子指标"}]
    data1 = [{"value": [round(values['average'], 2) for values in c_schema_with_average], "name": "平均"}]
    return metrix_range, c_schema0, data1[0]


def calc_metrics(nodes, links):
    """
    计算给定节点和边的网络指标。

    参数:
    - nodes: 节点列表，包含所有网络中的节点。
    - links: 边列表，描述网络中节点之间的连接关系。

    返回值:
    - result: 字典，包含计算得到的四个主要网络指标:
      - "拓扑稳健度": 衡量网络在节点失效情况下的稳健性。
      - "关键点防护能力": 衡量保护网络中关键节点的能力。
      - "结构合理性": 衡量网络结构的合理性。
      - "样本适量性": 衡量节点样本的充足性。
    """
    G = create_graph(nodes, links)

    # 初始化网络指标计算
    topology_robustness = compute_topology_robustness(G)  # 计算网络的拓扑稳健度
    critical_node_protection = compute_critical_node_protection(nodes)  # 计算关键节点保护能力
    structural_reasonableness = compute_structural_reasonableness(G)  # 计算网络的结构合理性
    sample_adequacy = compute_sample_adequacy(nodes)  # 计算样本适量性

    # 构建并返回指标结果字典
    result = {
        "稳健度": topology_robustness,
        "关键防护": critical_node_protection,
        "结构": structural_reasonableness,
        "样本量": sample_adequacy
    }
    """
    data0 = [{"value": [4, 2, 2, 3], "name": "图安全系数子指标"}]
    
    c_schema0 = [
        {"name": "拓扑稳健度", "max": 4, "min": -4},
        {"name": "关键点防护能力", "max": 4, "min": -4},
        {"name": "结构合理性", "max": 4, "min": -4},
        {"name": "样本适量性", "max": 4, "min": -4},
    ]
    """
    data0 = {"value": [round(values, 2) for values in result.values()], "name": "本图相关指标"}
    return result, data0


if __name__ == '__main__':
    calc_average_metrix()
    print("end")
