import random

def calculate_typing_delay(text):
    """
    Calculates a realistic typing delay based on text length.
    
    Args:
        text (str): The text to be sent.
        
    Returns:
        float: The delay in seconds.
    """
    # Average typing speed: ~5-10 characters per second?
    # Let's say 0.05 to 0.1 seconds per character.
    chars_per_second = 15 # Fast typer so its not a boomer
    base_delay = len(text) / chars_per_second
    
    # Add some randomness
    variance = random.uniform(0.8, 1.2)
    delay = base_delay * variance
    
    # Cap the delay as requested (max 3-5 seconds)
    return min(delay, 4.0)
