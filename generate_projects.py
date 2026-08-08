#!/usr/bin/env python3
"""Generate 15 project detail pages for the portfolio multi-page site."""

import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "projects")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Project order for prev/next navigation
PROJECT_ORDER = [
    "sunon-chicago", "ancient-carnival", "art-exhibition", "twin-city",
    "china-cultural-day", "film-week", "fashion-week", "happy-institute",
    "geely", "young-entrepreneurs", "dcf-dinner", "education-bureau",
    "mexico-tourism", "county-culture", "alibaba"
]

# Category display names
CAT_NAMES = {
    "exhibition": "展会类活动",
    "performance": "演出类活动",
    "conference": "会议类活动",
    "procurement": "活动采购工作"
}

# All project data
PROJECTS = {
    "sunon-chicago": {
        "title": "圣奥 Sunon 芝加哥展厅开幕活动",
        "subtitle": "Fulton Market Design Days x NeoCon 2025",
        "category": "exhibition",
        "time": "2025.06.09 - 06.11",
        "location": "美国 芝加哥 Fulton Market",
        "company": "独立执行",
        "tags": ["展厅开幕", "北美市场", "Co-Design Workshop"],
        "sections": [
            {
                "title": "项目背景",
                "paragraphs": [
                    "圣奥（Sunon）是中国办公家具行业头部品牌，近年加速北美市场拓展。2025 年 6 月，圣奥在芝加哥 Fulton Market 区开设全美第二座展厅（面积约 1,200 平方英尺），选址于芝加哥设计产业核心地段，紧邻 NeoCon（北美最大商业设计展）举办地 Mart。展厅开幕活动定于 6 月 9-11 日，与 Fulton Market Design Days 及 NeoCon 2025 同期，以最大化设计行业客流曝光。",
                    "展厅展出三条核心产品线：H7 人体工学椅（主打自适应腰部支撑）、MixCube 模块化办公系统（面向灵活办公场景）、H5 回收海洋塑料椅（体现 ESG 可持续战略）。活动期间还设有 Co-Design Workshop 环节，邀请设计师与客户参与产品共创体验。"
                ]
            },
            {
                "title": "执行内容",
                "paragraphs": [
                    "作为展厅开幕活动执行团队成员，主要负责以下环节：",
                ],
                "list": [
                    "现场协调：统筹活动三天（6/9-6/11）的展厅开放时段管理，协调展厅导览流程与 VIP 客户专属接待安排",
                    "嘉宾接待流程：负责设计行业 KOL、企业客户及媒体代表的到场登记、导览引导与体验安排",
                    "Co-Design Workshop 落地：组织 Workshop 场次排期、物料准备与现场互动引导，确保参与者完成从产品体验到共创反馈的完整闭环",
                    "NeoCon 客流对接：在 NeoCon 展会期间协调展厅接驳安排，引导展会客流到 Fulton Market 展厅参观体验",
                    "现场突发应对：处理嘉宾行程临时变动、设备调试、物料补充等现场问题"
                ]
            },
            {
                "title": "项目亮点",
                "paragraphs": [
                    "活动成功对接 NeoCon 2025 设计行业客流，展厅开放期间接待来自美国、加拿大、墨西哥等地的设计师与企业客户。Co-Design Workshop 环节获得参与者正面反馈，为圣奥北美市场品牌认知与客户线索积累提供了直接触点。展厅作为长期品牌展示空间，在活动后持续运营，成为圣奥在芝加哥的设计行业据点。"
                ]
            }
        ],
        "highlights": [
            {"number": "1,200", "label": "sqm 展厅面积"},
            {"number": "3", "label": "天活动周期"},
            {"number": "3", "label": "核心产品线展示"},
            {"number": "NeoCon", "label": "客流对接"}
        ],
        "images": []
    },

    "ancient-carnival": {
        "title": "墨尔本古风嘉年华",
        "subtitle": "中澳跨文化集市 + 国风展演",
        "category": "exhibition",
        "time": "2023.05 - 2023.10",
        "location": "澳大利亚 墨尔本",
        "company": "DCF Property 期间",
        "tags": ["全案策划", "跨境清关", "招商运营", "双语传播"],
        "sections": [
            {
                "title": "项目背景",
                "paragraphs": [
                    "墨尔本古风嘉年华是面向本地华人社区与澳洲主流社会的跨文化集市活动，以\"古风 + 跨文化融合\"为主题，融合传统国风展演与集市体验。活动选址墨尔本核心商圈，旨在通过沉浸式文化体验推动中澳民间文化交流，同时为参展商家提供品牌曝光与销售转化渠道。"
                ]
            },
            {
                "title": "策划与执行",
                "paragraphs": [
                    "独立负责活动全案策划与落地执行，工作覆盖以下环节：",
                ],
                "list": [
                    "展区规划：设计主舞台区、文化体验区、美食集市区、商家展销区四大功能分区，规划观众动线与驻留节点",
                    "预算编制：拆解场地租赁、物料制作、演艺人员、设备租赁、安保等成本项，编制全案预算并控制实际执行偏差",
                    "合规与风险预案：对接墨尔本市议会获取活动许可，编制突发事件应急预案（天气、人群拥堵、设备故障等）",
                    "招商运营：独立完成 35 家商家招商签约，签约率 100%，覆盖餐饮、文创、手作、服饰等品类",
                    "跨境物流：统筹国内活动物料跨境运输与澳洲海关清关，确保物料按时到场",
                    "现场执行：活动期间现场接待超 5,000 人次，零安全事故、零合规投诉"
                ]
            },
            {
                "title": "传播与成果",
                "paragraphs": [
                    "搭建中英双语传播渠道（微信公众号 + 小红书 + Facebook），活动期间累计触达约 20 万人次。活动登上墨尔本华人社交平台热榜，获得本地媒体自发报道。活动结束后完成完整复盘报告，为后续活动迭代提供数据支撑。"
                ]
            }
        ],
        "highlights": [
            {"number": "5,000+", "label": "现场接待人次"},
            {"number": "35", "label": "家商家签约 (100%)"},
            {"number": "20万", "label": "传播触达"},
            {"number": "0", "label": "安全事故 / 合规投诉"}
        ],
        "images": []
    },

    "art-exhibition": {
        "title": "墨韵华光：中澳雅集共潮生",
        "subtitle": "当代艺术展 + 非遗对话 + IP 孵化",
        "category": "exhibition",
        "time": "2025.10",
        "location": "墨尔本 澳华历史博物馆",
        "company": "DCF Property 期间",
        "tags": ["策展规划", "非遗文化", "IP 孵化", "慈善拍卖"],
        "sections": [
            {
                "title": "项目背景",
                "paragraphs": [
                    "墨韵华光是设在墨尔本澳华历史博物馆（Museum of Chinese Australian History）的当代艺术展览，以中澳文化对话为核心叙事。展览旨在通过多元艺术形式呈现中澳文化的交融与共生，同时推动中国非遗工艺与文创 IP 在澳洲市场的认知与传播。"
                ]
            },
            {
                "title": "策展规划",
                "paragraphs": [
                    "负责策展方案撰写与五大展区规划：",
                ],
                "list": [
                    "中澳儿童画展（\"童绘邮记\"）：展出中澳儿童以\"我眼中的两国文化\"为主题的绘画作品，设置互动邮递墙",
                    "艺术家作品联展（\"艺境双生\"）：邀请中澳当代艺术家联合展出，呈现跨文化创作对话",
                    "中澳非遗工艺展（\"非遗活色\"）：展示漆器、丝绸、陶瓷等非遗工艺，设现场制作演示",
                    "中澳生活方式展：呈现两国家居、茶道、花艺等生活方式的对比与融合",
                    "中国 IP 潮玩与文创专场：展出中国潮玩品牌与文创衍生品，探索 IP 出海路径"
                ]
            },
            {
                "title": "互动与传播",
                "paragraphs": [
                    "设置慈善拍卖环节，拍卖部分参展艺术品，收益捐赠中澳文化交流公益项目。引入现场人气投票机制，观众可为自己喜欢的作品投票，提升参与度与二次传播。展览期间组织多场导览活动与文化沙龙，邀请艺术家、非遗传承人与观众面对面交流。"
                ]
            }
        ],
        "highlights": [
            {"number": "5", "label": "大展区"},
            {"number": "4", "label": "条内容线"},
            {"number": "1", "label": "场慈善拍卖"},
            {"number": "100%", "label": "策展方案独立撰写"}
        ],
        "images": [
            {"src": "../assets/art_exhibition/page_1.png", "caption": "墨韵华光展览策展方案封面", "full": True},
            {"src": "../assets/art_exhibition/page_4.png", "caption": "展区规划与动线设计"},
            {"src": "../assets/art_exhibition/page_6.png", "caption": "非遗工艺展与互动环节设计"}
        ]
    },

    "twin-city": {
        "title": "墨尔本双城对话画展",
        "subtitle": "官方文化交流 + 政企联动",
        "category": "exhibition",
        "time": "2023.09 - 2024.01",
        "location": "澳大利亚 墨尔本",
        "company": "DCF Property 期间",
        "tags": ["政企对接", "跨境运输", "官方接待", "媒体报道"],
        "sections": [
            {
                "title": "项目背景",
                "paragraphs": [
                    "墨尔本双城对话画展是中澳两地政府部门联合发起的官方文化交流项目，以\"苏州园林文化 + 墨尔本多元艺术\"为策展主题，旨在通过艺术展览推动两座城市之间的文化互鉴与民间交流。活动属于中澳官方文化交流框架下的重点项目。"
                ]
            },
            {
                "title": "执行内容",
                "paragraphs": [
                    "在项目中承担以下职责：",
                ],
                "list": [
                    "主题策划：联合中澳两地政府部门确定\"苏州园林文化 + 墨尔本多元艺术\"策展主题，协调双方对展览内容的预期",
                    "跨境运输：负责参展作品从中国到澳大利亚的跨境安全运输与海关清关，确保作品完好到场",
                    "展区布置：规划展区动线、灯光设计与作品陈列方案，协调澳方场地方完成布展",
                    "官方嘉宾接待：编制官方嘉宾接待流程，协调接待规格、礼仪安排与行程衔接",
                    "媒体协调：对接新华社、澳洲 ABC 中文网等中澳主流媒体到场报道，提供新闻素材与采访安排"
                ]
            },
            {
                "title": "项目成果",
                "paragraphs": [
                    "活动期间零礼仪疏漏、零合规风险，获得中澳双方政府部门认可。新华社与 ABC 中文网均发布了活动报道，有效提升了活动的传播覆盖面。展览结束后，参展作品全部安全回运，无损坏记录。"
                ]
            }
        ],
        "highlights": [
            {"number": "2", "label": "国政府部门联动"},
            {"number": "0", "label": "礼仪疏漏 / 合规风险"},
            {"number": "100%", "label": "作品安全回运"},
            {"number": "2+", "label": "主流媒体报道"}
        ],
        "images": []
    },

    "china-cultural-day": {
        "title": "中国文化日 / 中国非遗文化嘉年华",
        "subtitle": "CMG x 澳大利亚网球公开赛",
        "category": "exhibition",
        "time": "澳网期间",
        "location": "墨尔本 AO 场地周边",
        "company": "跨机构合作",
        "tags": ["体育赛事", "非遗展示", "品牌出海", "互动体验"],
        "sections": [
            {
                "title": "项目背景",
                "paragraphs": [
                    "在中央广播电视总台（CMG）与澳大利亚网球公开赛（Australian Open）合作框架下，策划为期两天的非遗文化嘉年华。活动设在澳网场地周边，利用赛事流量实现中国文化在体育赛事场景下的出海展示，是\"体育 + 文化 + 商业\"融合的典型场景。"
                ]
            },
            {
                "title": "展区规划",
                "paragraphs": [
                    "负责展区规划与落地执行，设置四大展区：",
                ],
                "list": [
                    "文化展区：漆扇、烧箔画、螺钿镶嵌、绒花等非遗工艺展示与现场体验",
                    "美食展区：吹糖人、糖画、龙须酥等传统手作美食现场制作",
                    "品牌展区：中国品牌出海展示与产品体验",
                    "表演展区：T 台秀、机器人与无人机表演、网球灯笼墙打卡等互动形式"
                ]
            },
            {
                "title": "执行亮点",
                "paragraphs": [
                    "在体育赛事场景下完成文化出海展示，将非遗工艺、传统美食与现代科技互动结合，吸引大量澳网观众驻足参与。网球灯笼墙打卡环节成为社交媒体自发传播热点，有效扩大了活动的二次传播覆盖面。"
                ]
            }
        ],
        "highlights": [
            {"number": "2", "label": "天活动周期"},
            {"number": "4", "label": "大功能区"},
            {"number": "AO", "label": "赛事客流"},
            {"number": "CMG", "label": "合作框架"}
        ],
        "images": [
            {"src": "../assets/china_cultural_day/page_1.png", "caption": "中国文化日活动策划方案", "full": True},
            {"src": "../assets/china_cultural_day/page_5.png", "caption": "展区规划与动线设计"},
            {"src": "../assets/china_cultural_day/page_12.png", "caption": "互动体验与传播方案"}
        ]
    },

    "film-week": {
        "title": "中国国际电影周（维州中国电影周）",
        "subtitle": "中国驻墨尔本总领事馆主办",
        "category": "performance",
        "time": "2022.07-10 / 2024.09",
        "location": "塔斯马尼亚 / 墨尔本",
        "company": "领事馆合作",
        "tags": ["版权授权", "领事馆对接", "媒体传播", "影片展映"],
        "sections": [
            {
                "title": "项目背景",
                "paragraphs": [
                    "中国国际电影周（维州中国电影周）由中国驻墨尔本总领事馆主办，旨在通过中国电影展映推动中澳文化交流与影视互鉴。活动覆盖开幕式、影片展映、行业论坛等核心环节，是领区内年度重点文化活动。"
                ]
            },
            {
                "title": "策划与执行",
                "paragraphs": [
                    "联合总领事馆策划两届电影周活动，负责以下环节：",
                ],
                "list": [
                    "开幕式流程设计：编排开幕式议程、嘉宾致辞环节、影片开幕放映流程",
                    "影片展映排期：协调 7 部影片的展映场次安排，确保排片均衡与观众覆盖",
                    "版权授权沟通：完成 7 部影片的版权授权沟通、格式适配（DCP 转换等）与跨境运输清关",
                    "行业论坛：策划中澳影视行业论坛环节，协调嘉宾出席与议题设置",
                    "现场放映统筹：统筹 1,000+ 人现场放映，7 天 8 场展映零放映事故"
                ]
            },
            {
                "title": "2024 年维州中国电影周",
                "paragraphs": [
                    "2024 年维州中国电影周在本迭戈（Bendigo）举办，展映《热辣滚烫》《封神第一部》《长安三万里》《孤注一掷》《志愿军：雄兵出击》《满江红》《流浪地球 2》等 7 部影片。活动获新华社、ABC 中文等中澳主流媒体深度报道，有效提升了中国电影在维州地区的文化影响力。"
                ]
            }
        ],
        "highlights": [
            {"number": "2", "label": "届电影周"},
            {"number": "7", "label": "部影片展映"},
            {"number": "1,000+", "label": "人现场放映"},
            {"number": "0", "label": "放映事故"}
        ],
        "images": [
            {"src": "../assets/film_week/page_1.png", "caption": "中国电影周活动方案", "full": True},
            {"src": "../assets/film_week/page_3.png", "caption": "开幕式与展映排期"},
            {"src": "../assets/film_week/page_7.png", "caption": "媒体传播与成果"}
        ]
    },

    "fashion-week": {
        "title": "墨尔本时尚周艺人活动",
        "subtitle": "时尚展演 + 艺人统筹",
        "category": "performance",
        "time": "Melbourne Fashion Week 期间",
        "location": "澳大利亚 墨尔本",
        "company": "DCF Property 期间",
        "tags": ["艺人统筹", "时尚展演", "现场执行", "媒体拍摄"],
        "sections": [
            {
                "title": "项目背景",
                "paragraphs": [
                    "墨尔本时尚周（Melbourne Fashion Week）是澳大利亚最具影响力的时尚盛事之一。在时尚周期间，负责华人艺人活动的全流程统筹，将华人文化元素融入国际时尚语言，拓展中澳时尚文化交流场景。"
                ]
            },
            {
                "title": "执行内容",
                "paragraphs": [
                    "负责艺人活动全流程管理：",
                ],
                "list": [
                    "艺人接待：负责艺人从抵达墨尔本到活动结束的全行程接待安排",
                    "行程排期：协调艺人时尚周期间的日程安排，确保各环节衔接顺畅",
                    "现场彩排：统筹彩排流程，协调舞台、灯光、音响等技术配合",
                    "演出环节衔接：管理演出各环节的衔接与过渡，确保现场流畅",
                    "媒体拍摄管理：协调媒体拍摄点位、拍摄顺序与素材管理"
                ]
            },
            {
                "title": "项目亮点",
                "paragraphs": [
                    "结合时尚周官方调性，编排含华人文化元素的表演内容，协调澳方场地方与中方艺人团队的沟通。活动在时尚周期间获得现场观众与媒体正面反馈，有效拓展了华人文化在国际时尚场景中的呈现。"
                ]
            }
        ],
        "highlights": [
            {"number": "MFW", "label": "官方活动期间"},
            {"number": "100%", "label": "艺人行程零延误"},
            {"number": "5", "label": "项核心执行环节"}
        ],
        "images": [
            {"src": "../assets/fashion_week/page_1.png", "caption": "墨尔本时尚周艺人活动方案", "full": True},
            {"src": "../assets/fashion_week/page_2.png", "caption": "艺人统筹与行程安排"},
            {"src": "../assets/fashion_week/page_3.png", "caption": "现场执行与媒体拍摄"}
        ]
    },

    "happy-institute": {
        "title": "Happy Institute 开心学笑",
        "subtitle": "脱口秀俱乐部运营 · 笑果文化澳新唯一合作伙伴",
        "category": "performance",
        "time": "2020 - 2022",
        "location": "澳大利亚 墨尔本",
        "company": "PR ASIA 普亚文化",
        "tags": ["俱乐部运营", "演出策划", "IP 合作", "人才培养"],
        "sections": [
            {
                "title": "项目背景",
                "paragraphs": [
                    "开心学笑是普亚文化（PR ASIA）旗下深耕喜剧文化的子公司，以\"传播快乐，解决不开心\"为理念，是笑果文化在澳大利亚与新西兰地区的唯一官方合作伙伴。俱乐部通过脱口秀演出、培训与赛事，培养本地化喜剧人才，搭建中澳喜剧文化交流桥梁。"
                ]
            },
            {
                "title": "运营内容",
                "paragraphs": [
                    "参与俱乐部日常运营与演出策划，工作涵盖：",
                ],
                "list": [
                    "《脱口秀大会》澳新海选：组织笑果文化《脱口秀大会》在澳新地区的海选活动，协调场地、选手招募与评审流程",
                    "内部读稿会：定期组织读稿会，帮助喜剧创作者打磨段子与表演技巧",
                    "线下 Open Mic：策划并执行线下 Open Mic 开放麦活动，为新喜剧演员提供舞台实践机会",
                    "Happy Challenge 学笑挑战赛：组织年度挑战赛事，吸引澳新地区喜剧爱好者参与",
                    "场地对接与票务管理：负责演出场地租赁协调、票务系统运营与观众服务"
                ]
            },
            {
                "title": "项目意义",
                "paragraphs": [
                    "开心学笑作为笑果文化在澳新的唯一官方合作伙伴，有效推动了中国脱口秀文化在南半球的传播。通过系统化的培训与赛事体系，为澳新地区培养了一批本地化喜剧人才，建立了稳定的喜剧爱好者社区。"
                ]
            }
        ],
        "highlights": [
            {"number": "2", "label": "年运营周期"},
            {"number": "100%", "label": "笑果文化澳新独家"},
            {"number": "4", "label": "类核心活动"},
            {"number": "1", "label": "个喜剧社区"}
        ],
        "images": []
    },

    "geely": {
        "title": "吉利汽车商业伙伴大会",
        "subtitle": "星途共启 · 数智领航",
        "category": "conference",
        "time": "2025",
        "location": "国内",
        "company": "策划执行",
        "tags": ["品牌大会", "科技展区", "全流程 Rundown", "视觉系统"],
        "sections": [
            {
                "title": "项目背景",
                "paragraphs": [
                    "吉利汽车商业伙伴大会是吉利年度最高规格的合作伙伴会议，汇聚全国经销商、供应商与战略合作伙伴。大会以\"星途共启 · 数智领航\"为主题，围绕吉利全域 AI 技术体系与\"智能吉利 2025\"战略，向合作伙伴传递品牌方向与技术布局。"
                ]
            },
            {
                "title": "三天议程规划",
                "paragraphs": [
                    "负责三天商业伙伴大会的策划方案与执行 Rundown 编制：",
                ],
                "list": [
                    "Day 1 - 星舰晚宴：以太空主题设计欢迎晚宴，设置沉浸式星空投影与互动装置",
                    "Day 2 - 主题大会 + 颁奖盛典 + 全天展区：上午主题演讲与战略发布，下午颁奖盛典，全天设品牌科技展区",
                    "Day 3 - 分组论坛：按业务板块分组进行深度交流与培训"
                ]
            },
            {
                "title": "视觉系统与展区设计",
                "paragraphs": [
                    "设计深空蓝 + 虹膜橙的科技视觉系统，贯穿主视觉、展区装饰、物料设计全链路。规划以下展区互动体验：",
                ],
                "list": [
                    "全息投影展示区：展示吉利全域 AI 技术体系",
                    "AR 感应体验区：增强现实技术展示智能驾驶场景",
                    "互动涂鸦墙：参与者可通过数字涂鸦留下签名与寄语",
                    "汽车拼图互动：以吉利车型为主题的互动拼图游戏",
                    "扭蛋机抽奖：设置品牌周边扭蛋机，增加趣味性与参与度"
                ]
            },
            {
                "title": "Rundown 编制",
                "paragraphs": [
                    "输出从搭建进场到撤场的完整时间轴与分工表，涵盖技术进场、彩排、正式活动、撤场各环节的时间节点、责任人标注与应急预案。Rundown 精确到分钟级，确保各环节执行团队对时间节点与职责有清晰共识。"
                ]
            }
        ],
        "highlights": [
            {"number": "3", "label": "天大会议程"},
            {"number": "5", "label": "大互动展区"},
            {"number": "100%", "label": "Rundown 独立编制"},
            {"number": "AI", "label": "技术主题"}
        ],
        "images": [
            {"src": "../assets/geely/page_4.png", "caption": "吉利大会策划方案与议程规划", "full": True},
            {"src": "../assets/geely/page_22.png", "caption": "展区设计与互动体验方案"},
            {"src": "../assets/geely/page_26.png", "caption": "Rundown 与执行分工表"}
        ]
    },

    "young-entrepreneurs": {
        "title": "澳大利亚青年企业家峰会",
        "subtitle": "百人级澳新企业家商务对话",
        "category": "conference",
        "time": "2023.01 - 2023.07",
        "location": "澳大利亚",
        "company": "DCF Property 期间",
        "tags": ["商务峰会", "嘉宾对接", "全周期管理", "突发应急"],
        "sections": [
            {
                "title": "项目背景",
                "paragraphs": [
                    "澳大利亚青年企业家峰会面向澳新地区 30-40 岁青年企业家群体，旨在搭建跨境商务对话与合作平台。峰会涵盖主题演讲、圆桌讨论、商务对接等环节，百人级规模，是 DCF Property 旗下年度重点商务活动。"
                ]
            },
            {
                "title": "全周期管理",
                "paragraphs": [
                    "负责峰会从前期策划到后期复盘的全周期管理：",
                ],
                "list": [
                    "前期（1-3 月）：方案策划、议程设计、嘉宾邀约、物料筹备与预算把控",
                    "中期（活动期间）：现场统筹、流程把控、设备调试、嘉宾接待及突发应急处理",
                    "后期（活动结束后）：物资清点、资料归档、数据统计、活动复盘与成果交付"
                ]
            },
            {
                "title": "执行成果",
                "paragraphs": [
                    "全程保障议程按 Rundown 执行，未出现流程延误或嘉宾投诉。突发情况（嘉宾行程临时调整、设备故障等）均在现场快速处置，未影响整体流程。活动后完成完整复盘报告，为下届峰会优化提供数据支撑。"
                ]
            }
        ],
        "highlights": [
            {"number": "100+", "label": "位企业家出席"},
            {"number": "6", "label": "个月全周期管理"},
            {"number": "0", "label": "流程延误 / 嘉宾投诉"},
            {"number": "3", "label": "阶段闭环管理"}
        ],
        "images": []
    },

    "dcf-dinner": {
        "title": "DCF Property 晚宴与投资项目推介会",
        "subtitle": "地产集团圣诞晚宴 + 旅游经济开发论坛 + 高尔夫传承杯",
        "category": "conference",
        "time": "2021.12 / 2023.03",
        "location": "墨尔本",
        "company": "DCF Property 期间",
        "tags": ["高端私宴", "投资论坛", "家族办公室", "高尔夫赛"],
        "sections": [
            {
                "title": "项目背景",
                "paragraphs": [
                    "DCF Property（澳洲大新地产集团）是墨尔本本地地产开发集团，业务覆盖住宅开发、商业地产与投资管理。在其任职期间，策划并执行了两场高端定制活动，面向高净值客户、潜在投资人与官方领导，以活动驱动客户关系维护与项目转化。"
                ]
            },
            {
                "title": "2021 年圣诞晚宴暨旅游经济论坛",
                "paragraphs": [
                    "2021 年 12 月在墨尔本大学科学画廊（Science Gallery Melbourne）举办 DCF 圣诞晚宴暨 2022 旅游经济开发论坛。活动发布 South Melbourne 重点项目 Nu，邀请投资界人士与官方代表出席。负责场地选定、议程编排、嘉宾邀约、现场接待与风险预案。"
                ]
            },
            {
                "title": "2023 年传承杯高尔夫赛暨投资推介会",
                "paragraphs": [
                    "2023 年 3 月在 Eagle Ridge Golf Course 举办传承杯高尔夫比赛暨重点投资项目推介会。邀请 Monarc Pacific Group 家族办公室及各界投资人士出席，探讨财富传承与投资转型。负责赛事流程编排、投资项目推介环节设计、嘉宾接待与现场执行。"
                ]
            },
            {
                "title": "项目成果",
                "paragraphs": [
                    "两场活动均零突发事故，客户转化率较日常提升约 20%。活动有效维护了 DCF Property 与高净值客户、家族办公室及投资机构的长期关系，为后续项目推介建立了信任基础。"
                ]
            }
        ],
        "highlights": [
            {"number": "2", "label": "场高端定制活动"},
            {"number": "0", "label": "突发事故"},
            {"number": "20%", "label": "客户转化率提升"},
            {"number": "30+", "label": "场精品活动（在职期间总计）"}
        ],
        "images": [
            {"src": "../assets/tianlan/page_4.png", "caption": "DCF 地产活动策划方案", "full": True},
            {"src": "../assets/tianlan/page_5.png", "caption": "晚宴与论坛流程设计"},
            {"src": "../assets/tianlan/page_6.png", "caption": "现场执行与接待方案"}
        ]
    },

    "education-bureau": {
        "title": "上海闵行教育局年终会务",
        "subtitle": "官方政务会务 · 500+ 教育界领导参与",
        "category": "conference",
        "time": "2024.11 - 2024.12",
        "location": "上海 闵行",
        "company": "CPET YOUCH 期间",
        "tags": ["政务会务", "分会场统筹", "合规交付", "资料归档"],
        "sections": [
            {
                "title": "项目背景",
                "paragraphs": [
                    "由上海市闵行区教育局主办、长三角教育办公室指导的年终会务活动，五百名各校领导参与。活动属于官方政务类会议，对流程规范、环节衔接与合规性有严格要求。"
                ]
            },
            {
                "title": "执行内容",
                "paragraphs": [
                    "负责会议全流程执行：",
                ],
                "list": [
                    "会议流程排期：编排主会场与分会场议程时间表，确保环节衔接无遗漏",
                    "参会人员统筹：负责 500+ 参会人员的注册、分组、签到与引导",
                    "会务物料设计与制作：统筹会议手册、胸牌、桌签、背景板等物料的设计与制作",
                    "主会场及四个分会场布置：负责五个场地的场地布置、设备调试（音响、投影、直播等）",
                    "现场安保与秩序维护：协调安保人员，确保现场秩序与人员安全",
                    "会后工作：完成资料归档、数据统计与复盘报告"
                ]
            },
            {
                "title": "项目成果",
                "paragraphs": [
                    "严格遵循政务类会议规范，确保流程严谨、环节衔接无遗漏。会后复盘报告获得教育局认可，为后续政务类会务项目建立了标准化执行模板。"
                ]
            }
        ],
        "highlights": [
            {"number": "500+", "label": "位教育界领导参与"},
            {"number": "5", "label": "个会场（主+4分会场）"},
            {"number": "0", "label": "环节遗漏"},
            {"number": "100%", "label": "合规交付"}
        ],
        "images": []
    },

    "mexico-tourism": {
        "title": "诗画浙江（墨西哥）文旅推介会",
        "subtitle": "风华越洋 心印山海 · 浙江省文旅厅 x 墨西哥中国文化中心",
        "category": "conference",
        "time": "2025.05.13",
        "location": "墨西哥 墨西哥城",
        "company": "浙江广禾众联期间",
        "tags": ["官方推介", "中拉文化交流", "海外落地执行", "跨境运输"],
        "sections": [
            {
                "title": "项目背景",
                "paragraphs": [
                    "\"风华越洋 心印山海\"诗画浙江（墨西哥）文旅推介会于 2025 年 5 月 13 日在墨西哥城举办。活动由浙江省文化广电和旅游厅与墨西哥中国文化中心共同主办，浙江广禾众联文化传播有限公司中标承办（中标金额 419.75 万元）。这是浙江省文旅品牌在拉美市场的重要推广活动。"
                ]
            },
            {
                "title": "出席嘉宾",
                "paragraphs": [
                    "协调中墨双方嘉宾出席，近百人到场：",
                ],
                "list": [
                    "中国驻墨西哥使馆临时代办 朱健",
                    "浙江省文化广电和旅游厅厅长 陈广胜",
                    "墨西哥旅游部官员",
                    "墨西哥众议院官员",
                    "中墨文旅企业代表及媒体"
                ]
            },
            {
                "title": "活动结构",
                "paragraphs": [
                    "推介会以\"青绿\"\"绮璨\"\"澎湃\"\"和鸣\"四个篇章结构编排，融合江南文化与拉美本地文化元素：",
                ],
                "list": [
                    "江南服饰走秀：展示浙江传统服饰与现代设计融合",
                    "越剧水袖舞：呈现浙江越剧经典水袖表演",
                    "《黑神话 - 悟空》唢呐演奏：以中国热门游戏 IP 配乐呈现传统唢呐艺术",
                    "\"良渚揽秀\"走秀：以良渚文化为灵感的时尚走秀",
                    "文旅资源推介：向墨西哥旅行商与媒体推介浙江文旅资源与产品线路"
                ]
            },
            {
                "title": "海外落地执行",
                "paragraphs": [
                    "负责海外落地执行全流程：物料跨境运输与清关、现场流程把控、翻译衔接协调、嘉宾行程变动等突发问题处置。确保中墨双方在活动流程、礼仪规范与文化表达上的顺畅对接。"
                ]
            }
        ],
        "highlights": [
            {"number": "419.75", "label": "万元中标金额"},
            {"number": "100", "label": "人出席（近）"},
            {"number": "4", "label": "篇章结构"},
            {"number": "2025.05", "label": "墨西哥城举办"}
        ],
        "images": [
            {"src": "../assets/county_culture/page_4.png", "caption": "文旅推介会策划方案", "full": True},
            {"src": "../assets/county_culture/page_7.png", "caption": "节目编排与篇章结构"},
            {"src": "../assets/county_culture/page_12.png", "caption": "海外执行与传播方案"}
        ]
    },

    "county-culture": {
        "title": "中国县域文创文旅出海项目",
        "subtitle": "县域文化出海 + 政策补贴申报 + 海外文旅推介",
        "category": "conference",
        "time": "规划中",
        "location": "国内县域 / 海外",
        "company": "方案策划",
        "tags": ["县域经济", "文化出海", "政策申报", "一带一路"],
        "sections": [
            {
                "title": "项目背景",
                "paragraphs": [
                    "中国县域拥有丰富的非遗、民俗、美食、民族服饰等文化资源，但普遍缺乏系统化的文化出海路径与政策资金支持。本项目旨在为全国县域政府提供\"文化交流 + 补贴申报\"一体化方案，帮助县域文化\"走出去、留下来\"。"
                ]
            },
            {
                "title": "方案内容",
                "paragraphs": [
                    "项目包含三大模块：",
                ],
                "list": [
                    "县域文化挖掘：梳理非遗、民俗、美食、民族服饰等县域文化亮点，形成可展示、可传播的文化内容包",
                    "国内联展与海外交流：组织国内县域文化联展，策划海外轻量化交流（线上云展 + 海外品鉴会），降低出海门槛",
                    "政策补贴申报：对接国务院文化高质量发展政策、国家文化出口重点项目扶持及\"一带一路\"数字文化出海支持政策，协助县域政府完成项目申报与资金申请流程"
                ]
            },
            {
                "title": "政策对接",
                "paragraphs": [
                    "依托国务院关于文化高质量发展的政策框架、商务部与中宣部联合推进的国家文化出口重点项目认定，以及\"一带一路\"倡议下的数字文化出海支持政策，为县域政府提供政策解读、申报方案撰写与资金申请全流程服务。"
                ]
            }
        ],
        "highlights": [
            {"number": "3", "label": "大模块"},
            {"number": "2", "label": "类出海路径"},
            {"number": "3+", "label": "项政策对接"},
            {"number": "100%", "label": "申报全流程服务"}
        ],
        "images": []
    },

    "alibaba": {
        "title": "阿里巴巴活动供应商采购",
        "subtitle": "淘天 / 夸克 / 高德 / 智能信息 / 阿里公益",
        "category": "procurement",
        "time": "2025.09 - 2025.12",
        "location": "中国 杭州",
        "company": "阿里巴巴（国内）",
        "tags": ["供应商管理", "采购合规", "成本控制", "标准化流程"],
        "sections": [
            {
                "title": "项目背景",
                "paragraphs": [
                    "在阿里巴巴国内业务线期间，承接淘天集团、夸克、高德、智能信息、智能互联、阿里公益、思过崖等多条业务线的活动采购需求。覆盖电商大促、品牌峰会、线下地推、跨境推广、内部会议等 100+ 场活动，是集团活动供应链管理的重要环节。"
                ]
            },
            {
                "title": "采购全流程管理",
                "paragraphs": [
                    "负责从需求接到到交付验收的采购全流程：",
                ],
                "list": [
                    "供应商寻源与筛选：根据活动类型与预算定位，筛选符合资质的供应商（搭建、物料、设备、演艺、餐饮等）",
                    "比价谈判：组织多家供应商比价，通过谈判争取最优价格与服务条款",
                    "合同合规审核：审核供应商资质、合同条款与合规要求，确保采购流程符合集团内控标准",
                    "跨境履约跟进：跟进跨境活动（如海外推广、国际会议）的供应商履约进度，确保按时交付",
                    "成本控制：监控实际执行成本与预算偏差，优化采购结构降低综合成本",
                    "供应商评价体系：建立并维护标准化采购流程与供应商评价体系，沉淀优质供应商资源库"
                ]
            },
            {
                "title": "业务覆盖",
                "paragraphs": [
                    "服务业务线涵盖：淘天集团（电商大促、品牌活动）、夸克（产品发布、用户活动）、高德（地图业务推广活动）、智能信息（AI 产品活动）、智能互联（IoT 设备活动）、阿里公益（公益项目活动）、思过崖（内部培训与会议）。各业务线活动类型与预算规模差异大，需灵活适配采购策略。"
                ]
            }
        ],
        "highlights": [
            {"number": "100+", "label": "场活动采购"},
            {"number": "7+", "label": "条业务线"},
            {"number": "5", "label": "类供应商"},
            {"number": "1", "label": "套标准化流程"}
        ],
        "images": []
    }
}


