from cal import LouverFinRoundTube as cal


def get_data():
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
        'velocity_air':0.0925, 
        'viscosity_air':1.887*10**(-5),
        'Cp_air':1007,
        'Pr_air':0.71,
        'HtEx_height':0.355,
        'HtEx_width':0.595,
        'N':1
    }

def main():
    data = get_data()
    caldata = cal(**data)

    print("Re_DC:", caldata.Re_DC)
    print("Fanning friction factor:", caldata.f)
    print("Colburn j-factor:", caldata.j)
    print("Pressure drop:", caldata.delta_P)
    print("Heat transfer coefficient h_o:", caldata.h_air)
    print("efficiency:", caldata.eta_o)

if __name__ == '__main__':
    main()






