Edos Osazuwa 206647414

![[Pasted image 20240127194740.png]]1.
Ideal RAMJET - 
$$
p_{0a} = p_{02}= p_{04}= p_{06} , \space  T_{02}= T_{0a},\space,T_{04}=T_{06},\space \eta = 1 M_e = M_a\ , \ p_e = p_a
$$

$$
T_{04} = 2000[K] 
\longrightarrow 
T_4 = T_{04}\bigg(\frac{P_4}{P_{04}}\bigg)^{\frac{\gamma}{\gamma-1}} 
$$$$
T_{06} = 2000[K] 
\underset{ideal,p_6=p_e}{\longrightarrow} 
T_6 = \bigg(\frac{P_6}{P_{06}}\bigg)^{\frac{\gamma-1}{\gamma}}
$$$$
=T_{06}\bigg(\frac{P_e}{P_{06}}\bigg)^{\frac1{3.5}}
=T_{06}\bigg(\frac{15}{2277.5}\bigg)^{\frac1{3.5}}
=476[K]
$$
$$
T_{0a} = T_a(1+0.2M^2) = 250(1+0.2\cdot4^2) = 1050[K]
$$
$$
\frac{P_{0a}}{P_a} = (1+\frac{\gamma-1}{2}M_a^2)^\frac{\gamma}{\gamma-1} 
$$
$$P_{0a} = 15,000(1+0.2\cdot4^2)^{3.5} =2277.5[Kpa]$$

$$
f =
\frac{\frac{T_{04}}{T_{0a}}-1}{\frac{q_R}{C_pT_{0a}}-\frac{T_{04}}{T_{0a}}} =
\frac{1.9-1}{\frac{40\times10^6}{1000\cdot1050}-\frac{2000}{1050}}=0.025
$$

$$
U_a = M_a\sqrt{\gamma RT_a} =  1267[\frac ms]
$$
$$
U_e = \sqrt{\frac{T_{04}}{T_{0a}}}U_a = \sqrt{\frac{2000}{1050}}1050 = 1748[\frac{m}{s}]
$$
Therefore:
$$
\frac{F}{\dot m_a} =
(1+f)U_e-U_a+A_e(P_e-P_a)=
1.025\cdot 1748-1267+A_e(15,000-15,000)=
525[\frac{Ns}{kg}]
$$
$$
TSFC = \frac{f\cdot\dot m_a }{F} = \frac{0.025}{525}= 4.764\times10^{-5}[\frac{kg}{Ns}]
$$


![[Pasted image 20240127194658.png]]
$$
f(M), \ \frac{F}{\dot M_a}(M) , \ TSFC(M) 
$$
$$
50kft = 15240[m]
$$
$$
T_a = 220[K]
$$
$$
T_{4,max} = 2220[K]
$$
$$
\frac{P_{02}}{P_{01}} = 1-0.1(M_a-1)^{1.5} , M_a \ge1
$$
 $$
 \eta_{2,3} =0.97 \ \ , \eta_{3,4} =0.9 \ \ , \eta_{b} =0.98 \ \ ,\eta_{n} =0.95 \ \ 
 $$
 $$
 U_2 = U_3 = U_4 = 0
 $$
Solution:
What we want to find:
$$
f(M) =
\frac{\frac{T_{04}(M)}{T_{0a}(M)}-1}{\frac{q_R\eta_b}{C_pT_{0a}}-\frac{T_{04}}{T_{0a}}} =
$$
$$
\frac{F}{\dot m_a}(M) = (1+f)U_e(M)-Ua(M)+A_e(P_e(M)-P_a(M)) \underset{P_a = P_e}{=} (1+f)U_e(M)-Ua(M)
$$
$$
TSFC(M) = f(M)\cdot\frac{ \dot m_a}{F}(M)
$$

Property is equal to stagnation property when $U = 0$ Therefore:

$$
U_{2-4} = 0 \rightarrow T_4 = T_{04} = 2220[K]
$$
$$
T_{0a}(M) = 220(1+0.2M_a^2)
$$

$$
\frac{P_{0a}}{P_a}(M) = (1+\frac{\gamma-1}{2}M_a^2)^\frac{\gamma}{\gamma-1} 
$$
$$
\frac{P_{0e}}{P_{0a}} = r_d(M)r_cr_n
$$
 To find the effect of non ideal nozzle we assume isentropic and multiply by $\eta_n$:
 $$
T_{6s} = T_{04}(\frac{P_6}{P_{04}(M)})^{\frac{\gamma-1}{\gamma}} \longrightarrow T_6 = T_{06} - (T_{06} - T_{6s})\eta_n
 $$
 We can now calculate $Ua$ , $Ue$ :
 $$
 U_a(M) = \sqrt{\gamma RT_a}Ma
 $$
 $$