def generate_page(slug, data, prev_slug, next_slug):
    """Generate a single project detail page."""
    cat_name = CAT_NAMES[data["category"]]
    cat_class = data["category"]

    # Build gallery HTML
    gallery_html = ""
    if data["images"]:
        items = []
        for img in data["images"]:
            full_class = " full-width" if img.get("full") else ""
            items.append(f'''                    <div class="gallery-item{full_class}">
                        <img src="{img["src"]}" alt="{img["caption"]}" loading="lazy">
                        <div class="gallery-caption">{img["caption"]}</div>
                    </div>''')
        gallery_html = f'''
            <div class="detail-gallery">
                <div class="detail-gallery-title">视觉素材</div>
                <div class="gallery-grid">
{chr(10).join(items)}
                </div>
            </div>'''

    # Build highlights HTML
    stats_html = ""
    if data["highlights"]:
        stats = []
        for h in data["highlights"]:
            stats.append(f'''                    <div class="highlight-stat">
                        <div class="highlight-stat-number">{h["number"]}</div>
                        <div class="highlight-stat-label">{h["label"]}</div>
                    </div>''')
        stats_html = f'''
            <div class="detail-highlights">
                <div class="detail-highlights-title">关键数据</div>
                <div class="highlight-stats">
{chr(10).join(stats)}
                </div>
            </div>'''

    # Build sections HTML
    sections_html = ""
    for sec in data["sections"]:
        paras = ""
        for p in sec["paragraphs"]:
            paras += f'\n                    <p>{p}</p>'

        list_html = ""
        if sec.get("list"):
            items = [f'                        <li>{item}</li>' for item in sec["list"]]
            list_html = f'\n                    <ul>\n{chr(10).join(items)}\n                    </ul>'

        sections_html += f'''
                <div class="detail-section">
                    <h3 class="detail-section-title">{sec["title"]}</h3>{paras}{list_html}
                </div>'''

    # Build tags HTML
    tags_html = ""
    for tag in data["tags"]:
        tags_html += f'\n                            <span>{tag}</span>'

    # Prev/Next nav
    prev_html = ""
    if prev_slug:
        prev_data = PROJECTS[prev_slug]
        prev_html = f'''                    <a href="{prev_slug}.html" class="detail-nav-item prev">
                        <span class="detail-nav-label">&larr; 上一项目</span>
                        <span class="detail-nav-title">{prev_data["title"]}</span>
                    </a>'''
    else:
        prev_html = '<div class="detail-nav-item prev"></div>'

    next_html = ""
    if next_slug:
        next_data = PROJECTS[next_slug]
        next_html = f'''                    <a href="{next_slug}.html" class="detail-nav-item next">
                        <span class="detail-nav-label">下一项目 &rarr;</span>
                        <span class="detail-nav-title">{next_data["title"]}</span>
                    </a>'''
    else:
        next_html = '<div class="detail-nav-item next"></div>'

    # Full page HTML
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data["title"]} | 唐冠宇 Francis Tang</title>
    <meta name="description" content="{data["title"]} - {data["subtitle"]}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700&family=Playfair+Display:wght@500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../styles.css">
