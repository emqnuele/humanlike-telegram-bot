import random

def calculate_typing_delay(text):
    chars_per_second = 15
    base_delay = len(text) / chars_per_second
    variance = random.uniform(0.8, 1.2)
    delay = base_delay * variance
    
    return min(delay, 4.0)
