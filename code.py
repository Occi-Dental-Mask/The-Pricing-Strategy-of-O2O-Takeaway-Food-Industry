from sympy import *
 
init_printing()
lambda1 = Symbol("lambda1")
theta = Symbol('theta')
w = Symbol('w')
t = Symbol('t')
Uc1=Symbol('Uc1')
Uc2 = Symbol('Uc2')
Us1 = Symbol('Us1')
Us2 = Symbol('Us2')
ps1 = Symbol('ps1')
ps2 = Symbol('ps2')
pc1 = Symbol('pc1')
pc2 = Symbol('pc2')
ps1 = Symbol('ps1')
nc1 = Symbol('nc1')
nc2 = Symbol('nc2')
ns1 = Symbol('ns1')
ns2 = Symbol('ns2')
ns = Symbol('ns')
nc = Symbol('nc')
x = Symbol('x')
y = Symbol('y')
m = Symbol('m')
n = Symbol('n')
Uc = Symbol('Uc')
Us = Symbol('Us')

eq1 = lambda1 * ns1 + theta * nc1 + w*theta*nc + w*lambda1*ns - t*x - pc1 - Uc1
eq2 = lambda1 * ns2 + theta * nc2 + w*theta*nc + w*lambda1*ns - t*(1-y) - pc2 - Uc2
eq3  = lambda1 * nc1 - theta * ns1 - w*theta*ns + w*lambda1*nc - t*m - ps1 - Us1
eq4 =  lambda1 * nc2 - theta * ns2 - w*theta*ns + w*lambda1*nc - t*(1-n) - ps2 - Us2
eq5 = lambda1 + theta - pc1 - pc2 - t - Uc
eq6 = lambda1 - theta - ps1 - ps2 - t - Us
eq7 = Uc1 - Uc
eq8 = m - ns1
eq9 =  1 - n - ns2
eq10 = x - nc1
eq11 = 1 - y - nc2 
eq12 = Uc2 - Uc
eq13 = Us1 - Us
eq14 = Us2 - Us
eq19 = nc - (y - x)
eq20 = ns - (n - m)

result = solve((eq1,eq2,eq3,eq4,eq5,eq6,eq7,eq8,eq9,eq10,eq11, eq12, eq13, eq14, eq19, eq20), (nc1,nc2,ns1, ns2,Us, Us2, Us1, Uc, Uc1, Uc2, Uc, m, n, x, y,nc,ns))

eq15 = diff(ps1*(1 - result[ns2]) + pc1*(1 - result[nc2]), ps1)
eq16 = diff(ps1*(1 - result[ns2]) + pc1*(1 - result[nc2]), pc1)
eq17 = diff(ps2*(1 - result[ns1]) + pc2*(1 - result[nc1]), ps2)
eq18 = diff(ps2*(1 - result[ns1]) + pc2*(1 - result[nc1]), pc2)
res = solve((eq15 ,eq16, eq17, eq18), (ps1, pc1, ps2, pc2, ns1, ns2, nc1, nc2,nc,ns))
print(latex(res[pc1]))
print(latex(res[ps1]))
print(latex(res[pc2]))
print(latex(res[ps2]))

