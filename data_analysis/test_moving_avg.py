import numpy as np

from .data_analysis import moving_average

#Define test for moving_avgerage
def test_moving_avg():
    a = moving_average(np.ones(10),4)
    assert np.all(np.isnan(a[:2]))
    assert np.all(np.isnan(a[-2:]))
    assert np.allclose(a[4:-4], 1)


