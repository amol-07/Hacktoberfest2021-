# Volume of Triangular Pyramid
def volumeTriangular(a, b, h):
	return (0.1666) * a * b * h

# Function To calculate
# Volume of Square Pyramid
def volumeSquare(b, h):
	return (0.33) * b * b * h

# Function To calculate Volume
# of Pentagonal Pyramid
def volumePentagonal(a, b, h):
	return (0.83) * a * b * h

# Function To calculate Volume
# of Hexagonal Pyramid
def volumeHexagonal(a, b, h):
	return a * b * h


# Driver Code
b = float(4)
h = float(9)
a = float(4)
print( "Volume of triangular base pyramid is ",
					volumeTriangular(a, b, h) )
print( "Volume of square base pyramid is ",
					volumeSquare(b, h) )
print( "Volume of pentagonal base pyramid is ",
					volumePentagonal(a,b, h) )
print( "Volume of Hexagonal base pyramid is ",
					volumeHexagonal(a, b, h))
