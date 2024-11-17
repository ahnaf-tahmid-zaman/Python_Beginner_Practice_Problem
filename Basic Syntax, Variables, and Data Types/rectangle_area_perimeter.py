#Calculate the area and perimeter of a rectangle given its width and height.


width = float(input("Enter the width of the rectangle: "))
length = float(input("Enter the length of the rectangle: "))

print(f'Area = {width * length:.4f}\nPerimeter = {2 * (width + length):.4f}')
