from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker


v = Faker.choose()
x_data = ["激光机", "射线机", "增值单"]
y_data = [49, 6, 4]
c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(x_data,y_data)],
        radius=["50%", "75%"],
        #center=["75%", "50%"],
        #label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Pie-Radius"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_rosetype.html")
)