import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path


g = 9.81
x0, y0 = 0 , 50
v0x, v0y = 5, 10

t_land = (v0y + np.sqrt(v0y**2 + 2*g*y0))/g

t = np.linspace(0, t_land, 50)

x = x0 + v0x*t
y = y0 + v0y*t - 0.5*g*t**2

print("total time ", t_land)
print("max height ", y.max())
print("range ", x.max())

plt.plot(x, y, color = 'navy', linestyle = 'dashed', marker = 'o')
plt.xlim(0, y.max()+5)
plt.ylim(0, y.max()+5)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid(True)
plt.savefig(Path(__file__).parent / 'projectile.png', dpi=150, bbox_inches='tight')
plt.show()
