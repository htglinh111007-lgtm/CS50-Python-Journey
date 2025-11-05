def main():
    a = mass_to_float(input("Enter your weight: "))
    b = height_to_float(input("Enter your height: "))
    bmi = a/(b*b)
    if bmi <= 18.5:
        status = "(Underweight)"
    elif bmi > 18.5 and bmi <= 22.9:
        status = "(Normal)"
    elif bmi >=23 and bmi<= 24.9:
        status = "(Overweight)"
    elif bmi >= 25 and bmi <= 29.9:
        status = "(Pre-obesity)"
    elif bmi >=30:
        status = "(Obesity)"
    print (f"Your BMI is {bmi:.2f} "+ status)
def mass_to_float(m):
    return float(m.replace("kg",""))
def height_to_float(h):
    return float(h.replace("m",""))
main()