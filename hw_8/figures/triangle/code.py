def triangle_perimeter(a,b,c):
    return a+b+c


def triangle_area(a,b,c):
    p=triangle_perimeter(a,b,c)/2
    return round((p*(p-a)*(p-b)*(p-c))**0.5,2)