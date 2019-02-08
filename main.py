import pygal
import numpy as np
import math


def oblicz_wartość(x):
    return math.sin(x)


def petla_obliczeniowa(pocz, konc, przedzialy):
    r_range = np.linspace(pocz, konc, przedzialy, endpoint=True)

    f_values = []
    for x in r_range:
        f_values.append(oblicz_wartość(x))

    pole1 = []
    for x, _ in enumerate(f_values[:-1]):
        result = (r_range[x+1] - r_range[x]) * f_values[x+1]
        pole1.append(result)

    pole2 = []
    for x, _ in enumerate(f_values[:-1]):
        result = (r_range[x+1] - r_range[x]) * f_values[x]
        pole2.append(result)

    return {
        'range': r_range,
        'f_values': f_values,
        'pole1': pole1,
        'pole2': pole2
    }


wyniki = petla_obliczeniowa(0, 3.14, 11)

line_chart = pygal.Line(human_readable=True)
line_chart.x_labels = wyniki['range']
line_chart.add('f(x)', wyniki['f_values'])
line_chart.render_to_file('linechart.svg')

print("Pole 1:", sum(wyniki['pole1']))
print("Pole 2:", sum(wyniki['pole2']))
print("Średnia:", (sum(wyniki['pole1']) + sum(wyniki['pole2'])) / 2)

