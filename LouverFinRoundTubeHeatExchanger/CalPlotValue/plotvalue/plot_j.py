import sys
import os
sys.path.append(r"C:\Users\derek\Desktop\pythoncode\cal_ht\LouverFinRoundTubeHeatExchanger\CalPlotValue\calvalue")

from cal_value import calculate_Re_DC_values as Re_DC
from cal_value import calculate_colburn_j_factor_values001 as j1
from cal_value import calculate_colburn_j_factor_values002 as j2
from cal_value import calculate_colburn_j_factor_values003 as j3


import plotly.graph_objects as go

Re_DC_values = Re_DC()
j1_values = j1()
j2_values = j2()
j3_values = j3()

fig1 = go.Figure()

fig1.add_trace(go.Scatter(x=Re_DC_values, y=j1_values, mode='lines+markers', name='F_P=1.5mm', line=dict(shape='spline')))
fig1.add_trace(go.Scatter(x=Re_DC_values, y=j2_values, mode='lines+markers', name='F_P=2.0mm', line=dict(shape='spline')))
fig1.add_trace(go.Scatter(x=Re_DC_values, y=j3_values, mode='lines+markers', name='F_P=2.5mm', line=dict(shape='spline')))


fig1.update_layout(title="colburn_j_factor vs Re_DC under different F_p ", xaxis_title="Re_DC", yaxis_title="colburn_j_factor", template="plotly_dark")

fig1.show()
fig1.write_html("plot_j.html")


