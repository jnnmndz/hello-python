import geometry


def triangle_perimeter (a, b, c):
    return (a+b+c)

def triangle_heronsarea(a, b, c):
    P = (a+b+c)
    A =(s*(s-a)*(s-b)*(s-c)) ** 0.5
    return A

data = input("Enter the side lengths of a triangle: ")

triangle = int(data)

#print("Perimeter of Triangle: {} "
#.format(geometry.triangle_perimeter(P)))