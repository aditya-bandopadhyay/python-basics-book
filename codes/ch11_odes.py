"""
ch10_odes.py

Simple ODE integration example using the forward Euler method for
dy/dt = -k * y with verbose names and clear comments.
"""

def euler_integrate_exponential_decay(
    initial_value: float,
    decay_rate: float,
    time_step: float,
    total_time: float
):
    """Return times and solution array for decay using Euler."""
    times = [0.0]
    solution_values = [initial_value]
    current_time = 0.0
    while current_time < total_time:
        current_value = solution_values[-1]
        derivative = -decay_rate * current_value
        next_value = current_value + derivative * time_step
        current_time += time_step
        times.append(current_time)
        solution_values.append(next_value)
    return times, solution_values


if __name__ == "__main__":
    t, y = euler_integrate_exponential_decay(1.0, 0.5, 0.1, 2.0)
    print("Final approximate value:", y[-1])
