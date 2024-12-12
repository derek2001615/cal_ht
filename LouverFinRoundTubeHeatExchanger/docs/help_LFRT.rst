Louver fin with round tube
============================



Description
-----------

The package calculates different features of Louver fin with round tube heat exchanger

Louver fin with a flat tube
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html
     
     <img src="./img/LF.jpg" alt="Description of the image" width="100%" height="auto">
     <p><em>Figure 1: Schematic of a Louver fin with a flat tube <a href="https://www.sciencedirect.com/science/article/pii/0017931096001160">Y.J. Chang, C.C. Wang</a></em></p>

------------------------------------------------



Correlations
-----------------

J Colburn factor
-----------------

The J-factor provides a way to relate heat, mass, and momentum transfer processes. This allows to estimate one transfer coefficient. 

:math:`j = Re_{Lp}^{-0.49} \left( \frac{\theta}{90} \right)^{0.27} \left( \frac{F_p}{L_p} \right)^{-0.14} \left( \frac{F_l}{L_p} \right)^{-0.29} \left( \frac{T_d}{L_p} \right)^{-0.23} \\
\left( \frac{L_1}{L_p} \right)^{0.68} \left( \frac{T_p}{L_p} \right)^{-0.28} \left( \frac{\delta_f}{L_p} \right)^{-0.05}` 


F friction factor
-----------------

The friction factor in heat exchanger fins is a dimensionless parameter that quantifies the resistance to fluid flow through the finned passages. 


:math:`f=f_{1}f_{2}f_{3}`

:math:`\begin{equation}
f_1 = \begin{cases}
14.39 Re_{Lp}^{-0.805 \left( \frac{F_P}{F_l} \right)} \log_{e}\left( 1.0 + \left( \frac{F_p}{L_p} \right)\right)^{3.04} & Re_{Lp} < 150 \\
4.97 Re_{Lp}^{0.6049 - 1.064 / \theta^2} \log_{e} \left( \left( \frac{F_t}{F_p} \right)^{0.5} + 0.9 \right)^{ - 0.527} & 150 < Re_{Lp} < 5,000
\end{cases}
\end{equation}`

:math:`\begin{equation}
f_2 = \begin{cases}
\left( \log_{e} \left( \left( \frac{F_l}{F_p} \right)^{0.48} + 0.9 \right) \right) ^{- 1.435}  \left( \frac{D_h}{L_p} \right)^{-3.01} \log_{e} \left( 0.5 Re_{Lp} \right)^{-3.01} & Re_{Lp} < 150 \\
\left( \left( \frac{D_h}{L_p} \right) \log_{e} \left( 0.3 Re_{Lp} \right)\right) ^ {- 2.966} \left( \frac{F_p}{L_1} \right)^ { - 0.7931 \left( {T_p}/{T_h} \right)} & 150 < Re_{Lp} < 5,000
\end{cases}
\end{equation}`

:math:`\begin{equation}
f_3 = \begin{cases}
\left( \frac{F_p}{L_l} \right)^{-0.308} \left( \frac{F_d}{L_l} \right)^{-0.308} \left( e^{-0.1167 \frac{T_p}{D_m}} \right) \theta ^{0.35} & Re_{Lp} < 150 \\
\left( \frac{T_p}{D_m} \right)^{-0.0446} \log_{e} \left( 1.2 + \left( \frac{L_p}{F_p} \right)^{1.4} \right)^{-3.553} \theta ^{-0.477}  & 150 < Re_{Lp} < 5,000
\end{cases}
\end{equation}`


Hc heat transfer coefficient
----------------------------

It quantifies the rate of heat transfer between a solid surface (like a fin) and a surrounding fluid.

:math:`Hc = \frac{ J \rho V C_{p} }{P_{r}^{2/3} \sigma }`

Pressure drop
----------------

Reduction in pressure of the fluid as it flows through the heat exchanger due to the resistance to flow caused by the fins. 

:math:`P = 0.5 \frac{ 4 f \rho F_{d}}{D_{h} } \left(\frac{V}{ \sigma}\right ) ^{2}`

Fin-and-tube louver surface efficiency
----------------------------------------
  
Measure of how effectively a louver system can transfer heat between two fluids.


  
:math:`m = \sqrt{\frac{2 h_c}{k \delta}}`
        
:math:`\eta = \frac{\tanh(m F_l)}{m F_l}`

:math:`\eta_{overall} = 1 - \left(\frac{A_{fin}}{A_{total}}\right) (1 - \eta)`

------------------------------------------------------------------------

Example
--------

For the instance it is necessary to provide these values:

Fin parameters:

