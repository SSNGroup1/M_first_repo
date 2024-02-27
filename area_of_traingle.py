class Triangle:
    def _init_ (self, base, height):
        self.base = base
        self.height = height
    def calculate_area(self):
        return 0.5 * self.base * self.height
base = float(input("Enter the base length of the triangle: "))
height = float(input("Enter the height of the triangle: "))
traingle =Triangle ( base, height)
area = traingle.calculate_area()
print("The area of the value is:", area)