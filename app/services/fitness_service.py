def calculate_bmi(weight, height):
    if height == 0:
        raise ValueError("Height cannot be zero")

    bmi = weight / (height * height)
    return round(bmi, 2)
