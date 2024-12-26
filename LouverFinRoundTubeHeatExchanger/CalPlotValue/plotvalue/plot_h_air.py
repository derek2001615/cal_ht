import sys
import os
sys.path.append(r"C:\Users\derek\Desktop\pythoncode\cal_ht\LouverFinRoundTubeHeatExchanger\CalPlotValue\calvalue")

import numpy as np

from cal_value_F_p import calculate_Re_DC_values as Re_DC
from cal_value_F_p import calculate_heat_transfer_coefficient_values001 as H1
from cal_value_F_p import calculate_heat_transfer_coefficient_values001 as H2
from cal_value_F_p import calculate_heat_transfer_coefficient_values001 as H3


import plotly.graph_objects as go

Re_DC_values = Re_DC()
H1_values = H1()
H2_values = H2()
H3_values = H3()

Re_DC_values = np.insert(Re_DC_values, 35, None)

fig1 = go.Figure()

fig1.add_trace(go.Scatter(x=Re_DC_values, y=H1_values, mode='lines+markers', name='F_P=1.5mm', line=dict(shape='spline')))
fig1.add_trace(go.Scatter(x=Re_DC_values, y=H2_values, mode='lines+markers', name='F_P=2.0mm', line=dict(shape='spline')))
fig1.add_trace(go.Scatter(x=Re_DC_values, y=H3_values, mode='lines+markers', name='F_P=2.5mm', line=dict(shape='spline')))


fig1.update_layout(title="heat transfer coefficient vs Re_DC under different F_p ", xaxis_title="Re_DC", yaxis_title="heat transfer coefficient", template="plotly_dark")

fig1.show()
fig1.write_html("plot_F_p_h_air.html")


