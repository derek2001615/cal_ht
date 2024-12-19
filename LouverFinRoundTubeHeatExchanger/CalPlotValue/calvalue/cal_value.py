import sys
import os
sys.path.append(r"C:\Users\derek\Desktop\pythoncode\cal_ht\LouverFinRoundTubeHeatExchanger\src")

import numpy as np
from cal import LouverFinRoundTube as cal

def get_data001():
    return {
        'D_c':0.01034,
        'delta_f':0.00012,
        'F_p':0.0015,
        'k_f':204,
        'L_h':0.00107,
        'L_p':0.002,
        'P_l':0.022,
        'P_t':0.0254,
        'density_air':1.225,
        'velocity_air':None,
        'viscosity_air':1.887*10**(-5),
        'Cp_air':1007,
        'Pr_air':0.71,
        'HtEx_height':0.355,
        'HtEx_width':0.595,
        'N':1
    }

def calculate_Re_DC_values():
    data = get_data001()
    velocity_air_values = [0.00925 * i for i in range(3, 30)] + [0.0925 * i for i in range(3, 10)] + [0.92] +[0.0925 * i for i in range(10, 21)]
    Re_DC_values = []

    for velocity_air in velocity_air_values:
        data['velocity_air'] = velocity_air  
        LouverFinRoundTube = cal(**data)  
        Re_DC_values.append(LouverFinRoundTube.Re_DC)  

    return np.array(Re_DC_values)

def calculate_colburn_j_factor_values001():
    data = get_data001()
    velocity_air_values = [0.00925 * i for i in range(3, 30)] + [0.0925 * i for i in range(3, 10)] + [0.92] +[0.0925 * i for i in range(10, 21)]
    j_values = []

    for velocity_air in velocity_air_values:
        data['velocity_air'] = velocity_air 
        LouverFinRoundTube = cal(**data) 
        j_values.append(LouverFinRoundTube.j)  

    return np.array(j_values)

def calculate_fanning_friction_factor_values001():
    data = get_data001()
    velocity_air_values = [0.00925 * i for i in range(3, 30)] + [0.0925 * i for i in range(3, 10)] + [0.92] +[0.0925 * i for i in range(10, 21)]
    f_values = []

    for velocity_air in velocity_air_values:
        data['velocity_air'] = velocity_air 
        LouverFinRoundTube = cal(**data) 
        f_values.append(LouverFinRoundTube.f)  

    return np.array(f_values)

def calculate_pressure_drop_values001():
    data = get_data001()
    velocity_air_values = [0.00925 * i for i in range(3, 30)] + [0.0925 * i for i in range(3, 10)] + [0.92] +[0.0925 * i for i in range(10, 21)]
    P_values = []

    for velocity_air in velocity_air_values:
        data['velocity_air'] = velocity_air 
        LouverFinRoundTube = cal(**data) 
        P_values.append(LouverFinRoundTube.delta_P)  

    return np.array(P_values)

def calculate_heat_transfer_coefficient_values001():
    data = get_data001()
    velocity_air_values = [0.00925 * i for i in range(3, 30)] + [0.0925 * i for i in range(3, 10)] + [0.92] +[0.0925 * i for i in range(10, 21)]
    H_values = []

    for velocity_air in velocity_air_values:
        data['velocity_air'] = velocity_air 
        LouverFinRoundTube = cal(**data)   
        H_values.append(LouverFinRoundTube.h_air)  

    return np.array(H_values)


def get_data002():

    return {
        'D_c':0.01034,
        'delta_f':0.00012,
        'F_p':0.002,
        'k_f':204,
        'L_h':0.00107,
        'L_p':0.002,
        'P_l':0.022,
        'P_t':0.0254,
        'density_air':1.225,
        'velocity_air':None,
        'viscosity_air':1.887*10**(-5),
        'Cp_air':1007,
        'Pr_air':0.71,
        'HtEx_height':0.355,
        'HtEx_width':0.595,
        'N':1
    }

def calculate_colburn_j_factor_values002():
    data = get_data002()
    velocity_air_values = [0.00925 * i for i in range(3, 30)] + [0.0925 * i for i in range(3, 10)] + [0.92] +[0.0925 * i for i in range(10, 21)]
    j_values = []

    for velocity_air in velocity_air_values:
        data['velocity_air'] = velocity_air 
        LouverFinRoundTube = cal(**data) 
        j_values.append(LouverFinRoundTube.j)  

    return np.array(j_values)

