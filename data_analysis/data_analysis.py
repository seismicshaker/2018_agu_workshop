"""
These are data anaysis functions to download and process temperature series from Berkeley Earth.
"""

#Import Libraries
import numpy as np
import requests

#Define loading functions
def generate_URL(place):
    url = f'http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/{place.lower()}-TAVG-Trend.txt'
    return url

def download_data(place):
    # Download the content of the URL
    url = generate_URL(place)
    response = requests.get(url)

    data = np.loadtxt(response.iter_lines(), comments="%")
    return data


#Define processing functions
def moving_avgerage(data, width):
    moving_avg = np.full(data.size, np.nan)
    for i in range(width, moving_avg.size - width):
        moving_avg[i] = np.mean(data[i - width:i + width])
    return moving_avg


#Define test for moving_avgerage
def test_moving_avg():
    a = moving_avgerage(np.ones(10),4)
    assert np.all(np.isnan(a[:2]))
    assert np.all(np.isnan(a[-2:]))
    assert np.allclose(a[4:-4], 1)


