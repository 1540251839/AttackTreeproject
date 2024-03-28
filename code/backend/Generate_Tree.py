import pprint
import random

metaACT = {
    "ACT泛攻击层可视化": {
        "攻击行为": {
            "物理攻击": {
                "硬件篡改": {
                    "硬件植入": [
                        {"方法名称": "微控制器植入", "描述": "在目标设备中植入特制的微控制器以收集数据或修改设备行为"},
                        {"方法名称": "芯片克隆", "描述": "复制合法芯片并植入后门或篡改其功能"},
                        {"方法名称": "串行设备劫持", "描述": "通过串行接口植入恶意硬件，拦截或篡改数据传输"}
                    ],
                    "JTAG攻击": [
                        {"方法名称": "JTAG接口利用", "描述": "通过JTAG接口读取或修改设备内存"},
                        {"方法名称": "调试端口访问", "描述": "利用未受保护的JTAG端口进行系统调试和代码注入"},
                        {"方法名称": "硬件级Rootkit", "描述": "在设备上植入硬件级的Rootkit，难以被检测"}
                    ]
                },
                "侧信道攻击": {
                    "功耗分析": [
                        {"方法名称": "功耗分析", "描述": "通过电源分析来评估设备的功耗"},
                        {"方法名称": "电压分析", "描述": "通过电压分析来评估设备的电压"},
                        {"方法名称": "温度分析", "描述": "通过温度分析来评估设备的温度"}
                    ],
                    "电磁分析": [
                        {"方法名称": "电磁辐射探测", "描述": "通过测量设备工作时产生的电磁辐射来收集敏感信息"},
                        {"方法名称": "电磁信号分析", "描述": "分析设备工作时产生的电磁信号特征以识别攻击点"}
                    ]
                },
                "电磁攻击": {
                    "TEMPEST攻击": [
                        {"方法名称": "信息泄露测试", "描述": "通过测量设备电磁泄露来评估信息安全性"},
                        {"方法名称": "电磁干扰注入", "描述": "通过向设备注入电磁干扰来干扰其正常功能"}
                    ],
                    "EMP攻击": [
                        {"方法名称": "电磁脉冲发生器", "描述": "使用EMP发生器产生高强度电磁脉冲以破坏电子设备"},
                        {"方法名称": "EMP武器化应用", "描述": "将EMP技术应用于武器系统，实现对电子设备的远程攻击"}
                    ]
                }
            },
            "逻辑攻击": {
                "软件攻击": {
                    "恶意软件攻击": {
                        "病毒": {
                            "文件病毒": [
                                {"方法名称": "宏病毒",
                                 "描述": "嵌入在Office文档中的恶意宏代码，通过用户执行宏来传播病毒"},
                                {"方法名称": "脚本病毒", "描述": "利用脚本语言编写的病毒，通过网页或邮件附件传播"}
                            ],
                            "引导区病毒": [
                                {"方法名称": "MBR病毒", "描述": "感染主引导记录的病毒，破坏系统启动过程"},
                                {"方法名称": "分区表病毒", "描述": "破坏硬盘分区表的病毒，导致数据丢失"}
                            ]
                            # ... 可以继续添加更多类型的病毒
                        },
                        "木马": {
                            "后门木马": [
                                {"方法名称": "Rootkit", "描述": "隐藏自身进程和文件，为攻击者提供持久化后门"},
                                {"方法名称": "RAT (远程管理工具)", "描述": "允许攻击者远程控制受害者的计算机"}
                            ],
                            "远程访问木马": [
                                {"方法名称": "VNC木马", "描述": "使用VNC协议进行远程桌面访问"},
                                {"方法名称": "RDP木马", "描述": "利用Windows远程桌面协议进行远程访问"}
                            ]
                        }
                    },
                    "蠕虫": {
                        "网络蠕虫": [
                            {"方法名称": "Nimaya蠕虫", "描述": "通过网络共享和邮件传播，消耗网络资源"},
                            {"方法名称": "Conficker蠕虫", "描述": "感染Windows系统，利用漏洞传播并下载恶意软件"}
                        ],
                        "电子邮件蠕虫": [
                            {"方法名称": "Sobig蠕虫", "描述": "通过电子邮件附件传播，窃取用户信息"},
                            {"方法名称": "Mydoom蠕虫", "描述": "通过垃圾邮件和网络共享传播，形成僵尸网络"}
                        ]
                    },

                    "代码执行攻击": {
                        "缓冲区溢出": {
                            "栈溢出": [
                                {"方法名称": "格式化字符串溢出", "描述": "通过格式化字符串函数漏洞执行任意代码"},
                                {"方法名称": "返回地址覆盖", "描述": "覆盖函数调用栈上的返回地址，重定向执行流程"}
                            ],
                            "堆溢出": [
                                {"方法名称": "堆喷射", "描述": "在堆上大量分配包含特定内容的块，以利用溢出时的地址预测"},
                                {"方法名称": "Use-after-free", "描述": "释放内存后继续使用，导致内存损坏或代码执行"}
                            ]
                        },
                        "代码注入": {
                            "SQL注入": [
                                {"方法名称": "盲注", "描述": "通过数据库返回信息的差异来判断注入是否成功，提取敏感数据"},
                                {"方法名称": "联合查询注入", "描述": "利用SQL查询的联合特性，执行多个查询以获取更多信息"}
                            ],
                            "XSS(跨站脚本攻击)": {
                                "反射性XSS": [
                                    {"方法名称": "URL编码绕过", "描述": "通过URL编码绕过前端过滤，注入恶意脚本"},
                                    {"方法名称": "利用JavaScript事件",
                                     "描述": "在输入中嵌入JavaScript事件来触发恶意代码"}
                                ],
                                "存储型XSS": [
                                    {"方法名称": "留言板注入", "描述": "在网站留言板等用户可编辑内容中注入恶意脚本"},
                                    {"方法名称": "数据库污染",
                                     "描述": "污染数据库中的存储内容，使得所有浏览相关内容的用户都会受到攻击"}
                                ]
                            }
                        }
                    },
                    "逻辑攻击": {
                        "DoS/DDoS（拒绝服务攻击）": {
                            "流量洪泛攻击": [
                                {"方法名称": "SYN Flood",
                                 "描述": "通过发送大量的SYN请求来耗尽服务器的资源，使服务器无法处理正常的连接请求。"},
                                {"方法名称": "ICMP Flood",
                                 "描述": "通过发送大量的ICMP请求来制造网络拥塞，使目标系统无法正常响应。"},
                                {"方法名称": "UDP Flood",
                                 "描述": "发送大量的UDP数据包到目标系统，由于UDP是无连接的协议，服务器会消耗大量资源处理这些无效的数据包。"}
                            ],
                            "应用层攻击": [
                                {"方法名称": "HTTP Flood",
                                 "描述": "发送大量的HTTP请求到目标Web服务器，导致服务器过载，无法正常服务其他用户。"},
                                {"方法名称": "Slowloris",
                                 "描述": "通过保持多个半开的HTTP连接来耗尽服务器的连接资源，使得其他正常请求无法被处理。"}
                            ]
                        },
                        "零日攻击": [
                            {"方法名称": "利用未公开漏洞",
                             "描述": "攻击者利用软件或系统中尚未被公众发现的漏洞，执行恶意代码或获取敏感信息。"}
                        ]
                    },
                    "操作系统攻击": {
                        "特权升级": {
                            "利用内核漏洞": [
                                {"方法名称": "本地提权",
                                 "描述": "通过利用内核漏洞，攻击者可以提升自己的权限等级，从而获得更高的系统访问权限。"},
                                {"方法名称": "远程提权",
                                 "描述": "通过网络攻击手段，如远程执行恶意代码或利用远程服务漏洞，攻击者可以提升远程主机的权限。"}
                            ],
                            "利用服务漏洞": [
                                {"方法名称": "利用软件漏洞",
                                 "描述": "攻击者利用软件的漏洞，如未打补丁的软件、配置不当的服务等，进行非法操作或获取敏感信息。"},
                                {"方法名称": "利用逻辑错误",
                                 "描述": "利用程序中存在的逻辑错误或缺陷，如缓冲区溢出、输入验证绕过等，实施恶意操作。"}
                            ]
                        },
                        "服务攻击": {
                            "远程服务漏洞利用": [
                                {"方法名称": "远程执行代码",
                                 "描述": "通过利用远程服务的漏洞，攻击者在目标系统上远程执行恶意代码。"},
                                {"方法名称": "远程数据窃取",
                                 "描述": "攻击者利用远程服务漏洞，获取目标系统的敏感数据或个人信息。"}
                            ],
                            "本地服务漏洞利用": [
                                {"方法名称": "本地特权提升",
                                 "描述": "攻击者在目标系统的本地环境中利用服务漏洞，提升自身权限。"},
                                {"方法名称": "本地数据泄露",
                                 "描述": "攻击者在目标系统的本地环境中泄露敏感数据或个人信息。"}
                            ]
                        },
                        "配置弱点利用": {
                            "默认账户利用": [
                                {"方法名称": "使用默认账户密码",
                                 "描述": "攻击者利用系统或服务提供的默认账户和密码进行登录和攻击。"},
                                {"方法名称": "暴力破解账户密码",
                                 "描述": "攻击者尝试使用各种方式暴力破解目标系统的账户密码。"}
                            ],
                            "弱密码攻击": [
                                {"方法名称": "常见密码攻击", "描述": "攻击者利用常见的密码组合进行尝试登录。"},
                                {"方法名称": "字典攻击", "描述": "攻击者使用预定义的字典中的密码进行尝试登录。"}
                            ]
                        }
                    },
                    "应用程序攻击": {
                        "浏览器攻击": {
                            "插件漏洞利用": [
                                {"方法名称": "利用过时插件漏洞",
                                 "描述": "攻击者利用目标系统中过时的浏览器插件漏洞，执行恶意操作或获取敏感信息。"},
                                {"方法名称": "利用未打补丁的插件漏洞",
                                 "描述": "攻击者利用目标系统未打补丁的浏览器插件漏洞，进行非法操作或数据窃取。"}
                            ],
                            "浏览器扩展攻击": [
                                {"方法名称": "利用扩展程序漏洞",
                                 "描述": "攻击者利用目标系统中安装的浏览器扩展程序的漏洞，执行恶意操作或获取敏感信息。"},
                                {"方法名称": "钓鱼链接诱导安装恶意扩展程序",
                                 "描述": "攻击者通过钓鱼链接诱骗用户点击并安装恶意扩展程序，从而控制用户的浏览器并执行恶意操作。"}
                            ]
                        },
                        "办公软件攻击": {
                            "宏病毒攻击":
                                [
                                    {"方法名称": "利用宏病毒传播恶意软件",
                                     "描述": "攻击者利用宏病毒在目标系统中传播恶意软件，如勒索软件、间谍软件等。"}
                                ]
                            ,
                            "文件格式漏洞利用": [
                                {"方法名称": "利用文件解析漏洞",
                                 "描述": "攻击者利用目标系统的文件解析漏洞，如解析引擎漏洞、文件处理漏洞等，执行恶意代码或造成其他危害。"},
                                {"方法名称": "利用文件执行漏洞",
                                 "描述": "攻击者利用目标系统的文件执行漏洞，如在某些情况下可执行特定类型的文件，执行恶意代码或造成其他危害。"}
                            ]
                        },
                        "其他应用软件攻击": {
                            "PDF阅读器攻击": [
                                {"方法名称": "利用PDF漏洞执行恶意代码",
                                 "描述": "攻击者利用目标系统的PDF阅读器漏洞，执行恶意代码或造成其他危害。"},
                                {"方法名称": "钓鱼链接诱导下载恶意附件",
                                 "描述": "攻击者通过钓鱼链接诱骗用户下载恶意附件，如包含恶意软件的压缩包、图片等，从而实施攻击。"}
                            ],
                            "多媒体播放器攻击": [
                                {"方法名称": "利用媒体播放器漏洞执行恶意代码",
                                 "描述": "攻击者利用目标系统的媒体播放器漏洞，执行恶意代码或造成其他危害。"},
                                {"方法名称": "钓鱼链接诱导下载恶意媒体文件",
                                 "描述": "攻击者通过钓鱼链接诱骗用户下载恶意媒体文件，如恶意软件捆绑的音乐、视频等，从而实施攻击。"}
                            ]
                        }
                    }
                },
                "无线攻击": {
                    "Wi-Fi攻击": {
                        "WEP破解": [
                            {"方法名称": "穷举攻击", "描述": "通过穷举可能的密钥进行破解"},
                            {"方法名称": "字典攻击", "描述": "利用预先生成的密码字典进行破解"},
                            {"方法名称": "重放攻击", "描述": "截获并重放加密的数据包以获得密钥"}
                        ],
                        "WPA/WPA2破解": [
                            {"方法名称": "暴力破解", "描述": "通过穷举可能的密码组合进行破解"},
                            {"方法名称": "彩虹表攻击", "描述": "使用预先计算好的彩虹表进行破解"},
                            {"方法名称": "握手包攻击", "描述": "截获加密握手包，通过离线破解获取密钥"}
                        ],
                        "Evil Twin攻击": [
                            {"方法名称": "无线钓鱼", "描述": "伪装成合法的Wi-Fi网络，诱使用户连接并泄露信息"},
                            {"方法名称": "中间人攻击", "描述": "截获用户数据流量，实施窃听或篡改数据"}
                        ]
                    },
                    "蓝牙攻击": {
                        "蓝牙间谍软件": [
                            {"方法名称": "蓝牙监听", "描述": "监听蓝牙通信以窃取敏感信息"},
                            {"方法名称": "数据嗅探", "描述": "嗅探蓝牙数据包，分析其中的内容"}
                        ],
                        "蓝牙拒接服务攻击": [
                            {"方法名称": "蓝牙干扰", "描述": "发送干扰信号使目标设备无法正常连接蓝牙网络"},
                            {"方法名称": "蓝牙瘫痪", "描述": "发送大量的无效蓝牙请求，使目标设备过载"}
                        ]
                    },
                    "RFID攻击": {
                        "RFID克隆": [
                            {"方法名称": "RFID复制", "描述": "读取合法RFID卡信息并复制到另一张卡上"},
                            {"方法名称": "RFID模拟", "描述": "模拟合法RFID卡的信号，欺骗读卡器"}
                        ],
                        "RFID中间人攻击": [
                            {"方法名称": "RFID数据中继",
                             "描述": "中间人在合法用户和读卡器之间传递数据，窃取信息或篡改数据"}
                        ]
                    }
                },
                "网络攻击": {
                    "中间人攻击": {
                        "ARP欺骗": [
                            {"方法名称": "ARP缓存投毒", "描述": "发送伪造的ARP响应，欺骗目标主机与中间人通信"},
                            {"方法名称": "ARP欺骗中继", "描述": "转发收到的ARP请求和响应，中间人窃取通信内容"}
                        ],
                        "DNS欺骗": [
                            {"方法名称": "DNS响应劫持", "描述": "伪造DNS响应，将合法域名解析至恶意IP地址"},
                            {"方法名称": "DNS投毒", "描述": "在DNS服务器和客户端之间插入虚假DNS响应"}
                        ]
                    },
                    "IP地址欺骗": [
                        {"方法名称": "IP欺骗", "描述": "伪造IP地址，使通信的源地址或目的地址被欺骗"}
                    ],
                    "端口扫描": {
                        "TCP扫描": [
                            {"方法名称": "全连接扫描", "描述": "尝试建立完整的TCP连接以确定端口是否开放"},
                            {"方法名称": "SYN扫描", "描述": "发送TCP SYN包，根据响应确定端口是否开放"},
                            {"方法名称": "FIN扫描", "描述": "发送TCP FIN包，根据响应确定端口是否开放"}
                        ],
                        "UDP扫描": [
                            {"方法名称": "UDP扫描", "描述": "发送UDP包，根据响应确定端口是否开放"}
                        ]
                    },
                    "Eavesdropping（监听）": {
                        "网络嗅探": [
                            {"方法名称": "数据包嗅探", "描述": "监视网络上的数据包，窃取通信内容"},
                            {"方法名称": "流量分析", "描述": "分析网络流量模式和特征，获取敏感信息"}
                        ],
                        "数据包捕获": [
                            {"方法名称": "数据包捕获", "描述": "截获传输在网络上的数据包，分析其中的内容"}
                        ]
                    }
                }
            },
            "其他攻击": {
                "供应链攻击": {
                    "硬件供应链攻击": [
                        {"方法名称": "硬件后门植入", "描述": "在硬件设备中植入后门，用于未经授权的访问或控制"},
                        {"方法名称": "硬件假冒", "描述": "伪装成合法硬件并混入供应链，用于执行恶意操作"}
                    ],
                    "软件供应链攻击": [
                        {"方法名称": "恶意代码注入", "描述": "将恶意代码注入软件更新或发布的流程中，感染终端用户"},
                        {"方法名称": "篡改软件包", "描述": "篡改软件分发渠道中的软件包，植入恶意代码"}
                    ]
                },
                "冷启动攻击": [
                    {"方法名称": "内存数据窃取", "描述": "利用计算机在冷启动过程中未加密的内存数据，窃取敏感信息"},
                    {"方法名称": "加密密钥泄露", "描述": "通过冷启动攻击获取加密密钥，导致加密数据的泄露"}
                ],
                "Rowhammer攻击": {
                    "DRAM刷新漏洞利用": [
                        {"方法名称": "Rowhammer攻击", "描述": "利用DRAM中不同行之间的电荷泄漏现象，修改相邻内存位的内容"}
                    ]
                }
            },
            "总线攻击": {
                "USB攻击": [
                    {"方法名称": "USB恶意设备", "描述": "通过USB接口连接恶意设备，执行未经授权的操作"},
                    {"方法名称": "USB钓鱼攻击", "描述": "将USB设备伪装成合法设备，诱骗用户连接并执行恶意操作"}
                ],
                "PCle攻击": [
                    {"方法名称": "PCle硬件窃取", "描述": "利用PCI Express总线进行数据窃取或植入恶意代码"},
                    {"方法名称": "PCle固件篡改", "描述": "通过PCle接口篡改固件，以执行未经授权的操作"}
                ]
            }
        },
        "社交工程": {
            "钓鱼邮件": [
                {"方法名称": "伪装成合法邮件", "描述": "伪装成合法的邮件，诱使用户点击恶意链接或下载恶意附件"},
                {"方法名称": "欺骗性内容", "描述": "通过欺骗性的内容引诱用户点击链接、提供个人信息或执行恶意操作"}
            ],
            "钓鱼攻击": [
                {"方法名称": "社交媒体欺骗", "描述": "在社交媒体平台上通过虚假账号发送欺骗性信息，诱导用户执行恶意操作"},
                {"方法名称": "伪装身份", "描述": "伪装成受信任的个人、组织或机构，以获取目标信任并实施攻击"}
            ],
            "开源情报搜集": [
                {"方法名称": "信息收集", "描述": "通过开源情报搜集各种信息，包括目标系统、组织架构、个人信息等"}
            ]
        }
    }
}


