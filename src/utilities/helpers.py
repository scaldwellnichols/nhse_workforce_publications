import re

def extract_month_year(text : str) -> str:
    """
    Extracts month-year pattern from a given text.

    For example, 
        'The report is for January-2021' ---> 'January-2021'
        'asdfgh-july-2025-asdf' ---> 'july-2025'
        'The report is for 2021' ---> 'No month-year found'

    Parameters
    ----------
    `text` : str
        Text to search for month-year pattern
    
    Returns
    -------
    str
        Month-year pattern if found, otherwise 'No month-year found'
    """
    # Regular expression to match month-year pattern
    pattern = r'(\b(january|february|march|april|may|june|july|august|september|october|november|december)-\d{4}\b)'
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(0)
    else:
        return 'No month-year found'