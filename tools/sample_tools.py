from googlesearch import search

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

def web_search(query):
    """
    Performs a web search using Google and returns the top 5 results.
    Use this to find information on the internet.
    """
    try:
        search_results = []
        for j in search(query, num=5, stop=5, pause=2):
            search_results.append(j)
        return search_results
    except Exception as e:
        return f"Error: {e}"
