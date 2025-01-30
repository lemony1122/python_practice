def std_weight(height, gender):
    if gender == "male":
        return round(height*height*22*pow(0.01,2),2)
    else :
        return round(height*height*21*pow(0.01,2),2)

print(std_weight(175,"male"))