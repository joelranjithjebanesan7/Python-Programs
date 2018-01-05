def get_circle_area(radius):
    
    area=(22/7)*radius*radius
    return area

r = eval(input("Enter the radius:"))
area = get_circle_area(r)
print(area)
