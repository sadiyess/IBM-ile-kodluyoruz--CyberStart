import math

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def get_point_from_user(label):
    x = float(input("{}. noktanın x koordinatını girin: ".format(label)))
    y = float(input("{}. noktanın y koordinatını girin: ".format(label)))
    return (x, y)

def main():
    print("İlk noktayı girin:")
    point1 = get_point_from_user("1")
    print("İkinci noktayı girin:")
    point2 = get_point_from_user("2")
    distance = euclideanDistance(point1, point2)
    print("Noktalar arasındaki mesafe:", distance)

if __name__ == "__main__":
    main()