class Node:
    """
    节点类，用于构建树结构中的每个节点。

    参数:
    - contents: 节点包含的内容。
    - ID: 节点的唯一标识。
    - father_id: 父节点的标识，默认为None。
    - sons_id: 子节点的标识列表，默认为None，初始化为空列表。
    """

    def __init__(self, contents, ID, depth, father_id=None, sons_id=None, nodeType='None-leaf'):
        assert nodeType in ['None-leaf', 'leaf'], "nodeType must in 'None-leaf', 'leaf', got {}".format(nodeType)
        if sons_id is None:
            sons_id = []
        self.contents = contents
        self.sons_id = sons_id
        self.father_id = father_id
        self.id = ID
        self.nodeType = nodeType
        self.depth = depth
        self.offspring_id = []


class MetaACT:
    """
    MetaACT类，用于管理和生成基于metaACT数据的树结构。

    属性:
    - metaData: 存储原始metaACT数据。
    - Nodes: 存储生成的节点对象列表。
    - cur_max_node_ID: 当前最大的节点ID，用于生成唯一ID。
    """

    def __init__(self):
        """
        初始化MetaACT类实例，创建根节点并生成初始的树结构。
        """
        self.metaData = metaACT  # 原始metaACT数据存储
        self.depth_count = {}  # 用于存储树的深度计数
        self.Nodes = []  # 节点对象列表存储
        self.cur_max_node_ID = 0  # 当前最大节点ID，用于生成唯一ID
        self.neg2Nodes_id = []  # 存储特定ID的节点列表
        self.sample_neg2Nodes_id = []  # 示例节点ID列表
        self._generate_node_from_metaACT()  # 从metaACT数据生成节点
        self.format_json_tree = self._generate_format_json_tree(curNode=self._fetch_node_by_id(0))  # 生成格式化的JSON树结构
        self.format_json_tree_sample = None  # 存储示例格式化的JSON树结构

        # 检查节点ID位置是否正确
        for index, node in enumerate(self.Nodes):
            if index != node.id:
                raise Exception("Node ID position error")

    @staticmethod
    def _check_common_in_list(ListA, ListB):
        """
        检查两个列表是否有共同元素。

        参数:
        - ListA: 第一个列表。
        - ListB: 第二个列表。

        返回值:
        - True: 如果两个列表有至少一个共同元素。
        - False: 如果两个列表没有共同元素。
        """
        return len(set(ListA) & set(ListB)) > 0

    def _count_depth(self, depth):
        """
        统计树中指定深度的节点数量。

        参数:
        - depth: 节点的深度。
        """
        # 如果指定深度未被记录，则初始化计数为0
        if depth not in self.depth_count:
            self.depth_count[depth] = 0
        self.depth_count[depth] += 1  # 深度计数加一


    def _fetch_node_by_id(self, ID) -> Node:
        """
        根据ID查找并返回节点。

        参数:
        - ID: 要查找的节点ID。

        返回:
        - 找到的节点对象。

        异常:
        - 如果ID不存在于树中，抛出异常。
        """
        if self.Nodes[ID].id == ID:
            return self.Nodes[ID]
        raise Exception(f"No such ID {ID} in Tree!!! maybe something went wrong with Node ID and its position")

    def _generate_father_son_relationships_with_dfs(self, curTree, curNode, depth):
        """
        使用深度优先搜索生成节点间的父子关系。

        参数:
        - curTree: 当前遍历的树结构（字典形式）。
        - curNode: 当前节点对象。
        """
        for key, value in curTree.items():

            # 递归处理子字典，构建父子节点关系
            sonNode = Node(
                contents=key,
                ID=self.cur_max_node_ID,
                father_id=curNode.id,
                depth=depth
            )
            self._count_depth(depth)
            curNode.sons_id.append(sonNode.id)
            self.Nodes.append(sonNode)
            self.cur_max_node_ID += 1
            if isinstance(value, dict):
                self._generate_father_son_relationships_with_dfs(curTree=value, curNode=sonNode, depth=depth + 1)
            else:
                # 处理叶子节点，构建父子节点关系
                self.neg2Nodes_id.append(sonNode.id)
                for instance in value:
                    assert isinstance(instance, dict), f'invalid instance: {instance}| value:{value}'
                    sonNode1 = Node(
                        contents=instance["方法名称"],
                        ID=self.cur_max_node_ID,
                        father_id=sonNode.id,
                        nodeType='leaf',
                        depth=depth + 1
                    )
                    self._count_depth(depth + 1)
                    sonNode.sons_id.append(sonNode1.id)
                    self.Nodes.append(sonNode1)
                    self.cur_max_node_ID += 1

    def _generate_node_from_metaACT(self):
        """
        根据metaACT数据生成节点树。

        使用方法:
        - 遍历原始数据，创建根节点并添加到Nodes列表。
        - 递归处理metaACT数据，构建整个树的父子关系。
        """
        rootNode = Node(
            contents=list(metaACT.keys())[0],
            ID=self.cur_max_node_ID,
            depth=0
        )
        self._count_depth(0)
        self.cur_max_node_ID += 1
        self.Nodes.append(rootNode)
        self._generate_father_son_relationships_with_dfs(curTree=metaACT[rootNode.contents], curNode=rootNode, depth=1)

    def _generate_format_json_tree(self, curNode: Node):
        """
        根据当前节点生成格式化的JSON树结构。

        参数:
        - curNode: 当前处理的节点对象。

        返回:
        - 格式化的JSON树结构（字典形式）。
        """
        curTree = {
            "name": curNode.contents,
            "children": [],
            'value': random.randint(1, 100) / 100
        }
        for son_ID in curNode.sons_id:
            curTree['children'].append(self._generate_format_json_tree(curNode=self._fetch_node_by_id(ID=son_ID)))
            self.Nodes[curNode.id].offspring_id += self.Nodes[son_ID].offspring_id + [son_ID]
        return curTree

    def _generate_sampled_json_tree(self, curNode: Node):
        """
        根据当前节点生成格式化的JSON树结构。

        参数:
        - curNode: 当前处理的节点对象。

        返回:
        - 格式化的JSON树结构（字典形式）。
        """
        if (self._check_common_in_list(curNode.offspring_id + [curNode.id],
                                       self.sample_neg2Nodes_id) is False) and (curNode.nodeType != 'leaf'):
            return -1
        curTree = {
            "name": curNode.contents,
            "children": [],
            'value': random.randint(1, 100) / 100
        }
        for son_ID in curNode.sons_id:
            sonTree = self._generate_sampled_json_tree(curNode=self._fetch_node_by_id(ID=son_ID))
            if sonTree is not -1:
                curTree['children'].append(sonTree)
        return curTree

    def Sample_neg2Nodes_id(self, sed=None):
        """
        从neg2Nodes_id中采样节点id，不重复。
        :param sed: 可选参数，如果提供，则用作随机数生成器的种子，确保结果可复现。
        :return: 无返回值，但会修改实例变量sample_neg2Nodes_id和format_json_tree_sample。
        """

        # 如果提供了sed参数，则设置随机数种子
        if sed is not None:
            random.seed(sed)

        self.sample_neg2Nodes_id = []
        # 遍历neg2Nodes_id列表
        for i in self.neg2Nodes_id:
            if random.randint(1, 1000) / 1000 < 0.2:  # 选择节点
                self.sample_neg2Nodes_id.append(i)

        # 生成并设置格式化的采样json树结构
        self.format_json_tree_sample = self._generate_sampled_json_tree(curNode=self.Nodes[0])


if __name__ == "__main__":
    metaACT = MetaACT()
    metaACT.Sample_neg2Nodes_id(112)
    pprint.pprint(metaACT.format_json_tree_sample)
    print("end")
