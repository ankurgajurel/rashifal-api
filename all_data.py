from bs4 import BeautifulSoup
import requests

base = "https://hamropatro.com/rashifal"

def get_rashifal(work_url):
    """ unites function to get scrape a specific element

    Args:
        work_url (str): this is the url to the API

    Returns:
        str: unicode of the rashifal nepali
    """
    response = requests.get(work_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    return_rashifal = soup.find('div', {'class': 'desc'}).find('p').text

    return return_rashifal

def get_daily(rashi):
    """daily rashifal

    Args:
        rashi (str): which rashi

    Returns:
        dict: rashifal message
    """
    work_url = base + "/daily/" + rashi
    daily_rashifal = get_rashifal(work_url)

    return {"daily_rashifal" + "_" + rashi: daily_rashifal}

def get_monthly(rashi):
    """monthly rashifal

    Args:
        rashi (str): which rashi

    Returns:
        dict: rashifal message
    """
    work_url = base + "/monthly/" + rashi
    monthly_rashifal = get_rashifal(work_url)

    return {"daily_rashifal" + "_" + rashi: monthly_rashifal}
    
def get_yearly(rashi):
    """yearly rashifal

    Args:
        rashi (str): which rashi

    Returns:
        dict: rashifal message
    """
    work_url = base + "/yearly/" + rashi
    yearly_rashifal = get_rashifal(work_url)

    return {"daily_rashifal" + "_" + rashi: yearly_rashifal}