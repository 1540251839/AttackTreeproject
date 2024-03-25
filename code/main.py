# -*- coding: utf-8 -*-

from flask import Flask, render_template
from utils.pathConfig import *
from generate_plot.treeMap import *
from generate_plot.multiCharts import *
from generate_plot.liquid import *
from generate_plot.relationShipGraph import *
from generate_plot.singleBarPlot import *
from generate_plot.timeLine import *
from generate_plot.Radar import *
from backend.drawCluster import draw
import argparse
app = Flask(__name__, template_folder=frontEndPath, static_folder=frontEndPath)  # 创建Flask应用实例，配置模板和静态文件路径
app.config["SECRET_KEY"] = "ABCDFWA"  # 配置Flask应用的密钥

report = "对于该拓扑网络的安全性分析报告如下：[newline]1. **网络拓扑结构概述**： 经过深入分析，当前网络采用的是（星型/环形/网状/树状等）拓扑结构，其中包含主要节点数量为N个，连接方式和链路关系稳定。各节点间的通信路径多样，确保了网络的冗余性和可靠性。[newline][newline]2. **安全风险评估**：[newline]   - **设备安全**: 已识别出M台关键设备存在固件版本过时、默认配置未更改等问题。[newline]   - **链路安全**: 发现K条链路上未启用必要的加密协议，可能存在数据泄露的风险。[newline]   - **访问控制**: 部分网络区域间的访问控制策略不严，存在潜在的非法入侵点。[newline][newline]3. **漏洞扫描与威胁检测**： 扫描结果显示共有X个中高危漏洞，集中在操作系统服务、应用程序接口及网络设备配置等方面，需尽快采取补丁更新或策略调整措施。[newline][newline]4. **安全建议与改进建议**：[newline]   - 升级所有设备至最新安全固件版本，并加强设备的基线配置管理。[newline]   - 实施全网链路加密，确保敏感信息在传输过程中的安全性。[newline]   - 优化访问控制列表（ACL），实施最小权限原则，仅允许必要服务和用户进行特定网络资源访问。[newline][newline]5. **后续监控与审计建议**：[newline]   建议建立持续性的网络监控系统，对网络流量、异常行为、日志事件等进行实时监测，并定期进行安全审计，确保及时发现并响应新的安全威胁。[newline][newline]本报告基于实际扫描结果和规则模型构建的安全评估，旨在提供全面而详尽的安全状况概览，并针对具体问题提出可操作的安全改进措施。"
graph_nodes = [{"name": f"node{i}", "value": i ** i} for i in range(30)]  # 生成节点数据


@app.route('/detail/<equipment>', methods=['GET', 'POST'])
def detailPage(equipment):
    """
    处理设备详情页面的请求，根据指定设备名称显示相关详情和图表。

    参数:
    - equipment: 设备名称，用于指定要显示的设备详情。

    返回值:
    - 渲染后的设备详情页面。
    """
    # 初始化设备详情信息
    equipment_name = equipment
    equipment_detail_name = "equipment_detail_name"
    equipment_detail_type = "equipment_detail_type"
    equipment_detail_status = "equipment_detail_status"
    equipment_protection_advise = 'equipment_protection_advise'
    percentage_of_equipment = 0.54

    # 生成各种图表
    TreeMap = generateTreeMap()
    mult = generate_muti()
    mult2 = generate_muti_reverse()
    liquid = generate_liquid(percentage_of_equipment)
    return render_template(
        'detailPage.html',
        MainMap=TreeMap.render_embed(),
        mult=mult.render_embed(),
        mult2=mult2.render_embed(),
        liquid=liquid.render_embed(),
        equipment_name=equipment_name,
        equipment_detail_name=equipment_detail_name,
        equipment_detail_type=equipment_detail_type,
        equipment_detail_status=equipment_detail_status,
        equipment_protection_advise=equipment_protection_advise,
        graph_nodes=graph_nodes,
    )


@app.route('/')
def MainPage():
    """
    处理主页面的请求，显示概览图表和报告。

    返回值:
    - 渲染后的主页面。
    """
    # 生成各种概览图表
    relationShipGraph = generate_relation_graph()
    barPlot = generate_single_barPlot()
    timeLine = generate_timeline_pie()
    radar = generate_radar()
    return render_template(
        'MainPage.html',
        relationShipGraph=relationShipGraph.render_embed(),
        barPlot=barPlot.render_embed(),
        timeLine=timeLine.render_embed(),
        radar=radar.render_embed(),
        graph_nodes=graph_nodes,
        report=report

    )


if __name__ == '__main__':
    # 初始化命令行参数解析器
    arg_parser = argparse.ArgumentParser()
    # 添加可选的运行模式参数
    arg_parser.add_argument('--mode', type=str, default='webPage', choices=['webPage', 'cluster_result'])
    # 解析命令行参数
    args = arg_parser.parse_args()
    if args.mode == 'webPage':
        # 在调试模式下运行Web应用
        app.run(debug=True)
    elif args.mode == 'cluster_result':
        # 生成并保存集群结果图
        draw(resultPklPath=os.path.join(dataPoolPath, 'clusterResult.pkl'), savePath=os.path.join(dataPoolPath, "cluster_result.png"))

