from pyecharts import options as opts
from pyecharts.charts import Tree


def generate_random_json_tree():
    """
    生成一个预定义的树状JSON数据结构，该结构模拟了一种层次化的分类或组织关系。

    这个JSON数据字典采用嵌套结构表示树形结构，其中：
    - 每个节点是一个包含`name`（节点名称）属性的字典；
    - 节点还可以包含一个名为`children`的列表属性，用于存储其子节点；
    - `value`属性代表与节点关联的数值信息（在本例中，可能表示某种度量、权重或其他统计信息）。

    返回:
    dict: 一个表示树结构的字典，其中顶层节点的名称为"flare"，它具有多个子节点，每个子节点同样可以拥有自己的子节点，形成多级嵌套关系。

    示例结构如下：
    {
        "name": "flare",  # 树的根节点
        "children": [
            {
                "name": "analytics",  # 第一层子节点
                "children": [
                    {"name": "cluster", "value": 3938},  # 第二层子节点
                    {"name": "graph", "value": 502},
                    {"name": "optimization", "value": 1771},
                    {
                        "name": "graph-tree",  # 第二层子节点，且有进一步的子节点
                        "children": [
                            {"name": "dendrogram", "value": 128},
                            {"name": "cluster", "value": 1000},
                            {"name": "layout", "value": 1050},
                            {"name": "sugiyama", "value": 498},
                        ],
                    },
                    {
                        "name": "partition",
                        "children": [
                            {"name": "bundling", "value": 423},
                            {"name": "crop", "value": 220},
                            {"name": "squarify", "value": 1496},
                        ]
                    }
                ]
            }
        ]
    }

    注意：虽然此函数名为“generate_random_json_tree”，但实际提供的JSON数据是硬编码的固定结构，并非真正意义上的随机生成。
    """
    JSON = {
        "name": "flare",
        "children": [
            {
                "name": "analytics",
                "children": [
                    {"name": "cluster", "value": 3938},
                    {"name": "graph", "value": 502},
                    {"name": "optimization", "value": 1771},
                    {
                        "name": "graph-tree",
                        "children": [
                            {"name": "dendrogram", "value": 128},
                            {"name": "cluster", "value": 1000},
                            {"name": "layout", "value": 1050},
                            {"name": "sugiyama", "value": 498},
                        ],
                    },
                    {
                        "name": "partition",
                        "children": [
                            {"name": "bundling", "value": 423},
                            {"name": "crop", "value": 220},
                            {"name": "squarify", "value": 1496},
                        ]
                    }
                ]
            }
        ]
    }
    return JSON


def validate_json_tree(json_tree, depth=0):
    """
    检查传入的JsonTree是否符合预定义的树状JSON数据格式标准，并确保层级深度不超过20层。

    参数:
    json_tree (dict): 待验证的树状JSON数据结构。
    depth (int): 当前递归深度，默认为0，即根节点。

    返回:
    bool: 如果json_tree符合格式标准并且层级深度不超过20层，则返回True，否则返回False。

    格式标准:
    - 根节点必须是一个字典，包含键"name"和可能包含键"children"的列表；
    - "children"列表中的每个元素都应该是包含键"name"的字典，并且可能还包含键"value"以及自身的"children"列表；
    - "name"属性的值必须是字符串类型；
    - "value"属性的值可以是数字类型，也可以不存在；
    - 子节点的嵌套结构最多可以递归到第20层。
    """

    def is_valid_node(node, current_depth):
        if current_depth > 20:
            return False
        if not isinstance(node, dict):
            return False
        if "name" not in node or not isinstance(node["name"], str):
            return False
        if "children" in node:
            if not isinstance(node["children"], list):
                return False
            for child in node["children"]:
                if not is_valid_node(child, current_depth + 1):
                    return False
        return True

    # 验证根节点
    return is_valid_node(json_tree, depth)


def generateTreeMap(InputJsonTree=None):
    """
    根据输入的JSON树数据生成树图。

    参数:
    InputJsonTree (dict, optional): 输入的树状JSON数据。如果未提供，则使用随机生成的JSON数据。

    返回:
    Tree: 生成的树图对象。
    """
    if InputJsonTree is not None:
        JSON = InputJsonTree
    else:
        JSON = generate_random_json_tree()
    assert validate_json_tree(JSON), 'tree shape invalid'
    # 创建并配置树图
    c = (
        Tree()
        .add(
            "",
            [JSON],
            # collapse_interval=2,
            label_opts=opts.LabelOpts(
                position="top",
                horizontal_align="right",
                vertical_align="middle",
            ),
            initial_tree_depth=2
        )
    )
    return c


if __name__ == '__main__':
    print("end")
