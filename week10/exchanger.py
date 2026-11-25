"""
The steam heat exchanger of Practice 6, Industrial AI, KBTU.

Treat it as the real plant: a black box you can only run. Its insides are not a first order plus
dead time model, which is the point of Task 6. Do not read the parameters out of it.

    t, Y, U = closed_loop(Kp, Ki, Kd, extra_dead_time=0.0)

runs the exchanger under the same PID as simulate_loop() in the notebook: a setpoint step of
+5 °C at t = 0, deviations from the operating point, valve limits -40 / +60 %.
Gains may be arrays.
"""
import numpy as np

_P = np.frombuffer(bytes.fromhex("9a9999999999e93f00000000008056400000000000003e400000000000002e40"), dtype=np.float64)

def _pid_loop(Kp, Ki, Kd, plant_step, n_states, d, t_end, dt, r, u_lo, u_hi):
    # PID (derivative on the measurement, filtered; anti-windup) on any plant.
    # plant_step(x, u) advances the state x (n_states, loops) by dt; the output is its
    # last row. d: dead time in steps. Gains may be arrays: one loop per element.
    # Returns t (steps,), Y and U (steps, loops).
    gains = [np.atleast_1d(np.asarray(g, float)) for g in (Kp, Ki, Kd)]
    Kp, Ki, Kd = np.broadcast_arrays(*gains)
    n = Kp.size
    steps = int(t_end / dt)
    Tf = Kd / np.maximum(Kp, 1e-9) / 10           # derivative filter time constant, s

    x = np.zeros((n_states, n))
    integral, deriv, y_prev = np.zeros(n), np.zeros(n), np.zeros(n)
    valve_queue = np.zeros((d + 1, n))            # commands on their way to the plant
    Y, U = np.zeros((steps, n)), np.zeros((steps, n))
    for k in range(steps):
        y = x[-1]
        e = r - y

        # filtered derivative of the measurement, then the command within the valve limits
        if k:
            deriv = (Tf * deriv - Kd * (y - y_prev)) / (Tf + dt)
        y_prev = y
        u_raw = Kp * e + integral + deriv
        u = np.clip(u_raw, u_lo, u_hi)

        # anti-windup: no integration towards a limit the valve already sits at
        winding = (u != u_raw) & (np.sign(e) == np.sign(u_raw))
        integral = integral + np.where(winding, 0.0, Ki * e * dt)

        # the plant sees the command sent d steps ago
        valve_queue = np.roll(valve_queue, -1, axis=0)
        valve_queue[-1] = u
        x = plant_step(x, valve_queue[0])
        Y[k], U[k] = x[-1], u
    return np.arange(1, steps + 1) * dt, Y, U


def _plant(extra_dead_time, dt):
    # The step function of the exchanger and its dead time in steps.
    K, T1, T2, L = _P
    a1, a2 = np.exp(-dt / T1), np.exp(-dt / T2)

    def step(x, u):                     # the second lag sees the first one's previous value
        x1 = a1 * x[0] + (1 - a1) * K * u
        x2 = a2 * x[1] + (1 - a2) * x[0]
        return np.stack([x1, x2])

    return step, int(round((L + extra_dead_time) / dt))


def closed_loop(Kp, Ki, Kd, extra_dead_time=0.0, r=5.0, t_end=900.0, dt=1.0,
                u_lo=-40.0, u_hi=60.0):
    step, d = _plant(extra_dead_time, dt)
    return _pid_loop(Kp, Ki, Kd, step, 2, d, t_end, dt, r, u_lo, u_hi)
