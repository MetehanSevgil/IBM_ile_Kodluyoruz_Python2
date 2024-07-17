import math 

def ouclide(x1: float, y1: float, x2:float, y2:float):
    # p = sqrt(q^2 + r^2)
    return math.sqrt((x2 -x1)**2 + (y2-y1)**2)

if __name__ == "__main__":
    A = (5.5, 6.6)
    B = (4.3, 5.7)
    p = ouclide(A[0], A[1], B[0], B[1])
    print(f"Ouclide: {p}")
