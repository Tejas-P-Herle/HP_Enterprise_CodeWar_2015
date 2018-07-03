from math import sqrt


def main():
    
    # Get input
    side = float(input())

    # Calculate basic components for calculation
    area_of_triangle = ((3**(1/2) * side**2) / 4)
    height_of_triangle = (area_of_triangle * 2) / side
    height = (side ** 2) - ((height_of_triangle * 2 / 3) ** 2)
    height = sqrt(height)

    # Calculate surface area
    surface_area = 4 * area_of_triangle

    # Calculate volume
    volume = (1/3) * area_of_triangle * height

    # Print surface area and volume of triangular pyramid
    print("Surface Area: {:0.2f} square units.".format(surface_area))
    print("Volume: {:0.2f} cubic units.".format(volume))

if __name__ == "__main__":
    main()