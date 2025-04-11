'''
https://www.sciencedirect.com/science/article/pii/S0017931098003020
'''
import numpy as np


class LouverFinRoundTube:
    def __init__(self, **kwargs):
        # fin parameters
        self.D_c = kwargs['D_c']
        self.delta_f = kwargs['delta_f']
        self.F_p = kwargs['F_p']
        self.k_f = kwargs['k_f']
        # louver parameters
        self.L_h = kwargs['L_h']
        self.L_p = kwargs['L_p']
        # tube parameters
        self.P_l = kwargs['P_l']
        self.P_t = kwargs['P_t']
        # air parameters
        self.density_air = kwargs['density_air']
        self.velocity_air = kwargs['velocity_air']
        self.viscosity_air = kwargs['viscosity_air']
        self.Cp_air = kwargs['Cp_air']
        self.Pr_air = kwargs['Pr_air']
        # heat exchanger parameters
        self.HtEx_height = kwargs['HtEx_height']
        self.HtEx_width = kwargs['HtEx_width']
        self.N = kwargs['N']

        self.calc_areas()
        self._calc_reynolds_numbers()
        self._calc_D_h()
        
        self._calc_J1()
        self._calc_J2()
        self._calc_J3()
        self._calc_J4()
        self._calc_J5()
        self._calc_J6()
        self._calc_J7()
        self._calc_J8()
        self._calc_colburn_j_factor()

        self._calc_F1()
        self._calc_F2()
        self._calc_F3()
        self._calc_F4()
        self._calc_F5()
        self._calc_F6()
        self._calc_F7()
        self._calc_F8()
        self._calc_F9()
        self._calc_fanning_friction_factor()

        self.calc_pressure_drop()
        self.calc_heat_transfer_coefficient()
        self.calc_efficiency()


    '''
    #fin parameters
    D_c: fin collar outside diameter (m)
    delta_f(=t in graph): fin thickness (m)
    F_p: fin pitch (m)
    k_f: thermal conductivity of fin (W/(m*K))

    #louver parameters
    L_h: louver height (m)
    L_p: major louver pitch (m)

    #tube parameters
    P_l: longitudinal tube pitch (m)
    P_t: transverse tube pitch (m)

    #air parameters
    density_air: density of air (kg/m^3)
    velocity_air: velocity of air (m/s)
    viscosity_air: viscosity of air (kg/(m*s))
    Cp_air: specific heat at constant pressure of air (W/(kg*K))
    Pr_air: Prandtl number of air (dimensionless)

    #heat exchanger parameters
    HtEx_height: height of heat exchanger (m)
    HtEx_width: width of heat exchanger (m)
    N: number of longitudinal tube rows (dimensionless)

    N_t: numbers of tubes in a row (dimensionless)
    N_f: numbers of fins (dimensionless)
     
    A_c: minimum free flow area (m^2)
    A_f: fin surface area (m^2)
    A_o: total surface area (m^2)
    A_t: external tube surface area (m^2)
    A_fr: frontal area of the fins (m^2)
    sigma: contraction ratio of cross sectional area (dimensionless)
    '''

    def calc_areas(self):
        self.N_t = np.floor(self.HtEx_height / self.P_t)
        self.N_f = np.floor(self.HtEx_width / self.F_p)

        self.A_fr = self.HtEx_height * self.HtEx_width
        self.A_c = self.A_fr \
            - self.N_t \
            * (self.D_c * self.HtEx_width + self.N_f * self.delta_f * (self.P_t * self.D_c))
        self.sigma = self.A_c / self.A_fr      

        self.A_f = 2 * self.N_f \
            * (self.P_l * self.HtEx_height - 0.25 * np.pi * self.D_c**2 * self.N_t) \
            * self.N \
            + 2 * self.delta_f * self.N_f * (self.HtEx_height + self.P_l * self.N)        
        self.A_t = np.pi * self.D_c \
            * (self.HtEx_width - self.N_f * self.delta_f) \
            * self.N_t * self.N
        self.A_o = self.A_f + self.A_t

    def _calc_reynolds_numbers(self):
        self.Re_DC = self.density_air * self.velocity_air * self.D_c \
            / self.viscosity_air / self.sigma

    def _calc_D_h(self):
        self.D_h = 4 * self.A_c * self.P_l * self.N \
            / self.A_o

    def _calc_colburn_j_factor(self):
        if self.Re_DC < 1000:
            self.j = 14.3117 * self.Re_DC ** self.J1 \
                * (self.F_p / self.D_c) ** self.J2 \
                * (self.L_h / self.L_p) ** self.J3 \
                * (self.F_p / self.P_l) ** self.J4 \
                * (self.P_l / self.P_t) ** (-1.724)
        
        elif self.Re_DC >= 1000:
            self.j = 1.1373 * self.Re_DC ** self.J5 \
                * (self.F_p / self.P_l) ** self.J6 \
                * (self.L_h / self.L_p) ** self.J7 \
                * (self.P_l / self.P_t) ** self.J8 \
                * self.N ** 0.3545
    
    def _calc_J1(self):
        self.J1 = -0.991 \
            - 0.1055 * (self.P_l / self.P_t) \
            * np.log(self.L_h / self.L_p)

    def _calc_J2(self):
        self.J2 = -0.7344 \
            + 2.1059 * (self.N ** 0.55 / (np.log(self.Re_DC) - 3.2))

    def _calc_J3(self):
        self.J3 = 0.08485 * (self.P_l / self.P_t) ** (-4.4) \
            * self.N ** (-0.68)

    def _calc_J4(self):
        self.J4 = -0.1741 * np.log(self.N)

    def _calc_J5(self):
        self.J5 = -0.6027 \
            + 0.02593 * (self.P_l / self.D_h) ** 0.52 \
            * self.N ** (-0.5) \
            * np.log(self.L_h / self.L_p)

    def _calc_J6(self):
        self.J6 = -0.4776 \
            + 0.40774 * (self.N ** 0.7 / (np.log(self.Re_DC) - 4.4))

    def _calc_J7(self):
        self.J7 = -0.58655 * (self.F_p / self.D_h) ** 2.3 \
            * (self.P_l / self.P_t) ** (-1.6) \
            * self.N ** (-0.65)

    def _calc_J8(self):
        self.J8 = 0.0814 * (np.log(self.Re_DC) - 3)


    def _calc_fanning_friction_factor(self):
        if self.N == 1:
            self.f = 0.00317 * self.Re_DC ** self.F1 \
                * (self.F_p / self.P_l) ** self.F2 \
                * (self.D_h / self.D_c) ** self.F3 \
                * (self.L_h / self.L_p) ** self.F4 \
                * (np.log(self.A_o / self.A_t)) ** (-6.0483)

        elif self.N > 1:
            self.f = 0.06393 * self.Re_DC ** self.F5 \
                * (self.F_p / self.D_c) ** self.F6 \
                * (self.D_h / self.D_c) ** self.F7 \
                * (self.L_h / self.L_p) ** self.F8 \
                * self.N ** self.F9 \
                * (np.log(self.Re_DC) - 4) ** (-1.093)

    def _calc_F1(self):
        self.F1 = 0.1691 \
            + 4.4118 * (self.F_p / self.P_l) ** (-0.3) \
            * (self.L_h / self.L_p) ** (-2) \
            * (np.log(self.P_l / self.P_t)) \
            * (self.F_p / self.P_t) ** 3

    def _calc_F2(self):
        self.F2 = -2.6642 \
            - 14.3809 * (1 / np.log(self.Re_DC))

    def _calc_F3(self):
        self.F3 = -0.6816 * np.log(self.F_p / self.P_l)

    def _calc_F4(self):
        self.F4 = 6.4668 * (self.F_p / self.P_t) ** 1.7 \
            * np.log(self.A_o / self.A_t)

    def _calc_F5(self):
        self.F5 = 0.1395 \
            - 0.0101 * (self.F_p / self.P_l) ** 0.58 \
            * (self.L_h / self.L_p) ** (-2) \
            * (np.log(self.A_o / self.A_t)) \
            * (self.P_l / self.P_t) ** 1.9

    def _calc_F6(self):
        self.F6 = -6.4367 * (1 / np.log(self.Re_DC))

    def _calc_F7(self):
        self.F7 = 0.07191 * np.log(self.Re_DC)

    def _calc_F8(self):
        self.F8 = -2.0585 * (self.F_p / self.P_t) ** 1.67 \
            * np.log(self.Re_DC)

    def _calc_F9(self):
        self.F9 = 0.1036 * np.log(self.P_l / self.P_t)

    def calc_pressure_drop(self):
        self.delta_P = self.density_air \
            * self.f \
            * self.A_o / self.A_c \
            * 0.5 * (self.velocity_air / self.sigma) ** 2 
        
    def calc_heat_transfer_coefficient(self):
        self.h_air = self.j \
            * self.density_air \
            * (self.velocity_air / self.sigma) \
            * self.Cp_air \
            / self.Pr_air**(2 / 3)

    def calc_efficiency(self):
        m = np.sqrt(2 * self.h_air / (self.k_f * self.delta_f))
        self.r = self.D_c / 2
        self.X_L = self.P_l / 2
        self.X_M = np.sqrt((self.P_t / 2)**2 + self.P_l**2) / 2

        #inline layout or 1-row coil
        if self.N == 1:
            self.Req_over_r = 1.28 * self.X_M / self.r \
                * np.sqrt(self.X_L / self.X_M - 0.2)
        #staggered tube layout
        elif self.N >= 2:
            self.Req_over_r = 1.27 * self.X_M / self.r \
                * np.sqrt(self.X_L / self.X_M - 0.3)

        self.phi = (self.Req_over_r - 1) \
            * (1 + 0.35 * np.log(self.Req_over_r))
        self.eta_f = np.tanh(m * self.r * self.phi) / (m * self.r * self.phi)
        self.eta_o = 1 - (self.A_f / self.A_o) * (1 - self.eta_f)
