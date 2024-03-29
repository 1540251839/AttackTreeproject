import random


class EquipmentMessage:

    def __init__(self):
        # 初始化一个空字典来存储设备类型
        self.equipment_type = {}
        self._generate_equipment_type()
        self.equipment_name = {}
        self._generate_equipment_name()
        self.equipment_status = {}
        self._generate_equipment_status()
        self.equipment_suggestion = {}
        self.start_suggestion = [
            "根据算法分析的结果，我们发现该装置在几个关键的安全领域存在显著的弱点。",
            "结合算法分析，该设备存在如下几个值得关注的弱点。",
            "通过算法分析，我们发现该设备在以下几个关键安全领域存在问题。",
            "根据算法分析，该设备在以下几个关键方面需要改进。",
            "基于算法分析，该设备在以下几个关键安全领域存在不足。",
            "根据算法分析的结果，我们发现该装置在几个关键的安全领域存在显著的弱点。",
            "根据算法分析的结果，我们发现该装置的一些安全隐患。",
            "基于算法分析的结果，我们发现该装置存在部分安全隐患。",
            "结合算法的分析，我们发现该装置存在一些需要注意的安全隐患。",
            "算法分析表明，该装置存在一些安全隐患。"
        ]
        self.Router_suggestions = [i.strip() for i in """
                在固件更新和访问控制方面，该装置表现出明显的不足，这使得它在面对分布式拒绝服务（DDoS）攻击和地址解析协议（ARP）攻击时显得尤为脆弱。为了有效防范这些网络攻击，必须对设备的固件进行定期的更新和维护，并且实施更为严格的访问控制策略。

                在物理安全性方面，该装置存在重大的安全隐患，特别是对USB接口的攻击途径。因此，为了防止通过USB接口发起的攻击，该装置需要采取额外的物理安全措施，例如限制对USB端口的访问或者完全封闭这些端口。

                该装置运行了多个不必要的网络服务，并且对外开放了过多的网络端口，这些不必要的端口和服务大大增加了设备遭受网络攻击的风险，特别是那些针对特定服务的端口攻击。为了减少这种风险，建议关闭所有非必需的服务和端口，从而最小化设备的攻击面，提高整体的安全性。
                """.split("\n\n")]

        self.DataCenter_suggestions = [i.strip() for i in """
                由于该装置在网络端进行数据计算和服务，因此它容易受到来自网络的攻击，例如分布式拒绝服务（DDoS）攻击和地址解析协议（ARP）欺骗等。为了有效防范这些网络攻击，必须对装置的网络安全性进行加固，并采取相应的防护措施。

                由于该装置的硬件更新频率较高，它容易成为供应链攻击的目标。因此，在硬件更新和更换过程中，需要对硬件进行再次的检测和验证，以确保硬件的安全性和可靠性。

                该装置需要实施严格的权限控制，以防止外部的恶意软件和病毒对装置造成感染。这包括对用户权限进行精细化管理，限制不必要的访问权限，以及采取有效的恶意软件和病毒防护措施。

                在物理层面，服务器也需要进行物理权限访问的控制，以隔绝物理的威胁，比如防止数据硬盘被窃取等。这包括对服务器的物理访问进行限制和监控，确保只有授权人员才能接触到服务器硬件。
                """.split("\n\n")]

        self.Switch_suggestions = [i.strip() for i in """
                该装置可能面临MAC地址欺骗和泛洪攻击。为防止此类攻击，网络管理员应确保交换机的MAC地址表准确无误，并对交换机的MAC地址表进行定期维护。同时，可以配置交换机的端口安全功能，限制特定端口上的MAC地址数量，从而减少MAC地址欺骗和泛洪攻击的风险。

                ARP欺骗和中毒攻击也可能对该装置造成威胁。为防范此类攻击，网络管理员应启用交换机的ARP防欺骗功能，并确保网络中的设备使用静态ARP表，以减少ARP欺骗和中毒攻击的风险。

                该装置还可能面临DDoS攻击等网络攻击。为防止此类攻击，网络管理员应配置交换机的流量控制功能，限制特定端口上的流量速率，从而减少DDoS攻击的风险。同时，可以配置交换机的访问控制列表（ACL），过滤掉恶意流量，提高网络的安全性。

                该装置还可能受到端口扫描和嗅探攻击。为防范此类攻击，网络管理员应配置交换机的端口安全功能，限制特定端口上的连接数量，从而减少端口扫描和嗅探攻击的风险。同时，可以配置交换机的VLAN隔离功能，将不同安全级别的网络隔离在不同的VLAN中，以提高网络的安全性。

                该装置的固件和软件漏洞也可能导致安全风险。为防范此类漏洞，网络管理员应确保交换机的固件和软件保持最新，及时安装补丁程序，以修复已知的安全漏洞。

                该装置的物理安全也至关重要。为防范物理安全威胁，网络管理员应确保交换机放置在安全的环境中，限制对交换机的物理访问，并定期检查交换机的配置和状态，以确保其正常运行。
               """.split("\n\n")]

        self.Terminal_suggestions = [i.strip() for i in """
                恶意软件和病毒是该装置面临的主要威胁之一。为防范此类攻击，用户应定期更新操作系统和应用程序，以修复已知的安全漏洞。同时，安装和维护有效的防病毒软件，以实时监测和阻止恶意软件的传播。

                该装置还面临密码攻击的威胁。用户应使用强密码，并采取多因素认证，以增加账户的安全性。同时，定期更改密码，避免使用简单或容易被猜测的密码。

                该装置还容易受到网络钓鱼和社交工程的攻击。用户应提高警惕，不轻易泄露个人信息，不随意打开未知来源的电子邮件附件，以及访问受信任的网站。

                未修补的软件漏洞也可能导致该装置受到攻击。用户应定期更新操作系统和应用程序，以修复已知的安全漏洞。

                作为用户端设备，设备的错误配置可能导致权限丢失，从而影响整个网络拓扑安全性。终端用户应确保网络连接加密，并使用安全的Wi-Fi密码等。

                终端的物理安全威胁也需要引起重视。用户应限制对设备的物理访问，并采取措施防止数据被盗或设备损坏。

                恶意电子邮件附件、浏览器安全威胁、以及使用不安全的移动存储设备也会增加该装置安全风险。用户应谨慎处理这些潜在威胁，并采取相应的防范措施。
               """.split("\n\n")]

        self.Admin_suggestions = [i.strip() for i in """
                该装置可能面临恶意软件和病毒的威胁。为防范此类攻击，管理员应确保管理终端的操作系统和应用程序保持最新，安装和维护有效的防病毒软件，以及定期进行病毒扫描。

                作为管理设备，未授权访问是该装置一个主要的安全风险。管理员应启用访问控制机制，如使用强密码和多因素认证，以及限制对管理终端的访问权限。

                中间人攻击是该装置另一种潜在的威胁。为防止此类攻击，管理员应确保管理终端与网络设备之间的通信使用加密技术，并定期检查网络配置，确保没有开放端口或不当的安全设置。

                该设备容易受到权限提升攻击。为防止此类攻击，管理员应确保系统中的权限设置合理，并定期检查系统日志，以发现异常行为。

                该装置的物理安全威胁需要引起重视。管理员应确保管理终端的物理位置安全，限制对设备的物理访问，并采取措施防止设备被盗或被物理破坏。

                该装置的数据泄露也是一个严重的安全风险。管理员应确保管理终端存储的敏感信息得到有效的加密保护，并采取措施防止数据泄露。

                网络钓鱼和社交工程是针对管理员的另一种攻击方式。管理员应提高警惕，不轻易泄露个人信息，不随意打开未知来源的电子邮件附件，以及访问受信任的网站。
                """.split("\n\n")]
        self._generate_equipment_suggestion()

    def _generate_equipment_type(self):
        # 路由器节点列表
        router_nodes = [14, 9, 19, 17, 11]
        # 数据中心节点列表
        data_center_nodes = [3, 15, 2, 16, 10, 5, 1, 7, 6]
        # 交换机节点列表
        switch_nodes = [10, 4]
        # 终端节点列表
        terminal_nodes = [8, 12]
        # 管理终端节点列表
        admin_terminal_node = [13, 18]

        # 遍历节点列表并分配设备类型
        for node in router_nodes:
            self.equipment_type[node] = 'Router'

        for node in data_center_nodes:
            self.equipment_type[node] = 'Data Center'

        for node in switch_nodes:
            self.equipment_type[node] = 'Switch'

        for node in terminal_nodes:
            self.equipment_type[node] = 'Terminal'

        for node in admin_terminal_node:
            self.equipment_type[node] = 'Admin Terminal'

    def _generate_equipment_name(self):
        # 路由器节点列表
        router_nodes = [14, 9, 19, 17, 11]
        router_models = ["Huawei AR2200", "Huawei NE20E-S", "Huawei NetEngine AR6120", "Huawei NetEngine AR6140-9G-2AC",
                         "Huawei AR2240"]

        # 数据中心节点列表及其对应的具体设备型号
        data_center_models = [
            "Huawei TaiShan 2280",
            "Dell PowerEdge R740",
            "HPE ProLiant DL380 Gen10",
            "Inspur NF5280M5",
            "Lenovo ThinkSystem SR650",
            "IBM Power System S922",
            "Huawei FusionServer Pro 2295 V5",
            "HPE Synergy 480 Gen10",
            "Inspur AS5600M5"
        ]

        data_center_nodes = [3, 15, 2, 16, 10, 5, 1, 7, 6]

        # 交换机节点列表及其对应的具体设备型号
        switch_models = ["Cisco Catalyst 3750X", "Huawei S5700"]
        switch_nodes = [10, 4]

        # 终端节点列表及其对应的具体设备型号
        terminal_models = ["HP EliteDesk 800 G6 Desktop Mini PC", "Dell OptiPlex 7070"]
        terminal_nodes = [8, 12]

        # 管理终端节点列表及其对应的具体设备型号
        admin_terminal_models = ["Lenovo ThinkPad X1 Carbon", "Lenovo ThinkPad X1 Carbon"]
        admin_terminal_node = [13, 18]

        # 遍历节点列表并分配设备类型
        for index, node in enumerate(router_nodes):
            self.equipment_name[node] = router_models[index]

        for index, node in enumerate(data_center_nodes):
            self.equipment_name[node] = data_center_models[index]

        for index, node in enumerate(switch_nodes):
            self.equipment_name[node] = switch_models[index]

        for index, node in enumerate(terminal_nodes):
            self.equipment_name[node] = terminal_models[index]

        for index, node in enumerate(admin_terminal_node):
            self.equipment_name[node] = admin_terminal_models[index]

    def _generate_equipment_status(self):
        node_id = list(self.equipment_type.keys())
        for ID in node_id:
            self.equipment_status[ID] = f"Running ({random.randint(1, 10 + int(len(node_id)/10))} days ago)"

    def _generate_equipment_suggestion(self):
        node_id = list(self.equipment_type.keys())

        for ID in node_id:
            if self.equipment_type[ID] == 'Data Center':
                self.equipment_suggestion[ID] = random.sample(self.start_suggestion, 1) + random.sample(self.DataCenter_suggestions, 3)
            elif self.equipment_type[ID] == 'Switch':
                self.equipment_suggestion[ID] = random.sample(self.start_suggestion, 1) + random.sample(self.Switch_suggestions, 3)
            elif self.equipment_type[ID] == 'Router':
                self.equipment_suggestion[ID] = random.sample(self.start_suggestion, 1) + random.sample(self.Router_suggestions, 3)
            elif self.equipment_type[ID] == 'Terminal':
                self.equipment_suggestion[ID] = random.sample(self.start_suggestion, 1) + random.sample(self.Terminal_suggestions, 3)
            elif self.equipment_type[ID] == 'Admin Terminal':
                self.equipment_suggestion[ID] = random.sample(self.start_suggestion, 1) + random.sample(self.Admin_suggestions, 3)
            else:
                raise Exception(f"Invalid equipment type {self.equipment_type[ID]}")
        for ID in node_id:
            self.equipment_suggestion[ID] = "[newline]".join(self.equipment_suggestion[ID])


if __name__ == '__main__':
    x = EquipmentMessage()
    print("end")