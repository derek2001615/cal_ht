import sys
import os
sys.path.append(r"C:\Users\derek\Desktop\pythoncode\cal_ht\LouverFinRoundTubeHeatExchanger\CalPlotValue\calvalue")

import numpy as np

from cal_value_F_p import calculate_Re_DC_values as Re_DC
from cal_value_F_p import calculate_pressure_drop_values001 as P1
from cal_value_F_p import calculate_pressure_drop_values002 as P2
from cal_value_F_p import calculate_pressure_drop_values003 as P3


import plotly.graph_objects as go

Re_DC_values = Re_DC()
P1_values = P1()
P2_values = P2()
P3_values = P3()

Re_DC_values = np.insert(Re_DC_values, 35, None)

fig1 = go.Figure()

fig1.add_trace(go.Scatter(x=Re_DC_values, y=P1_values, mode='lines+markers', name='F_P=1.5mm', line=dict(shape='spline')))
fig1.add_trace(go.Scatter(x=Re_DC_values, y=P2_values, mode='lines+markers', name='F_P=2.0mm', line=dict(shape='spline')))
fig1.add_trace(go.Scatter(x=Re_DC_values, y=P3_values, mode='lines+markers', name='F_P=2.5mm', line=dict(shape='spline')))


fig1.update_layout(title="pressure drop vs Re_DC under different F_p ", xaxis_title="Re_DC", yaxis_title="pressure drop", template="plotly_dark")

fig1.show()
fig1.write_html("plot_delta_P.html")


