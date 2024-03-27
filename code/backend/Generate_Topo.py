"""
本文件主要目的是写一个函数，生成一个网络的拓扑结构，包括节点列表和边列表。这些数据用于绘制首页的关系图

**返回数据格式详解**

- **nodes**: 一个列表，其中每个元素都是一个字典，表示一个节点。每个节点具有以下两个属性：
  - `"name"`: 字符串类型，表示节点的唯一标识或名称。
  - `"symbolSize"`: 整数类型，表示节点的大小或视觉重要性，具体含义取决于后续的图表渲染库。

- **links**: 一个列表，其中每个元素也是一个字典，表示一条连接两个节点的边。每条边具有以下两个属性：
  - `"source"`: 字符串类型，引用`nodes`列表中某个节点的`"name"`属性，表示这条边的起始节点。
  - `"target"`: 字符串类型，引用`nodes`列表中另一个节点的`"name"`属性，表示这条边的目标节点。

nodes输出结果类似如下：
[
  {'name': '结点1', 'symbolSize': 10},
  {'name': '结点2', 'symbolSize': 20},
  {'name': '结点3', 'symbolSize': 30}
]

links输出结果类似如下：
[
  {'source': '结点1', 'target': '结点1'},
  {'source': '结点1', 'target': '结点2'},
  {'source': '结点1', 'target': '结点3'},
  {'source': '结点1', 'target': '结点4'},
  {'source': '结点1', 'target': '结点5'}
]

额外要求：
在设计图的拓扑时，要考虑如下问题：
1. 图是设备网络，因此图的结果需要满足设备网络的度特征。也就是，存在少量的（1到2个）节点连接到大量节点，而其他节点（5到10个）则连接到少量节点。
2. 图的节点数量和边数量不能太多，不然可视化效果不好。具体而言，点最好在10个左右，边最好在点的数量的1.5倍左右。
3. 对于图中点的大小，遵循如下规则：点连接的点（出度）越多，点的大小就越大。但是对于边缘节点，可以采取一些随机化扰动来使得边缘节点大小存在少量随机性。
"""
import math
# 更改划分线###############################################################
import random


def reconstructLinks(Topo):
    assert 'nodes' in Topo, "Topo must contain 'nodes'"
    links = Topo['nodes']
    nodeList = [{"name": i['name'], 'value': i['symbolSize']} for i in links]
    return nodeList


def f(x: float):
    # 输入x，输出f(x)，保留1位小数
    return round(15*math.log2(x), 1)


# 更改划分线###############################################################
def generate_topo():
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
    random.seed(15422226)
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


