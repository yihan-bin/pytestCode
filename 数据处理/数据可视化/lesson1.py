from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

bar = (
    # 使用了InitOpts来初始化图的主题
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [10, 21, 30, 15, 80, 92])
    # 使用TitleOpts来初始化了标题和子标题
    .set_global_opts(title_opts=opts.TitleOpts(title="Pyecharts练习",subtitle="柱状图"))
)
bar.render('bar1.html')


#设置行名
columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#设置数据
data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
#设置柱状图的主标题与副标题
bar = Bar("柱状图", "一年的降水量与蒸发量")
#添加柱状图的数据及配置项
bar.add_yaxis("降水量", columns, data1, mark_line=["average"], mark_point=["max", "min"])
bar.add_yaxis("蒸发量", columns, data2, mark_line=["average"], mark_point=["max", "min"])
line = Line("折线图","一年的降水量与蒸发量")
#is_label_show是设置上方数据是否显示
line.add("降水量", columns, data1, is_label_show=True)
line.add("蒸发量", columns, data2, is_label_show=True)

bar.render('bar2.html')
