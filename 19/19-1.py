import sympy as sp
def z_transform_unit_step():
    z = sp.symbols('z')
    n = sp.symbols('n', integer=True)
    u_n = sp.Heaviside(n) # Unit step function
    z_transform = sp.summation(u_n * z**(-n), (n, 0, sp.oo))
    return z_transform
z_transform_result = z_transform_unit_step()
print(f"Z-transform of the unit step function: {z_transform_result}")
