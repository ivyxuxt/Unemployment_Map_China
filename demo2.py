from pyecharts.charts import Map
from pyecharts import options as opts

# 准备数据，格式为 ("省份名称", 值)
map_data = [
    ("北京市", 3.2),
    ("天津市", 3.7),
    ("河北省", 3.1),
    ("山西省", 2.3),
    ("内蒙古自治区", 3.8),
    ("辽宁省", 4.3),
    ("吉林省", 3.3),
    ("黑龙江省", 3.2),
    ("上海市", 2.7),
    ("江苏省", 2.5),
    ("浙江省", 2.6),
    ("安徽省", 2.5),
    ("福建省", 3.3),
    ("江西省", 2.8),
    ("山东省", 2.9),
    ("河南省", 3.4),
    ("湖北省", 3.0),
    ("湖南省", 2.3),
    ("广东省", 2.5),
    ("广西壮族自治区", 2.5),
    ("海南省", 3.1),
    ("重庆市", 2.9),
    ("四川省", 3.6),
    ("贵州省", 4.5),
    ("云南省", 3.8),
    ("西藏自治区", 2.6),
    ("陕西省", 3.5),
    ("甘肃省", 3.4),
    ("青海省", 1.8),
    ("宁夏回族自治区", 4.1),
    ("新疆维吾尔自治区", 2.0),
]

# 创建地图
map = Map(init_opts={"width": "1200px", "height": "800px"})

# 添加地图数据
map.add("china_unemployment_rate", map_data, "china", is_map_symbol_show=False) ##隐藏小圆点

# 设置全局配置项
map.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(
        is_piecewise=True,
        pieces=[
            {"min": 0, "max": 0.5, "label": "0-0.5%", "color": "#E0F7FA"},
            {"min": 0.5, "max": 1.0, "label": "0.5-1%", "color": "#42A5F5"},
            {"min": 1.0, "max": 1.5, "label": "1-1.5%", "color": "#FFF9C4"},
            {"min": 1.5, "max": 2.0, "label": "1.5-2%", "color": "#FFEB3B"},
            {"min": 2.0, "max": 2.5, "label": "2-2.5%", "color": "#FF9800"},
            {"min": 2.5, "max": 3.0, "label": "2.5-3%", "color": "#FF5722"},
            {"min": 3.0, "max": 3.5, "label": "3-3.5%", "color": "#F44336"},
            {"min": 3.5, "max": 4.0, "label": "3.5-4%", "color": "#795548"},
            {"min": 4.0, "max": 4.5, "label": "4-4.5%", "color": "#3E2723"},
        ],
    ),
    tooltip_opts=opts.TooltipOpts(
        formatter="{c}%",
        textstyle_opts={"fontSize": 9},
    ),
    title_opts=opts.TitleOpts(
        title="China Unemployment Rate",
        subtitle="Data Visualization",
        title_textstyle_opts={"fontSize": 16}
    ),
)

# 设置系列配置项，隐藏省份名称
map.set_series_opts(
    label_opts=opts.LabelOpts(is_show=False),  # 隐藏数据标签
    tooltip_opts=opts.TooltipOpts(
        formatter=lambda x: f"{x['value']}%"

        #formatter="<br/>{c}"  # 只显示省份名称和数值，不显示标签
    )
)

# 渲染图表到文件
map.render("china_unemployment_map.html")
print("地图已保存为 china_unemployment_map.html，请在浏览器中打开查看。")