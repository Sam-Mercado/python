PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

WATER_DENSITY = 998.2  # kg/m^3


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    # Calculating pressure loss in the first part of the system
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)

    pressure -= pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure -= pressure_loss_from_fittings(velocity, quantity_angles)
    pressure -= pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)

    # Calculating pressure loss in the second part of the system
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    pressure -= pressure_loss_from_pipe(diameter, length2, friction, velocity)

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()

def water_column_height(tower_height, tank_height):
    column_height = tower_height + (3 * tank_height / 4)
    return column_height

def pressure_gain_from_water_height(height):
    density_of_water = WATER_DENSITY
    gravity = 9.80665  
    return (density_of_water * gravity * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    density_of_water = WATER_DENSITY
    return (-friction_factor * pipe_length * density_of_water * fluid_velocity**2) / (2000 * pipe_diameter)

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    lost_pressure_in_kilopascals= -0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings/ 2000
    return lost_pressure_in_kilopascals

def reynolds_number(hydraulic_diameter, fluid_velocity):
    r_number = WATER_DENSITY * hydraulic_diameter * fluid_velocity/ 0.0010016
    return r_number


def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter): 
    large_small_diameter = (larger_diameter / smaller_diameter) ** 4
    constant = 0.1 + 50 / reynolds_number * large_small_diameter - 1

    lost_pressure = - constant * WATER_DENSITY * fluid_velocity**2 / 2000
    return lost_pressure


if __name__ == "__main__":
    main()