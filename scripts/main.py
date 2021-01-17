# Calculates the amount of liquid in the jth glass of ith row when K litres


def calculate_liquid_volume(i, j, k):
    """
    i represents the number of rows, j the number of glasses and k the amount of liquid in litres
    :return: volume of liquid
    """

    # Initialised glass variable with the first index assuming that the number of glasses is rows * (rows+1) /2
    glass = [0] * int(i * (i + 1) / 2)
    index = 0
    glass[index] = k

# Loops through the glasses from the top to the bottom
    for row in range(1, i):
        for col in range(1, row + 1):
            k = glass[index]
            glass[index] = 1.0 if (k >= 1.0) else k
            k = (k - 1) if (k >= 1.0) else 0.0
            glass[index + row] += (k / 2)
            glass[index + row + 1] += (k / 2)
            index += 1

    return glass[int(i * (i - 1) / 2 + j - 1)]


if __name__ == "__main__":
    while True:
        try:
            i = int(input("Enter the value for row: "))
            j = int(input("Enter the number of the glass: "))
            k = float(input("Enter the amount of litres: "))
            if j > i:
                raise ValueError("Number of glasses cannot be greater than the number of rows")
        except Exception as e:
            print(e)

        res = repr(calculate_liquid_volume(i, j, k))
        print("The Volume of Liquid is: ", res.ljust(8, '0'))
        print("Press 'Ctrl+Z' or 'Command+Z' and the enter Key to break the loop")
