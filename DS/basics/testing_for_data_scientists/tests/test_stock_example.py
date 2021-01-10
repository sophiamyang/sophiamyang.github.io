from stock_example import get_data, stock_plot, neg_sharpe_ratio, optimize_sharpe_ratio
from datetime import datetime
import pandas as pd
from pandas.testing import assert_frame_equal
from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt
import pytest
from numpy.testing import assert_almost_equal, assert_array_almost_equal
from hypothesis import given
from hypothesis.extra.pandas import column, data_frames, range_indexes
import hypothesis.strategies as st

# TEST INPUT DATA 
def test_stock_data():
    # what we get from the function
    tickers = ['GOOGL', 'TSLA'] 
    start_date = '2020-01-02'
    end_date = '2020-01-03'
    df_func = get_data(tickers, start_date, end_date)  
    # what we expect     
    d = {
        'Date': [datetime(2020,1,2)], 
        'GOOGL': [1368.680054], 
        'TSLA': [86.052002]
        }
    df_truth = pd.DataFrame(data=d).set_index('Date')
    # make sure they are the same
    assert_frame_equal(df_func, df_truth)   

@pytest.fixture
def load_data():
    # what we get from the function
    tickers = ['AAPL','GOOGL', 'TSLA']  
    start_date = '2019-01-02'
    end_date = '2020-01-03'
    df_func = get_data(tickers, start_date, end_date)  
    return df_func 

def test_load_data(load_data):
    # verify the shape and cell values of input data
    df = load_data
    assert df.shape == (253, 3)
    assert df.notnull().values.any() == True
    assert (df>0).values.any() == True
    assert (df.columns == ['AAPL', 'GOOGL', 'TSLA']).any() == True

# TEST VISUALIZATION
@pytest.mark.mpl_image_compare(remove_text=True, tolerance=3)
def test_stock_plot(load_data):
    plot = stock_plot(load_data)
    return plot

# TEST DATA PROCESSING
@pytest.mark.parametrize('allocation, expected', [
    ([0.1, 0.2, 0.7], -0.0756), 
    ([0.9, 0.1, 0], -0.1648),
    ([0.1, 0.8, 0.1], -0.0955)
])
def test_sharpe_ratio(load_data, allocation, expected):
    """test function neg_sharpe_ratio"""
    # get our input data
    df = load_data
    # calculate neg sharpe ratio from function 
    sharpe_ratio_func = neg_sharpe_ratio(allocation, df)
    # verify it's the same as expected
    assert_almost_equal(sharpe_ratio_func, expected, decimal=3)

# # TEST MODEL
@pytest.mark.parametrize('tickers, start_date, end_date, expected', [
    (['AAPL','GOOGL', 'TSLA'], '2019-01-02', '2020-01-03', [1, 0, 0]),
    (['AAPL','AMZN','MSFT','NVDA'], '2019-05-02', '2020-01-03', [0.64, 0, 0.35, 0])
])
def test_optimization(tickers, start_date, end_date, expected):
    # get input date 
    df = get_data(tickers, start_date, end_date)  
    # optimize sharpe ratio from function
    optimized_allocations_func = optimize_sharpe_ratio(df)
    # verify if it's the same as expected
    assert_array_almost_equal(optimized_allocations_func, expected, decimal=2)

@given(
    data_frames([
    column('StockA', dtype=int, unique=True),
    column('StockB', dtype=int, unique=True),
    column('StockD', dtype=int, unique=True),
    column('StockC', dtype=int, unique=True)
    ],
    rows=st.tuples(
        st.integers(min_value=1e2, max_value=int(1e3)),
        st.integers(min_value=1e2, max_value=int(1e4)),
        st.integers(min_value=1e3, max_value=int(1e5)),
        st.integers(min_value=1e5, max_value=int(1e6))
    ),
    index=range_indexes(min_size=8)
    )
)
def test_optimization_allocation(df):
    # verify if the sum of the allocations are always 1 
    allocations = optimize_sharpe_ratio(df)
    print(allocations)
    assert_almost_equal(sum(allocations), 1, decimal=1)