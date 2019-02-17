import math

M = float(input("Please enter the m value: "))
B = float(input("Please enter the b value, no -: "))
X = int(input("Please enter the x value: "))


def cumulative_response(m_value, b_value, x_value):
    """Takes the M, B and X values submitted by the user and returns the cumulative responses"""
    cumulative_responses = 0

    while x_value > 0:
        cumulative_responses += m_value * math.exp(1 * (-b_value * x_value))
        x_value -= 1
    return cumulative_responses

print(cumulative_response(M, B, X))