</head>
<body>
    <!-- Navigation -->
    <header class="header scrolled" id="header">
        <nav class="nav container">
            <a href="../index.html" class="nav-logo">
                <span class="nav-logo-cn">唐冠宇</span>
                <span class="nav-logo-en">Francis Tang</span>
            </a>
            <button class="nav-toggle" id="navToggle" aria-label="切换导航">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-menu" id="navMenu">
                <li><a href="../index.html#about">个人介绍</a></li>
                <li><a href="../index.html#education">教育背景</a></li>
                <li><a href="../index.html#experience">工作履历</a></li>
                <li><a href="../projects.html" class="active">项目案例</a></li>
                <li><a href="../index.html#contact">联系方式</a></li>
            </ul>
        </nav>
    </header>

    <!-- Detail Hero -->
    <div class="detail-page">
        <section class="detail-hero">
            <div class="detail-hero-bg {cat_class}">
                <div class="detail-hero-pattern"></div>
            </div>
            <div class="container detail-hero-content">
                <div class="detail-breadcrumb">
                    <a href="../index.html">首页</a>
                    <span>/</span>
                    <a href="../projects.html">项目案例</a>
                    <span>/</span>
                    <span style="color: rgba(255,255,255,0.7);">{data["title"][:12]}</span>
                </div>
                <span class="detail-category">{cat_name}</span>
                <h1 class="detail-title">{data["title"]}</h1>
                <p class="detail-subtitle">{data["subtitle"]}</p>
            </div>
        </section>

        <!-- Meta Grid -->
        <div class="detail-meta-grid">
            <div class="container" style="display: grid; grid-template-columns: repeat(4, 1fr); width: 100%; max-width: 1280px; margin: 0 auto; padding: 0 24px;">
                <div class="detail-meta-item">
                    <div class="detail-meta-label">时间</div>
                    <div class="detail-meta-value">{data["time"]}</div>
                </div>
                <div class="detail-meta-item">
                    <div class="detail-meta-label">地点</div>
                    <div class="detail-meta-value">{data["location"]}</div>
                </div>
                <div class="detail-meta-item">
                    <div class="detail-meta-label">类型</div>
                    <div class="detail-meta-value">{cat_name}</div>
                </div>
                <div class="detail-meta-item">
                    <div class="detail-meta-label">所在公司</div>
                    <div class="detail-meta-value">{data["company"]}</div>
                </div>
            </div>
        </div>

        <!-- Body -->
        <div class="detail-body">
            <div class="container">
                <div class="detail-content">
{sections_html}
{stats_html}
{gallery_html}
                </div>
            </div>

            <!-- Prev/Next Nav -->
            <div class="detail-nav">
                <div class="container" style="display: grid; grid-template-columns: 1fr 1fr; width: 100%; max-width: 1280px; margin: 0 auto; padding: 0;">
{prev_html}
{next_html}
                </div>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="footer">
        <div class="container footer-content">
            <p>&copy; 2026 唐冠宇 Francis Tang. All rights reserved.</p>
            <p class="footer-note">本作品集基于个人真实经历与项目案例整理。</p>
        </div>
    </footer>

    <script>
        var header = document.getElementById('header');
        window.addEventListener('scroll', function() {{
            if (window.scrollY > 50) {{
                header.classList.add('scrolled');
            }} else {{
                header.classList.remove('scrolled');
            }}
        }});

        var navToggle = document.getElementById('navToggle');
        var navMenu = document.getElementById('navMenu');
        navToggle.addEventListener('click', function() {{
            navMenu.classList.toggle('open');
            navToggle.classList.toggle('active');
        }});
        navMenu.querySelectorAll('a').forEach(function(link) {{
            link.addEventListener('click', function() {{
                navMenu.classList.remove('open');
                navToggle.classList.remove('active');
            }});
        }});

        // Scroll reveal
        var revealElements = document.querySelectorAll('.detail-section, .detail-highlights, .detail-gallery, .detail-nav-item');
        revealElements.forEach(function(el) {{ el.classList.add('reveal'); }});
        var revealObserver = new IntersectionObserver(function(entries) {{
            entries.forEach(function(entry) {{
                if (entry.isIntersecting) {{
                    entry.target.classList.add('active');
                    revealObserver.unobserve(entry.target);
                }}
            }});
        }}, {{ threshold: 0.12, rootMargin: '0px 0px -50px 0px' }});
        revealElements.forEach(function(el) {{ revealObserver.observe(el); }});
    </script>
</body>
</html>'''

    return html


def main():
    for i, slug in enumerate(PROJECT_ORDER):
        prev_slug = PROJECT_ORDER[i - 1] if i > 0 else None
        next_slug = PROJECT_ORDER[i + 1] if i < len(PROJECT_ORDER) - 1 else None
        data = PROJECTS[slug]
        html = generate_page(slug, data, prev_slug, next_slug)

        output_path = os.path.join(OUTPUT_DIR, f"{slug}.html")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated: {slug}.html")

    print(f"\nTotal: {len(PROJECT_ORDER)} project pages generated.")


if __name__ == "__main__":
    main()