- k=Fin thermal conductivity coefficient [W/m-K]
- pitch=F_P [m]
- thickness=F_t δ fin thickness [m]
- depth= F_d fin depth [m]
- length= F_l fin length [m]

.. raw:: html
     
     <img src="./img/LFdF.jpg" alt="Description of the image" width="50%" height="auto">
     


Louver parameters:

- louver_pitch=L_p [m]
- louver_angle=θ (deg)
- louver_length=L_l [m]

.. raw:: html
     
     <img src="./img/LFL.jpg" alt="Description of the image" width="50%" height="auto">


Tube parameters:

- tube_depth=T_d [m]
- tube_pitch=T_p [m]
- outside_tube_diameter=Dm [m]


.. raw:: html
     
     <img src="./img/LFL.jpg" alt="Description of the image" width="50%" height="auto">


Air parameters:

- mu_air= μ air viscosity [kg/m-s]
- rho_air= ρ air density [kg/m^3]
- cp_air= gas specific heat [J/kg-K]
- Pr_air=Prandtl number 
- air_velocity=fan air speed [m/s]

Heat exchanger parameters:

- hx_length= Heat exchanger length, number of fins multiplied by fin pitch [m]

.. raw:: html

     
     <img src="./img/LFd.jpg" alt="Description of the image" width="100%" height="auto">
     <p><em>Figure 2: Schematic of a Louver fin with a flat tube <a href="https://www.sciencedirect.com/science/article/pii/0017931096001160">Y.J. Chang, C.C. Wang</a></em></p>

-----------------------------------------------------------------     

Implementation
-----------------

Input
------

Data provided by the user:

::

     from ccwht import LouverFinFlatTube as Lf
     louver=Lf(

     k=180,
     pitch=0.0018,
     thickness=0.00016,
     depth=0.022,
     lenght=0.016,

     louver_pitch=0.001318,
     louver_angle=28,
     louver_length=0.01244,

     tube_depth=0.022,
     tube_pitch=0.021,
     outside_tube_diameter=5e-3,


     mu_air=1.825e-5,rho_air=1.204,cp_air=1007,Pr_air=0.731,air_velocity=3,

     hx_lenght=0.018*60,)


Call the function
------------------

::

     J_Colburn_factor = louver.j
     friction_factor = louver.f
     heat transfer_coefficient=louver.h_c
     Pressure_drop=louver.pressure_drop
     efficiency=louver.eta_overall

Output
-------

Results obtained from the calculations:

::

     #Results
     J_Colburn_factor = 0.0259
     friction_factor = 0.147
     heat transfer_coefficient=129.0434
     Pressure_drop=29.0999
     efficiency=0.619

-----------------------------------------------------------------

Graphs
-------

The following graphs show the variation of the  friction factor, J Colburn factor, pressure drop, and heat transfer coefficient respect to Reynolds number and other parameters.


.. raw:: html
     
     <iframe src="./graph/fp_re_f.html" frameborder="0" scrolling="0" width="1000" height="700"></iframe>
     <p><em>Friction coefficient against Reynolds number &le; 150 and fin pitch </em></p>
     <iframe src="./graph/fp_re_f2.html" frameborder="0" scrolling="0" width="1000" height="700"></iframe>
     <p><em>Friction coefficient against Reynolds number &gt; 150 and fin pitch </em></p>
     <iframe src="./graph/la_re_f.html" frameborder="0" scrolling="0" width="1000" height="700"></iframe>
     <p><em>Friction coefficient against Reynolds number &le; 150 and louver angle </em></p>
     <iframe src="./graph/la_re_f2.html" frameborder="0" scrolling="0" width="1000" height="700"></iframe>
     <p><em>Friction coefficient against Reynolds number &gt; 150 and louver angle </em></p>
     <iframe src="./graph/fp_re_pd.html" frameborder="0" scrolling="0" width="1000" height="700"></iframe>
     <p><em>Pressure drop against Reynolds number &le; 150 and fin pitch </em></p>
     <iframe src="./graph/fp_re_pd2.html" frameborder="0" scrolling="0" width="1000" height="700"></iframe>
     <p><em>Pressure drop against Reynolds number &gt; 150 and fin pitch </em></p>
     <iframe src="./graph/fp_re_h.html" frameborder="0" scrolling="0" width="1000" height="700"></iframe>
     <p><em>Heat transfer coefficient against Reynolds number &le; 150 and fin pitch </em></p>
     <iframe src="./graph/fp_re_h2.html" frameborder="0" scrolling="0" width="1000" height="700"></iframe>
     <p><em>Heat transfer coefficient against Reynolds number &gt; 150 and fin pitch </em></p>

.. footer:: &copy; 2024 CC Wang Lab.



