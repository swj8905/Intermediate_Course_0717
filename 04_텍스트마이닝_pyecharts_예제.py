from pyecharts import Bar3D

bar3d = Bar3D("감성 분석 결과", width=1200, height=600)
x_axis = ["매우긍정", "긍정", "중립", "부정", "매우부정"]
y_axis = []
data = [[0, 0, 60], [0, 1, 10], [0, 2, 20], [0, 3, 5], [0, 4, 50]]
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
bar3d.add("", x_axis, y_axis, [[d[1], d[0], d[2]] for d in data],
    is_visualmap=True, visual_range=[0, 20], visual_range_color=range_color,
    grid3d_width=200, grid3d_depth=40)
bar3d.render("./bar3d.html")

import webbrowser
import os
ap = os.path.abspath("./bar3d.html")
# webbrowser.open(ap) # 윈도우
webbrowser.open("file://" + ap) # 맥