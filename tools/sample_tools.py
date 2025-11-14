def calculator(expression):
    """
    A simple calculator that can perform basic arithmetic operations.
    """
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"

def get_weather(city):
    """
    Gets the weather for a given city.
    (This is a placeholder and does not actually fetch weather data)
    """
    return f"The weather in {city} is sunny."
