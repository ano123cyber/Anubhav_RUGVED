import matplotlib.pyplot as plt
import numpy as np

class RobotTracker:
    def __init__(self, x=0.0, y=0.0, theta=0.0):
        self.x = x
        self.y = y
        self.theta = theta
        self.history = [(self.x, self.y, self.theta)]

    def execute_single_command(self, cmd_str):
        cmd_str = cmd_str.strip()
        if not cmd_str:
            return True
            
        try:
            action, val_str = cmd_str.split()
            val = float(val_str)
        except ValueError:
            print("Invalid format! Use: forward <val>, left <val>, or right <val>")
            return True

        init_pos = f"({self.x:.2f}, {self.y:.2f}, {np.degrees(self.theta):.1f}°)"
        action_lower = action.lower()
        
        valid_action = False
        
        if action_lower == "forward":
            self.x += val * np.cos(self.theta)
            self.y += val * np.sin(self.theta)
            valid_action = True
        elif action_lower == "left":
            self.theta += np.radians(val)
            valid_action = True
        elif action_lower == "right":
            self.theta -= np.radians(val)
            valid_action = True
        else:
            print(f"Unknown action: '{action}'")
            
        if valid_action:
            self.theta = (self.theta + np.pi) % (2 * np.pi) - np.pi
            self.history.append((self.x, self.y, self.theta))
            final_pos = f"({self.x:.2f}, {self.y:.2f}, {np.degrees(self.theta):.1f}°)"
            print(f" Initial Pos: {init_pos} | Executing: {cmd_str} | Final Pos: {final_pos}\n")
            
        return True


    def plot_trajectory(self):
        x_vals = [p[0] for p in self.history]
        y_vals = [p[1] for p in self.history]
        theta_vals = [p[2] for p in self.history]

        plt.figure(figsize=(8, 8))

        plt.plot( x_vals, y_vals, linestyle="-", color="blue", alpha=0.5, label="Trajectory Path" )

        u_vectors = [np.cos(t) for t in theta_vals]
        v_vectors = [np.sin(t) for t in theta_vals]
        
        first_arrow = True
        for i in range(len(self.history)):
            is_start = (i == 0)
            is_last = (i == len(self.history) - 1)
            
            # PERFECT CORNER CHECK:
            # Detects a corner state if the robot changed its heading angle 
            # while remaining stationary at the same physical position coordinate.
            is_turning_point = False
            if i > 0 and i < len(self.history):
                same_coord_as_prev = (x_vals[i] == x_vals[i-1] and y_vals[i] == y_vals[i-1])
                diff_angle_from_prev = (theta_vals[i] != theta_vals[i-1])
                if same_coord_as_prev and diff_angle_from_prev:
                    is_turning_point = True

            # Drop arrows cleanly at the Start, all Intermediate Corners, and the final End marker
            if is_start or is_turning_point or is_last:
                lbl = "Robot Heading" if first_arrow else ""
                first_arrow = False
                color = "red" if is_last else "purple"
                
                plt.quiver(
                    x_vals[i], y_vals[i], u_vectors[i], v_vectors[i], 
                    color=color, scale=15, width=0.005, label=lbl, zorder=6
                )


        # Draw the final tracking heading arrow at the very last location
        plt.quiver(
            x_vals[-1], y_vals[-1], 
            np.cos(theta_vals[-1]), np.sin(theta_vals[-1]), 
            color="red", scale=15, width=0.005
        )


        plt.scatter(
            x_vals[0], y_vals[0], color="green", s=100, zorder=5, label=f"Start ({x_vals[0]:.1f}, {y_vals[0]:.1f})")
        plt.scatter(
            x_vals[-1], y_vals[-1], color="red", s=100, zorder=5, label=f"End ({x_vals[-1]:.2f}, {y_vals[-1]:.2f})")

        plt.title("Robot Trajectory Mapping", fontsize=14)
        plt.xlabel("X Position")
        plt.ylabel("Y Position")
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.legend(loc="upper left")
        plt.axis("equal")
        plt.show()

if __name__ == "__main__":
    robot = RobotTracker(x=0.0, y=0.0, theta=0.0)
    print(" Robot Tracker Initialised! Starting at (0.0, 0.0, 0.0°)")
    print("Commands: 'forward <val>', 'left <val>', 'right <val>'")
    print("Type 'plot' or 'exit' to finish and see the graph.\n")

    while True:
        user_input = input("Enter command: ")
        if user_input.strip().lower() in ["plot", "exit"]:
            print("\nGenerating final trajectory plot...")
            robot.plot_trajectory()
            break
        robot.execute_single_command(user_input)

