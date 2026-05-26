
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

print("Polinomio de grado 5")
print("Forma: ax^5 + bx^4 + cx^3 + dx^2 + ex + f\n")

a = float(input("Coeficiente de x^5: "))
b = float(input("Coeficiente de x^4: "))
c = float(input("Coeficiente de x^3: "))
d = float(input("Coeficiente de x^2: "))
e = float(input("Coeficiente de x: "))
f = float(input("Término independiente: "))
x = sp.symbols('x')
polinomio = a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f
print("\nEl polinomio es:")
texto = str(sp.expand(polinomio)).replace("**", "^")
print("f(x) =", texto)

# RAÍCES
coeficientes = [a, b, c, d, e, f]
raices = np.roots(coeficientes)
print("\nLas raíces son:")
for i, r in enumerate(raices):
    print(f"Raíz {i+1}: {r}")

# DERIVADAS
d1 = sp.diff(polinomio, x)
d2 = sp.diff(d1, x)
d3 = sp.diff(d2, x)
d4 = sp.diff(d3, x)
d5 = sp.diff(d4, x)

print("\nLas primeras 5 derivadas son:")
print("\nPrimera derivada:")
texto = str(sp.expand(d1)).replace("**", "^")
print("f'(x) =", texto)
print("\nSegunda derivada:")
texto = str(sp.expand(d2)).replace("**", "^")
print("f''(x) =", texto)
print("\nTercera derivada:")
texto = str(sp.expand(d3)).replace("**", "^")
print("f'''(x) =", texto)
print("\nCuarta derivada:")
texto = str(sp.expand(d4)).replace("**", "^")
print("f''''(x) =", texto)
print("\nQuinta derivada:")
texto = str(sp.expand(d5)).replace("**", "^")
print("f'''''(x) =", texto)

# PUNTOS CRÍTICOS
criticos = sp.solve(d1, x)
print("\nPuntos críticos:")

for punto in criticos:
    print(punto)


# MÁXIMOS Y MÍNIMOS
print("\nMáximos y mínimos:")
maximos = []
minimos = []
for punto in criticos:
    if punto.is_real:
        segunda_eval = d2.subs(x, punto)
        y = polinomio.subs(x, punto)
        if segunda_eval > 0:
            print(f"\nMínimo local en x = {sp.N(punto)}")
            print(f"f(x) = {sp.N(y)}")
            minimos.append(float(punto))
        elif segunda_eval < 0:
            print(f"\nMáximo local en x = {sp.N(punto)}")
            print(f"f(x) = {sp.N(y)}")
            maximos.append(float(punto))
        else:
            print(f"\nEn x = {sp.N(punto)} no se puede clasificar.")


# CRECIMIENTO Y DECRECIMIENTO
print("\nIntervalos de crecimiento y decrecimiento:")
criticos_reales = []
for c1 in criticos:
    if c1.is_real:
        criticos_reales.append(float(c1))
criticos_reales.sort()
intervalos = []
if len(criticos_reales) == 0:
    print("No existen puntos críticos reales.")
    intervalos.append((-np.inf, np.inf))
else:
    intervalos.append((-np.inf, criticos_reales[0]))
    for i in range(len(criticos_reales)-1):
        intervalos.append((criticos_reales[i],
                            criticos_reales[i+1]))
    intervalos.append((criticos_reales[-1], np.inf))

for inter in intervalos:
    a1, b1 = inter
    if a1 == -np.inf:
        prueba = b1 - 1
    elif b1 == np.inf:
        prueba = a1 + 1
    else:
        prueba = (a1 + b1)/2
    valor = d1.subs(x, prueba)
    if valor > 0:
        print(f"La función CRECE en ({a1}, {b1})")
    elif valor < 0:
        print(f"La función DECRECE en ({a1}, {b1})")

# CONCAVIDAD
print("\nConcavidad:")
inflexion = sp.solve(d2, x)
inflexion_reales = []
for p in inflexion:
    if p.is_real:
        inflexion_reales.append(float(p))
inflexion_reales.sort()
intervalos2 = []
if len(inflexion_reales) == 0:
    print("No existen puntos de inflexión reales.")
    intervalos2.append((-np.inf, np.inf))
else:
    intervalos2.append((-np.inf, inflexion_reales[0]))
    for i in range(len(inflexion_reales)-1):
        intervalos2.append((inflexion_reales[i],
                             inflexion_reales[i+1]))
    intervalos2.append((inflexion_reales[-1], np.inf))
for inter in intervalos2:
    a2, b2 = inter
    if a2 == -np.inf:
        prueba = b2 - 1
    elif b2 == np.inf:
        prueba = a2 + 1
    else:
        prueba = (a2 + b2)/2
    valor = d2.subs(x, prueba)
    if valor > 0:
        print(f"Cóncava hacia ARRIBA en ({a2}, {b2})")
    elif valor < 0:
        print(f"Cóncava hacia ABAJO en ({a2}, {b2})")
f_numpy = sp.lambdify(x, polinomio, modules=['numpy'])

# INTEGRAL
print("\n Aproximqcion de la integral, metodo simpson")
a_int = float(input("Límite inferior: "))
b_int = float(input("Límite superior: "))
n = int(input("Número de intervalos (debe ser par): "))
if n % 2 != 0:
    print("El número de intervalos debe ser PAR")
else:

    h = (b_int - a_int) / n
    suma = f_numpy(a_int) + f_numpy(b_int)
    for i in range(1, n):
        x_i = a_int + i*h
        if i % 2 == 0:
            suma += 2 * f_numpy(x_i)
        else:
            suma += 4 * f_numpy(x_i)
    integral = (h/3) * suma
    print("\nLa aproximación de la integral es:")
    print(integral)     

# GRÁFICA

f_numpy = sp.lambdify(x, polinomio, modules=['numpy'])
x_vals = np.linspace(-3,3,1000)
y_vals = f_numpy(x_vals)
plt.figure(figsize=(10,6))
plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='black')
plt.axvline(0, color='black')
for punto in maximos:
    plt.plot(punto,
             f_numpy(punto),
             'ro',
             label='Máximo')
for punto in minimos:
    plt.plot(punto,
             f_numpy(punto),
             'go',
             label='Mínimo')
plt.title("Gráfica del polinomio")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(-2,2)
plt.ylim(-20,20)
plt.grid(True)
plt.legend()

plt.show()
