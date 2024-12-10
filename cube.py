# Function to calculate surface area and perimeter of a cuboid
def cuboid_area_and_perimeter(length, width, height):
    surface_area = 2 * (length * width + length * height + width * height)  # Surface area formula
    perimeter = 4 * (length + width + height)  # Perimeter formula
    return surface_area, perimeter

# Example usage
length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))

surface_area, perimeter = cuboid_area_and_perimeter(length, width, height)

print(f"The surface area of the cuboid is: {surface_area}")
print(f"The perimeter of the cuboid is: {perimeter}")
