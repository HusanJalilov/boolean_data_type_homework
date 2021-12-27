import math
def main(a):
    """To Check if a number is a perfect square or not
    Args:
        a: int
    Returns:
        bool
    """
    x=math.sqrt(a)
    # Write your code here
    return  int(x+0.5)**2==a