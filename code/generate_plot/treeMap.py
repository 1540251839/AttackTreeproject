import json
import os
from pyecharts import options as opts
from pyecharts.charts import Tree


def generate_random_json_tree():
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



def generateTreeMap(InputJsonTree=None):
    if InputJsonTree is not None:
        JSON = InputJsonTree
    else:
        JSON = generate_random_json_tree()
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