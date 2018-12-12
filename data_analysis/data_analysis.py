"""
These are data anaysis functions to download and process temperature series from Berkeley Earth.
"""

#Import Libraries
import numpy as np
import requests

#Define loading functions
def generate_URL(place):
    """
    This function will generate the string of the URL to access the temperature data

    :param place: Location of temperature time series
    """
    url = f'http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/{place.lower()}-TAVG-Trend.txt'
    return url

def download_data(place):
    """
    This function will download the content of the URL 
    """
    url = generate_URL(place)
    response = requests.get(url)

    data = np.loadtxt(response.iter_lines(), comments="%")
    return data


#Define processing functions
def moving_average(data, width):
    moving_avg = np.full(data.size, np.nan)
    for i in range(width, moving_avg.size - width):
        moving_avg[i] = np.mean(data[i - width:i + width])
    return moving_avg