U_e = \sqrt{2C_P(T_{04} - T_6)}  
$$
Graphs:
$$\frac{F}{\dot m}[\frac{kgf}{kg/sec}]:$$

![[F to mdot to ma.png]]

$$TSFC[\frac{kg}{hr/kgf}]:$$![[TSFC to Ma.png]]
$$f:$$
![[f to ma 1.png]]
![[Pasted image 20240127194718.png]]
$$
T_a = 220[K],
T_04 = 2200[K]
$$
$$r_c = \frac{P_{04}}{P_{02}}=0.95 \ , \ r_n = \frac{P_{06}}{P_{04}}=0.96$$
$$\frac{P_{02}}{P_{0a}} = 0.9 \ , \ f<<1 $$
For positive thrust calculate:
$$M_{max} = ? \ , \ M_{min} = ?$$
The thrust equation:
$$\frac{F}{\dot m} = (1+\underset{\sim0}{f})U_e-Ua +\frac{1}{\dot m_a}(P_e-P_a)A_e\underset{coordinated}{=}Ue-Ua$$
$$
U_a = M_a\sqrt{\gamma RT_a} \, \ U_e
$$
$$
U_e = M_e\sqrt{\frac{\gamma R T_{04}}{1+\frac{\gamma -1}{2}M_e^2}}
$$
$$
M_e = \sqrt{\frac{2}{\gamma -1}(m-1)}
$$
Where
$$
m = (1+\frac{\gamma-1}{2}M_a^2)(r_dr_cr_n\frac{P_a}{P_e})^{\frac{\gamma-1}{\gamma}} 
$$
We could derive the expression for $\frac{F}{\dot m}$ analytically or write code to find the points of $\frac{F}{\dot m} = 0$.
Plotting Yields:
![[q3.png]]
Therefore $0.58<M<6.3$
Max mach number is a function of $T_{04} , T_a$ , the effect is that Mach will be higher as $T_{04}$ is increasing and lower as $T_a$ is increasing. 
![[Pasted image 20240127194726.png]]![[Pasted image 20240204091449.png]]
The Ramjet engine has A very wide range of capabilities and is very versatile  