def calculate_fanning_friction_factor_values002():
    data = get_data002()
    velocity_air_values = [0.00925 * i for i in range(3, 30)] + [0.0925 * i for i in range(3, 10)] + [0.92] +[0.0925 * i for i in range(10, 21)]
    f_values = []

    for velocity_air in velocity_air_values:
        data['velocity_air'] = velocity_air 
        LouverFinRoundTube = cal(**data) 
        f_values.append(LouverFinRoundTube.f)  

    return np.array(f_values)

def calculate_pressure_drop_values002():
    data = get_data002()
    velocity_air_values = [0.00925 * i for i in range(3, 30)] + [0.0925 * i for i in range(3, 10)] + [0.92] +[0.0925 * i for i in range(10, 21)]
    P_values = []

    for velocity_air in velocity_air_values:
        data['velocity_air'] = velocity_air 
        LouverFinRoundTube = cal(**data) 
        P_values.append(LouverFinRoundTube.delta_P)  

    return np.array(P_values)

def calculate_heat_transfer_coefficient_values002():
    data = get_data002()
    velocity_air_values = [0.00925 * i for i in range(3, 30)] + [0.0925 * i for i in range(3, 10)] + [0.92] +[0.0925 * i for i in range(10, 21)]
    H_values = []

    for velocity_air in velocity_air_values:
        data['velocity_air'] = velocity_air 
        LouverFinRoundTube = cal(**data)   
        H_values.append(LouverFinRoundTube.h_air)  

    return np.array(H_values)


def get_data003():
    return {
        'D_c':0.01034,
        'delta_f':0.00012,
        'F_p':0.0025,
        'k_f':204,
        'L_h':0.00107,
        'L_p':0.002,
        'P_l':0.022,
        'P_t':0.0254,
        'density_air':1.225,
        'velocity_air':None,
        'viscosity_air':1.887*10**(-5),
        'Cp_air':1007,
        'Pr_air':0.71,
        'HtEx_height':0.355,
        'HtEx_width':0.595,
        'N':1
    }

def calculate_colburn_j_factor_values003():
    data = get_data003()
    velocity_air_values = [0.00925 * i for i in range(3, 30)] + [0.0925 * i for i in range(3, 10)] + [0.92] +[0.0925 * i for i in range(10, 21)]
    j_values = []

    for velocity_air in velocity_air_values:
        data['velocity_air'] = velocity_air 
        LouverFinRoundTube = cal(**data) 
        j_values.append(LouverFinRoundTube.j)  

    return np.array(j_values)

def calculate_fanning_friction_factor_values003():
    data = get_data003()
    velocity_air_values = [0.00925 * i for i in range(3, 30)] + [0.0925 * i for i in range(3, 10)] + [0.92] +[0.0925 * i for i in range(10, 21)]
    f_values = []

    for velocity_air in velocity_air_values:
        data['velocity_air'] = velocity_air 
        LouverFinRoundTube = cal(**data) 
        f_values.append(LouverFinRoundTube.f)  

    return np.array(f_values)

def calculate_pressure_drop_values003():
    data = get_data003()
    velocity_air_values = [0.00925 * i for i in range(3, 30)] + [0.0925 * i for i in range(3, 10)] + [0.92] +[0.0925 * i for i in range(10, 21)]
    P_values = []

    for velocity_air in velocity_air_values:
        data['velocity_air'] = velocity_air 
        LouverFinRoundTube = cal(**data) 
        P_values.append(LouverFinRoundTube.delta_P)  

    return np.array(P_values)

def calculate_heat_transfer_coefficient_values003():
    data = get_data003()
    velocity_air_values = [0.00925 * i for i in range(3, 30)] + [0.0925 * i for i in range(3, 10)] + [0.92] +[0.0925 * i for i in range(10, 21)]
    H_values = []

    for velocity_air in velocity_air_values:
        data['velocity_air'] = velocity_air 
        LouverFinRoundTube = cal(**data)   
        H_values.append(LouverFinRoundTube.h_air)  

    return np.array(H_values)



