print ("Hello, i will help you calculate the roots of a quadratic :)")

def solve1(a,b,c):
    y =((-b-(((b**2)-4*(a*c))**(1/2)))/(2*a))
    return y
def solve2(a,b,c):
    z = ((-b + (((b ** 2) - 4 * (a * c)) ** (1 / 2))) / (2 * a))
    return z

print(solve1(1,2,-3))
print(solve2(1,2,-3))