#Cesar Murillo
#CIS 261
#Rectangle

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
    def calculate_perimeter(self):
        return 2 * (self.height +self.width)
    
    def calculate_area(self):
        return self.height * self.width

    def print_rectangle(self):
        for i in range(self.height):
            if i == 0 or i == self.height - 1:
                print('* ' * self.width)
            else:
                print('*' + ' ' * (self.width * 2 - 3) + '*')
                      
def main():

    print("Welcome to the Rectangle Maker!\n")
    again = "yes"

    while again.lower() == "yes":
        height = int(input("Please Enter The Height Of The Rectangle: "))
        width = int(input("Please Enther The Width Of The Rectangle: "))
        rect = Rectangle(height, width)
        print(f"Perimeter: {rect.calculate_perimeter()}")
        print(f"Area: {rect.calculate_area()}")
        print("\nHere's Your Rectangle!!!\n")
        rect.print_rectangle()
        again = input("\nWould You Like to Build Another Rectangle? (Yes/No): ")
    print("\nThank You for Using the Rectangle Maker!\n")
    
if __name__ == "__main__":
    main()
    


