import math

m_value = float(input("Please enter the m value: "))
b_value = float(input("Please enter the b value, no -: "))
x_value = int(input("Please enter the x value: "))


def cumulative_response(m, b, x):
    cumulative_responses = 0

    while x > 0:
        cumulative_responses += m * math.exp(1 * (-b * x))
        x -= 1
    return cumulative_responses

print(cumulative_response(m_value, b_value, x_value))
