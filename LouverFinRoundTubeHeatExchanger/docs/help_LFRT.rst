Louver fin with round tube
============================



Description
-----------

The package calculates different features of Louver fin with round tube heat exchanger

Louver fin with a flat tube
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html
     
     <img src="_static/html/LFRTHEdef1.JPG" alt="Description of the image" width="100%" height="auto">
     <p><em>Figure 1:Typical louver fin geometry with round tube configuration <a href="https://www.sciencedirect.com/science/article/pii/S0017931098003020">C.-C. Wang</a></em></p>

------------------------------------------------



Correlations
-----------------

J Colburn factor
-----------------

The J-factor provides a way to relate heat, mass, and momentum transfer processes. This allows to estimate one transfer coefficient.

J1~J8 are parameters calculated by other parameters below.

.. math::

    \begin{equation}
    j = \begin{cases}
    14.3117 \cdot Re_{DC}^{J1} \cdot \left(\frac{F_p}{D_c}\right)^{J2} 
    \cdot \left(\frac{L_h}{L_p}\right)^{J3} \cdot \left(\frac{F_p}{P_l}\right)^{J4} 
    \cdot \left(\frac{P_l}{P_t}\right)^{-1.724} & \text{if } Re_{DC} < 1000 \\
    1.1373 \cdot Re_{DC}^{J5} \cdot \left(\frac{F_p}{P_l}\right)^{J6} 
    \cdot \left(\frac{L_h}{L_p}\right)^{J7} \cdot \left(\frac{P_l}{P_t}\right)^{J8} 
    \cdot N^{0.3545} & \text{if } Re_{DC} \geq 1000
    \end{cases}
    \end{equation} 

F friction factor
-----------------

The friction factor in heat exchanger fins is a dimensionless parameter that quantifies the resistance to fluid flow through the finned passages.

F1~F9 are parameters calculated by other parameters below.

.. math::

    \begin{equation}
    f = \begin{cases}
    0.00317 \cdot Re_{DC}^{F1} \cdot \left(\frac{F_p}{P_l}\right)^{F2} 
    \cdot \left(\frac{D_h}{D_c}\right)^{F3} \cdot \left(\frac{L_h}{L_p}\right)^{F4} 
    \cdot \left(\ln\left(\frac{A_o}{A_t}\right)\right)^{-6.0483} & \text{if } N = 1 \\
    0.06393 \cdot Re_{DC}^{F5} \cdot \left(\frac{F_p}{D_c}\right)^{F6} 
    \cdot \left(\frac{D_h}{D_c}\right)^{F7} \cdot \left(\frac{L_h}{L_p}\right)^{F8} 
    \cdot N^{F9} \cdot \left(\ln(Re_{DC}) - 4\right)^{-1.093} & \text{if } N > 1
    \end{cases}
    \end{equation}

h_air heat transfer coefficient
----------------------------

It quantifies the rate of heat transfer between a solid surface (like a fin) and a surrounding fluid.

.. math::

    h_{air} = j \cdot \rho_{air} \cdot \left(\frac{v_{air}}{\sigma}\right) \cdot C_{p_{air}} \cdot \left(Pr_{air}\right)^{-\frac{2}{3}}

Pressure drop
----------------

Reduction in pressure of the fluid as it flows through the heat exchanger due to the resistance to flow caused by the fins. 

.. math::

    \Delta P = \rho_{air} \cdot f \cdot \frac{A_o}{A_c} \cdot 0.5 \cdot \left(\frac{v_{air}}{\sigma}\right)^2

Fin-and-tube louver surface efficiency
----------------------------------------
  
Measure of how effectively a louver system can transfer heat between two fluids.

:math:`m = \sqrt{\frac{2 h_{air}}{k \delta}}`
        
:math:`\eta = \frac{\tanh(m r \varphi)}{m r \varphi}`

:math:`\eta_{overall} = 1 - \left(\frac{A_{fin}}{A_{total}}\right) (1 - \eta)`

------------------------------------------------------------------------

Example
--------

For the instance it is necessary to provide these values:

.. raw:: html
     
     <img src="_static/html/LFRTHEdef2.JPG" alt="Description of the image" width="100%" height="auto">

     <img src="_static/html/LFRTHEdef3.JPG" alt="Description of the image" width="100%" height="auto">

     <img src="_static/html/LFRTHEdef4.JPG" alt="Description of the image" width="100%" height="auto">

Fin parameters:

- D_c: fin collar outside diameter (m)
- delta_f(=t in graph): fin thickness (m)
- F_p: fin pitch (m)
- k_f: thermal conductivity of fin (W/(m*K))

Louver parameters:

- L_h: louver height (m)
- L_p: major louver pitch (m)

Tube parameters:

- P_l: longitudinal tube pitch (m)
- P_t: transverse tube pitch (m)

Air parameters:

- density_air: density of air (kg/m^3)
- velocity_air: velocity of air (m/s)
- viscosity_air: viscosity of air (kg/(m*s))
- Cp_air: specific heat at constant pressure of air (W/(kg*K))
- Pr_air: Prandtl number of air (dimensionless)

Heat exchanger parameters:

- HtEx_height: height of heat exchanger (m)
- HtEx_width: width of heat exchanger (m)
- N: number of longitudinal tube rows (dimensionless)


-----------------------------------------------------------------     

Implementation
-----------------

Input
------

Data provided by the user:

::

     from cal import LouverFinRoundTube as cal
     def get_data():
     return{
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


Call the function
------------------

::

     def main():
     data = get_data()
     caldata = cal(**data)

     print("Re_DC:", caldata.Re_DC)
     print("Fanning friction factor:", caldata.f)
     print("Colburn j-factor:", caldata.j)
     print("Pressure drop:", caldata.delta_P)
     print("Heat transfer coefficient h_air:", caldata.h_air)
     print("efficiency:", caldata.eta_o)

Output
-------

Results obtained from the calculations:

::

     #Results
     Re_DC: 100.05202671182407
     Fanning friction factor: 1.6476016678787477
     Colburn j-factor: 0.05148511118448749
     Pressure drop: 0.9557613545778805
     Heat transfer coefficient h_air: 11.894590038782678
     efficiency: 0.9655369378815283

-----------------------------------------------------------------

Graphs
-------

The following graphs show the variation of the  friction factor, J Colburn factor, pressure drop, and heat transfer coefficient respect to Reynolds number and other parameters.


.. raw:: html
     
     <iframe src="_static/graph/plot_F_p_f.html" frameborder="0" scrolling="0" width="1000" height="700"></iframe>
     <iframe src="_static/graph/plot_F_p_j.html" frameborder="0" scrolling="0" width="1000" height="700"></iframe>
     <iframe src="_static/graph/plot_F_p_delta_P.html" frameborder="0" scrolling="0" width="1000" height="700"></iframe>
     <iframe src="_static/graph/plot_F_p_h_air.html" frameborder="0" scrolling="0" width="1000" height="700"></iframe>


.. footer:: &copy; 2024 CC Wang Lab.



