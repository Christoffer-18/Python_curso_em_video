# Em inglês para treinar um pouco
'''def area():
    print("   Terrain control   ")
    print("-"*21)
    w = float(input("Width(m): "))
    l = float(input("Length(m): "))
    print(f"The area of a picie of lande {w:.2f}x{l:.2f} is {w*l:.2f}")

area()'''

# OR 

def area(width,length):
    print(f"The area of a picie of lande witch dimensions {w:.2f}x{l:.2f} is {w*l:.2f}m².")

print("   Terrain control   ")
print("-"*21)
w = float(input("Width(m): "))
l = float(input("Length(m): "))
area(w,l)