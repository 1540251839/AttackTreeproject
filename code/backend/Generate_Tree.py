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
                        # {"方法名称": "XXX", "描述": "XXX"}
                        # ...
                        # {"方法名称": "XXX", "描述": "XXX"}
                    ]
                },
                "电磁攻击": {
                    "TEMPEST攻击": [
                        # {"方法名称": "XXX", "描述": "XXX"}
                        # ...
                        # {"方法名称": "XXX", "描述": "XXX"}
                    ],
                    "EMP攻击": [
                        # {"方法名称": "XXX", "描述": "XXX"}
                        # ...
                        # {"方法名称": "XXX", "描述": "XXX"}
                    ]
                }
            },
            "逻辑攻击": {
                "软件攻击": {
                    "恶意软件攻击": {
                        "病毒": {
                            "文件病毒": [
                                # {"方法名称": "XXX", "描述": "XXX"}
                                # ...
                                # {"方法名称": "XXX", "描述": "XXX"}
                            ],
                            "引导区病毒": [
                                # {"方法名称": "XXX", "描述": "XXX"}
                                # ...
                                # {"方法名称": "XXX", "描述": "XXX"}
                            ]
                        },
                        "木马": {
                            "后门木马": [
                                # {"方法名称": "XXX", "描述": "XXX"}
                                # ...
                                # {"方法名称": "XXX", "描述": "XXX"}
                            ],
                            "远程访问木马": [
                                # {"方法名称": "XXX", "描述": "XXX"}
                                # ...
                                # {"方法名称": "XXX", "描述": "XXX"}
                            ]
                        }
                    },
                    "蠕虫": {
                        "网络蠕虫": [
                            # {"方法名称": "XXX", "描述": "XXX"}
                            # ...
                            # {"方法名称": "XXX", "描述": "XXX"}
                        ],
                        "电子邮件蠕虫": [
                            # {"方法名称": "XXX", "描述": "XXX"}
                            # ...
                            # {"方法名称": "XXX", "描述": "XXX"}
                        ]
                    },
                    "代码执行攻击": {
                        "缓冲区溢出": {
                            "栈溢出": [
                                # {"方法名称": "XXX", "描述": "XXX"}
                                # ...
                                # {"方法名称": "XXX", "描述": "XXX"}
                            ],
                            "堆溢出": [
                                # {"方法名称": "XXX", "描述": "XXX"}
                                # ...
                                # {"方法名称": "XXX", "描述": "XXX"}
                            ]
                        },
                        "代码注入": {
                            "SQL注入": [
                                # {"方法名称": "XXX", "描述": "XXX"}
                                # ...
                                # {"方法名称": "XXX", "描述": "XXX"}
                            ],
                            "XSS(跨站脚本攻击)": {
                                "反射性XSS": [
                                    # {"方法名称": "XXX", "描述": "XXX"}
                                    # ...
                                    # {"方法名称": "XXX", "描述": "XXX"}
                                ],
                                "存储型XSS": [
                                    # {"方法名称": "XXX", "描述": "XXX"}
                                    # ...
                                    # {"方法名称": "XXX", "描述": "XXX"}
                                ]
                            }
                        }
                    },
                    "逻辑攻击": {
                        "DoS/DDoS（拒绝服务攻击）": {
                            "流量洪泛攻击": [
                                # {"方法名称": "XXX", "描述": "XXX"}
                                # ...
                                # {"方法名称": "XXX", "描述": "XXX"}
                            ],
                            "应用层攻击": [
                                # {"方法名称": "XXX", "描述": "XXX"}
                                # ...
                                # {"方法名称": "XXX", "描述": "XXX"}
                            ]
                        },
                        "零日攻击": [
                            # {"方法名称": "XXX", "描述": "XXX"}
                            # ...
                            # {"方法名称": "XXX", "描述": "XXX"}
                        ]
                    },
                    "操作系统攻击": {
                        "特权升级": {
                            "利用内核漏洞": [
                                # {"方法名称": "XXX", "描述": "XXX"}
                                # ...
                                # {"方法名称": "XXX", "描述": "XXX"}
                            ],
                            "利用服务漏洞": [
                                # {"方法名称": "XXX", "描述": "XXX"}
                                # ...
                                # {"方法名称": "XXX", "描述": "XXX"}
                            ]
                        },
                        "服务攻击": {
                            "远程服务漏洞利用": [
                                # {"方法名称": "XXX", "描述": "XXX"}
                                # ...
                                # {"方法名称": "XXX", "描述": "XXX"}
                            ],
                            "本地服务漏洞利用": [
                                # {"方法名称": "XXX", "描述": "XXX"}
                                # ...
                                # {"方法名称": "XXX", "描述": "XXX"}
                            ]
                        },
                        "配置弱点利用": {
                            "默认账户利用": [
                                # {"方法名称": "XXX", "描述": "XXX"}
                                # ...
                                # {"方法名称": "XXX", "描述": "XXX"}
                            ],
                            "弱密码攻击": [
                                # {"方法名称": "XXX", "描述": "XXX"}
                                # ...
                                # {"方法名称": "XXX", "描述": "XXX"}
                            ]
                        }
                    },
                    "应用程序攻击": {
                        "浏览器攻击": {
                            "插件漏洞利用": [
                                # {"方法名称": "XXX", "描述": "XXX"}
                                # ...
                                # {"方法名称": "XXX", "描述": "XXX"}
                            ],
                            "浏览器扩展攻击": [
                                # {"方法名称": "XXX", "描述": "XXX"}
                                # ...
                                # {"方法名称": "XXX", "描述": "XXX"}
                            ]
                        },
                        "办公软件攻击": {
                            "宏病毒攻击": {},
                            "文件格式漏洞利用": [
                                # {"方法名称": "XXX", "描述": "XXX"}
                                # ...
                                # {"方法名称": "XXX", "描述": "XXX"}
                            ]
                        },
                        "其他应用软件攻击": {
                            "PDF阅读器攻击": [
                                # {"方法名称": "XXX", "描述": "XXX"}
                                # ...
                                # {"方法名称": "XXX", "描述": "XXX"}
                            ],
                            "多媒体播放器攻击": [
                                # {"方法名称": "XXX", "描述": "XXX"}
                                # ...
                                # {"方法名称": "XXX", "描述": "XXX"}
                            ]
                        }
                    }
                },
                "无线攻击": {
                    "Wi-Fi攻击": {
                        "WEP破解": [
                            # {"方法名称": "XXX", "描述": "XXX"}
                            # ...
                            # {"方法名称": "XXX", "描述": "XXX"}
                        ],
                        "WPA/WPA2破解": [
                            # {"方法名称": "XXX", "描述": "XXX"}
                            # ...
                            # {"方法名称": "XXX", "描述": "XXX"}
                        ],
                        "Evil Twin攻击": [
                            # {"方法名称": "XXX", "描述": "XXX"}
                            # ...
                            # {"方法名称": "XXX", "描述": "XXX"}
                        ]
                    },
                    "蓝牙攻击": {
                        "蓝牙间谍软件": [
                            # {"方法名称": "XXX", "描述": "XXX"}
                            # ...
                            # {"方法名称": "XXX", "描述": "XXX"}
                        ],
                        "蓝牙拒接服务攻击": [
                            # {"方法名称": "XXX", "描述": "XXX"}
                            # ...
                            # {"方法名称": "XXX", "描述": "XXX"}
                        ]
                    },
                    "RFID攻击": {
                        "RFID克隆": [
                            # {"方法名称": "XXX", "描述": "XXX"}
                            # ...
                            # {"方法名称": "XXX", "描述": "XXX"}
                        ],
                        "RFID中间人攻击": [
                            # {"方法名称": "XXX", "描述": "XXX"}
                            # ...
                            # {"方法名称": "XXX", "描述": "XXX"}
                        ]
                    }
                },
                "网络攻击": {
                    "中间人攻击": {
                        "ARP欺骗": [
                            # {"方法名称": "XXX", "描述": "XXX"}
                            # ...
                            # {"方法名称": "XXX", "描述": "XXX"}
                        ],
                        "DNS欺骗": [
                            # {"方法名称": "XXX", "描述": "XXX"}
                            # ...
                            # {"方法名称": "XXX", "描述": "XXX"}
                        ]
                    },
                    "IP地址欺骗": [
                        # {"方法名称": "XXX", "描述": "XXX"}
                        # ...
                        # {"方法名称": "XXX", "描述": "XXX"}
                    ],
                    "端口扫描": {
                        "TCP扫描": [
                            # {"方法名称": "XXX", "描述": "XXX"}
                            # ...
                            # {"方法名称": "XXX", "描述": "XXX"}
                        ],
                        "UDP扫描": [
                            # {"方法名称": "XXX", "描述": "XXX"}
                            # ...
                            # {"方法名称": "XXX", "描述": "XXX"}
                        ]
                    },
                    "Eavesdropping（监听）": {
                        "网络嗅探": [
                            # {"方法名称": "XXX", "描述": "XXX"}
                            # ...
                            # {"方法名称": "XXX", "描述": "XXX"}
                        ],
                        "数据包捕获": [
                            # {"方法名称": "XXX", "描述": "XXX"}
                            # ...
                            # {"方法名称": "XXX", "描述": "XXX"}
                        ]
                    }
                }
            },
            "其他攻击": {
                "供应链攻击": {
                    "硬件供应链攻击": [
                        # {"方法名称": "XXX", "描述": "XXX"}
                        # ...
                        # {"方法名称": "XXX", "描述": "XXX"}
                    ],
                    "软件供应链攻击": [
                        # {"方法名称": "XXX", "描述": "XXX"}
                        # ...
                        # {"方法名称": "XXX", "描述": "XXX"}
                    ]
                },
                "冷启动攻击": [
                    # {"方法名称": "XXX", "描述": "XXX"}
                    # ...
                    # {"方法名称": "XXX", "描述": "XXX"}
                ],
                "Rowhammer攻击": {
                    "DRAM刷新漏洞利用": [
                        # {"方法名称": "XXX", "描述": "XXX"}
                        # ...
                        # {"方法名称": "XXX", "描述": "XXX"}
                    ]
                }
            },
            "社交工程": {
                "钓鱼邮件": [
                    # {"方法名称": "XXX", "描述": "XXX"}
                    # ...
                    # {"方法名称": "XXX", "描述": "XXX"}
                ],
                "钓鱼攻击": [
                    # {"方法名称": "XXX", "描述": "XXX"}
                    # ...
                    # {"方法名称": "XXX", "描述": "XXX"}
                ],
                "开源情报搜集": [
                    # {"方法名称": "XXX", "描述": "XXX"}
                    # ...
                    # {"方法名称": "XXX", "描述": "XXX"}
                ]
            },
            "总线攻击": {
                "USB攻击": [
                    # {"方法名称": "XXX", "描述": "XXX"}
                    # ...
                    # {"方法名称": "XXX", "描述": "XXX"}
                ],
                "PCle攻击": [
                    # {"方法名称": "XXX", "描述": "XXX"}
                    # ...
                    # {"方法名称": "XXX", "描述": "XXX"}
                ]
            }
        }
    }
}


def generate_tree():
    pass
