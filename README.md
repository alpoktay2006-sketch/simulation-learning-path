\# Simulation Learning Path



My journey learning simulation for flight dynamics and robotics, using Simulink and Python. The goal is to build up to a 6DOF rocket flight simulator.



\## Repository structure

\- `simulink/`: Simulink models

\- `python/`: Python scripts



\## Simulink models



\### Mass-spring-damper (`MassDampedSpring.slx`)

Solves m·x'' = F − c·x' − k·x with m = 2 kg, c = 2 N·s/m, k = 20 N/m. The response to a step force oscillates and settles at F/k.



\### PD-controlled cars (`PD\_Control2Cars.slx`)

Car 1 drives at a constant 10 m/s from x = 50 m. Car 2 starts at rest and uses a PD controller on the position error to catch up with car 1 and match its speed. Kp = 1,  Kd = 2.



\## Python scripts



\### Projectile motion (`python/projectile-motion.py`)

A projectile launched from 50 m with 5 m/s horizontal and 10 m/s vertical speed, simulated with NumPy and plotted with Matplotlib. Flight time is about 4.4 s and the peak height about 55 m.



!\[Projectile trajectory](python/projectile.png)

