from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.globals import  CurrentConfig,NotebookType
CurrentConfig.NOTEBOOK_TYPE=NotebookType.NTERACT



data=[('北京',52912),
('天津',38975),
('河北',15893),
('山西',18132),

('辽宁',24866),
('吉林',15083),
('黑龙江',18859),
('上海',53617),
('江苏',39796),
('浙江',33851),
('安徽',17141),
('福建',25969),
('江西',17290),
('山东',28353),
('河南',17842),
('湖北',21642),
('湖南',19418),
('广东',30762),
('广西',16064),
('海南',20939),
('重庆',22927),
('四川',17920),
('贵州',16349),
('云南',15831),
('西藏',10990),
('陕西',18485),
('甘肃',14203),
('青海',18020),
('新疆',16736),
]
map_=Map()
map_.add(
    series_name='居民消费水平',
    data_pair=data,
    maptype='china',
    zoom=1
)
map_.set_global_opts(
    title_opts=opts.TitleOpts(
        title='2017年居民消费水平',
        subtitle='数据',
        pos_right='center',
        pos_top='5%',

    ),
    visualmap_opts=opts.VisualMapOpts(
        max_=53617,
        min_=10990,
        range_color=['#1E9600','#FFF200','#ff0000']

    )
)
map_.render('1.html')