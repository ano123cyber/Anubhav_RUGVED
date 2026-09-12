import matplotlib.pyplot as plt
import numpy as np


class ContinuousRobotTracker:

    def __init__(self, x=0.0, y=0.0, theta=0.0, dt=0.01):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt
        self.history = [(self.x, self.y, self.theta)]

    def execute_velocity_command(self, v, omega, duration):
        init_pos = f"({self.x:.2f}, {self.y:.2f}, {np.degrees(self.theta):.1f}°)"
        print(f"Initial State: {init_pos} | Executing: v={v}, omega={omega}, duration={duration}s" )
        steps = int(duration / self.dt)
        for _ in range(steps):
            self.x += v * np.cos(self.theta) * self.dt
            self.y += v * np.sin(self.theta) * self.dt
            self.theta += omega * self.dt
            self.theta = (self.theta + np.pi) % (2 * np.pi) - np.pi
            self.history.append((self.x, self.y, self.theta))
        final_pos = f"({self.x:.2f}, {self.y:.2f}, {np.degrees(self.theta):.1f}°)"
        print(f"Final State  : {final_pos}\n")

    def plot_trajectory(self):
        x_vals = [p[0] for p in self.history]
        y_vals = [p[1] for p in self.history]
        theta_vals = [p[2] for p in self.history]
        plt.figure(figsize=(8, 8))
        plt.plot(
            x_vals,
            y_vals,
            linestyle="-",
            color="royalblue",
            linewidth=2,
            label="Continuous Path",
        )
        quiver_skip = 50
        u = [np.cos(t) for t in theta_vals[::quiver_skip]]
        v = [np.sin(t) for t in theta_vals[::quiver_skip]]
        plt.quiver(
            x_vals[::quiver_skip],
            y_vals[::quiver_skip],
            u,
            v,
            color="crimson",
            scale=20,
            width=0.005,
            label="Heading (Quivers)",
        )
        plt.scatter(
            x_vals[0],
            y_vals[0],
            color="green",
            s=120,
            zorder=5,
            label=f"Start ({x_vals[0]:.1f}, {y_vals[0]:.1f})",
        )
        plt.scatter(
            x_vals[-1],
            y_vals[-1],
            color="black",
            s=120,
            zorder=5,
            label=f"End ({x_vals[-1]:.2f}, {y_vals[-1]:.2f})",
        )
        plt.title("Continuous Unicycle Model Trajectory", fontsize=14)
        plt.xlabel("X Position (meters)")
        plt.ylabel("Y Position (meters)")
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.legend(loc="upper left")
        plt.axis("equal")
        plt.show()
if __name__ == "__main__":
  # --- Replace your old block with this new interactive block ---
if __name__ == "__main__":
    robot = ContinuousRobotTracker(x=0.0, y=0.0, theta=0.0, dt=0.01)
    print("====================================================")
    print(" Continuous Unicycle Model Interactive Simulator ")
    print("====================================================")
    print("Provide movements using three numeric values separated by spaces.")
    print("Format: <v> <omega> <duration>")
    print("Type 'plot' or 'exit' when you are done to generate the map.\n")
    while True:
        raw_input = input("Enter command (v omega duration): ").strip()
        if raw_input.lower() in ["plot", "exit"]:
            print("\n--- Generating Continuous Curve Map ---")
            robot.plot_trajectory()
            break
        try:
            parts = raw_input.split()
            if len(parts) != 3:
                raise ValueError("Must provide exactly 3 numbers.")

            user_v = float(parts[0])
            user_omega = float(parts[1])
            user_duration = float(parts[2])

            if user_duration <= 0:
                print("Duration must be a positive number of seconds.")
                continue
            robot.execute_velocity_command(
                v=user_v, omega=user_omega, duration=user_duration
            )

        except ValueError:
            print(" Invalid Input! Enter three numbers separated by spaces: <v> <omega> <duration>")
    robot.plot_trajectory()
