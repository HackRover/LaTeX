import math

# Define rover parameters
R = 0.1  # Radius of the wheels (assuming both wheels have the same radius)
L = 0.5  # Distance between the two wheels (wheelbase or track width)

# Initial position and orientation
x = 0.0
y = 0.0
theta = 0.0  # Angle in radians

# Control inputs (angular velocities of left and right wheels)
omegaL = 1.0  # Angular velocity of left wheel (radians per second)
omegaR = 1.5  # Angular velocity of right wheel (radians per second)

# Time step
dt = 0.1
omega = math.pi / 4  # Desired angular velocity (45 degrees per second)

# setting velocity to an initial value
v = (R / 2) * (omegaR + omegaL)
# calculate left and right angular velocities
omegaR = (2 * v + L * omega) / (2 * R)
omegaL = (2 * v - L * omega) / (2 * R)

# Calculate angular velocity
omega = (R / L) * (omegaR - omegaL)

# Update rover's position and orientation
x += v * math.cos(theta) * dt
y += v * math.sin(theta) * dt
theta += omega * dt

# Print updated position and orientation
print("Updated position (x, y):", x, y)
print("Updated orientation (theta):", theta)