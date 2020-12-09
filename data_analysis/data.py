import requests
url = 'https://301c7116e11b.ngrok.io/authenticateuser'
# https://301c7116e11b.ngrok.io/gettransactions
myobj = {'username': 'customer1_hsbc','password' : 'pass1hsbc','accountnumber': '4204200005','specialkey':'fafjgaaiwkafa'}
x = requests.post(url, data = myobj)
print(x.text)
# import numpy as np
# import pandas as pd
# from pyecharts.charts import *
# from pyecharts.components import Table
# from pyecharts import options as opts
# from pyecharts.globals import CurrentConfig
# from jinja2 import Environment, FileSystemLoader

# data = pd.read_csv("./data_analysis/customer_transactions.csv")
# balance_bar = data[0:15]['Closing Balance']
# balance_hsbc = data[15:30]['Closing Balance']

# week_name_list = list(range(1,16))
# high_temperature = balance_hsbc
# low_temperature = balance_bar

# print(len(balance_bar))
# print(len(balance_hsbc))

# (
#     Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
#     .add_xaxis(xaxis_data=week_name_list)
#     .add_yaxis(
#         series_name="最高气温",
#         y_axis=high_temperature,
#         markpoint_opts=opts.MarkPointOpts(
#             data=[
#                 opts.MarkPointItem(type_="max", name="最大值"),
#                 opts.MarkPointItem(type_="min", name="最小值"),
#             ]
#         ),
#         markline_opts=opts.MarkLineOpts(
#             data=[opts.MarkLineItem(type_="average", name="平均值")]
#         ),
#     )
#     .add_yaxis(
#         series_name="最低气温",
#         y_axis=low_temperature,
#         markpoint_opts=opts.MarkPointOpts(
#             data=[opts.MarkPointItem(value=-2, name="周最低", x=1, y=-1.5)]
#         ),
#         markline_opts=opts.MarkLineOpts(
#             data=[
#                 opts.MarkLineItem(type_="average", name="平均值"),
#                 opts.MarkLineItem(symbol="none", x="90%", y="max"),
#                 opts.MarkLineItem(symbol="circle", type_="max", name="最高点"),
#             ]
#         ),
#     )
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="未来一周气温变化", subtitle="纯属虚构"),
#         tooltip_opts=opts.TooltipOpts(trigger="axis"),
#         toolbox_opts=opts.ToolboxOpts(is_show=True),
#         xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
#     )
#     .render("temperature_change_line_chart.html")
# )