import numpy as np
import pandas as pd

def get_sin_df(frequency: float|int=1, amplitude: float|int=1, period: float|int=2*np.pi, hshift: float|int=0, vshift: float|int=0):
    f = lambda x: np.sin(x)
    x_arr = np.arange(0 + hshift, period+0.02 + hshift, 0.1)
    y_arr = amplitude * f(frequency * x_arr ) + vshift
    df = pd.DataFrame(
        data=y_arr,
        index=x_arr,
        columns=["f(x) = sin(x)", ],
    )
    return df
