import sys
import os
sys.path.append(r"C:\Users\derek\Desktop\pythoncode\cal_ht\LouverFinRoundTubeHeatExchanger\CalPlotValue\calvalue")

import numpy as np

from cal_value_F_p import calculate_Re_DC_values as Re_DC
from cal_value_F_p import calculate_fanning_friction_factor_values001 as f1
from cal_value_F_p import calculate_fanning_friction_factor_values002 as f2
from cal_value_F_p import calculate_fanning_friction_factor_values003 as f3


import plotly.graph_objects as go

Re_DC_values = Re_DC()
f1_values = f1()
f2_values = f2()
f3_values = f3()

Re_DC_values = np.insert(Re_DC_values, 35, None)

fig1 = go.Figure()

fig1.add_trace(go.Scatter(x=Re_DC_values, y=f1_values, mode='lines+markers', name='F_P=1.5mm', line=dict(shape='spline')))
fig1.add_trace(go.Scatter(x=Re_DC_values, y=f2_values, mode='lines+markers', name='F_P=2.0mm', line=dict(shape='spline')))
fig1.add_trace(go.Scatter(x=Re_DC_values, y=f3_values, mode='lines+markers', name='F_P=2.5mm', line=dict(shape='spline')))


fig1.update_layout(title="fanning_friction_factor vs Re_DC under different F_p ", xaxis_title="Re_DC", yaxis_title="fanning_friction_factor", template="plotly_dark")

fig1.show()
fig1.write_html("plot_F_p_f.html")