Code:
main:
```
import pandas as pd  
import Isentropic_utils as isen  
import non_ideal_Ram  
import math  
import non_ideal_Ram as ram  
import numpy as np  
import matplotlib.pyplot as plt  
out_arr = []  
# dict_arr = {}  
M_arr = np.linspace(1,5,100)  
for M in M_arr:  
Ta = 220  
Pa = Pe = 12000  
q_R = 42e6  
M_arr = np.linspace(1,10,100)  
rd = 1-0.1*(M-1)**1.5  
r2_3 = 0.97  
r3_4 = 0.9  
rc = r2_3*r3_4  
rn = 0.95  
eta_b = 0.98  
U2 = U3 = U4 = 0  
C_p1 = C_p2 = 1000  
C_p3 = C_p4 = C_p5 = C_p6 = 1200  
gamma_1 = gamma_2 = 1.4  
gamma_3 = gamma_4 = gamma_5 = gamma_6 = 1.3  
#sol  
T0a = isen.calc_T0(gamma = gamma_1 , mach=M , T=Ta)  
P0a = isen.calc_P0(P=Pa , gamma= gamma_1 ,mach = M )  
T04 = T4 = T06 = 2220  
f1 = ram.calc_f(T04=T04 , T0a = T0a , q_R=q_R,eta=eta_b,C_p=C_p1)  
f4 = ram.calc_f(T04=T04 , T0a = T0a , q_R=q_R,eta=eta_b,C_p=C_p4)  
  
Me = ram.calc_mach_e(gamma = gamma_6 , M = M , eta = rd*rd*rn , Pa = Pa , Pe = Pe)  
Ua = ram.calc_U(M = M , gamma = gamma_1,R = 287 , T = Ta)  
T = isen.calc_T(1.4,4,2000)  
T0 = isen.calc_T0(1.4,4,T)  
P0 = isen.calc_P0(1.4,4,15000)  
P = isen.calc_P(1.4,4,P0)  
P02 = rd*P0a  
P03 = r2_3 * P02  
P04 = r3_4 * P03  
# P6 = isen.calc_P(gamma_6 , mach=M , P0 = P06)  
  
T6s = T06*(Pa/P04)**((gamma_6-1)/gamma_6)  
T6 = T06 - (T06 - T6s)*rn  
Ue = (2*C_p6*(T04-T6))**0.5  
F_to_m_Dot = ram.calc_TSFC(f = f1,U_e = Ue,U_a = Ua , m_dot_a = 1,P_e = 0,P_a = 0,A_e = 0)  
TSFC = 3600*f1/F_to_m_Dot  
# out_arr.append({'M':M,'P0a':P0a ,'P02':P02,'P03':P03,'P04':P04,"T6s":T6s,'T6':T6,'Ua':Ua,'Ue':Ue,'f1':f1,'F_to_m_Dot':F_to_m_Dot,'TSFC':TSFC})  
out_arr.append([M,P0a ,P02,P03,P04,T6s,T6,Ua,Ue,f1,F_to_m_Dot,TSFC])  
out_arr = np.array(out_arr)  
out_arr = {'M':out_arr[:,0],'P0a':out_arr[:,1] ,'P02':out_arr[:,2],'P03':out_arr[:,3],  
'P04':out_arr[:,4],"T6s":out_arr[:,5],'T6':out_arr[:,6],'Ua':out_arr[:,7],'Ue':out_arr[:,8],  
'f1':out_arr[:,9],'F_to_m_Dot':out_arr[:,10],'TSFC':out_arr[:,11]}  
  
data = pd.DataFrame(out_arr)  
# plt.figure()  
# plt.plot(data['M'] , data["TSFC"])  
# plt.ylabel('TSFC[kg/hr/kgf]')  
# plt.xlabel('Ma')  
# plt.grid()  
# plt.show()  
#  
# plt.figure()  
# plt.plot(data['M'] , data["f1"])  
# plt.ylabel('f')  
# plt.xlabel('Ma')  
# plt.grid()  
# plt.show()  
#  
# plt.figure()  
# plt.ylabel('F/m_dot[kgf/kg/sec]')  
# plt.xlabel('Ma')  
# plt.plot(data['M'] , data["F_to_m_Dot"])  
# plt.grid()  
# plt.show()  
  
  
# Question 3  
rc_3 = 0.95  
rn_3 = 0.96  
rd_3 = 0.9  
M_3_arr = np.linspace(0.55 , 10 , 1000)  
data_3 = []  
gamma = 1.4  
R = 287  
for M_3 in M_3_arr:  
Me_3= non_ideal_Ram.calc_mach_e(gamma = 1.4 , M = M_3 , eta = rn_3*rd_3*rc_3 , Pa = 1 , Pe = 1)  
Ua_3 =non_ideal_Ram.calc_U(M = M_3 ,gamma = 1.4 , R = 287 , T = 220)  
Ue_3 = non_ideal_Ram.calc_Ue(M = Me_3 ,gamma = 1.4 , R = 287 , T04 = 2200)  
F_to_m_Dot = Ue_3-Ua_3  
data_3.append(F_to_m_Dot)  
# F_M_DOT = math.sqrt((2*gamma*R*2200*(0.945+0.189*M_3**2 - 1)) / ((gamma-1)*(0.945+0.189*M_3**2))) - M_3*math.sqrt(gamma*R*220)  
# data_3.append(F_M_DOT)  
  
plt.figure()  
plt.plot(M_3_arr,data_3)  
plt.grid()  
plt.ylabel('F/m_dot[kgf/kg/sec]')  
plt.xlabel('Ma')  
plt.show()
```
insentropic eq module:
```
def calc_P(gamma,mach,P0):  
return P0/(1+((gamma-1)/2)*mach**2) ** (gamma/(gamma-1))  
def calc_P0(gamma, mach, P):  
return P * (1 + ((gamma - 1) / 2) * mach ** 2) ** (gamma / (gamma - 1))  
  
def calc_T(gamma,mach,T0):  
return T0/(1+((gamma-1)/2)*mach**2)  
def calc_T0(gamma, mach, T):  
return T * (1 + ((gamma - 1) / 2) * mach ** 2)  
  
  
def calc_mach(gamma,prop,prop_stag , T_P):  
if T_P == 'T':  
return (prop_stag/prop - 1 / ((gamma-1) / 2))**0.5  
elif T_P == 'P':  
return ((prop_stag/prop)**((gamma-1)/gamma) - 1 / ((gamma-1) / 2))**0.5  
pass
```
non ideal ram module
```
def calc_f (T04,T0a,q_R,C_p,eta):  
return (T04/T0a-1) / ( (q_R*eta/(C_p*T0a)) - (T04/T0a) )  
  
def calc_Ue(gamma,R,T04,M):  
return M * (gamma*R*T04 / (1+((gamma-1)/2) * (M**2)) )**0.5  
  
def calc_TSFC(f,U_e,U_a , m_dot_a,P_e,P_a,A_e):  
return ((1+f)*U_e - U_a + 1/m_dot_a * (P_e-P_a)*A_e) / 9.81  
  
def calc_U(M,gamma,R,T):  
return M*(gamma*R*T)**0.5  
  
def calc_mach_e(gamma , M , eta , Pa , Pe):  
return ((2/(gamma-1))*((1+((gamma-1)/2)*M**2 * (eta*Pa/Pe))**((gamma-1)/gamma)-1))**0.5
```