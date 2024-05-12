def time_series_forecast(data: pd.DataFrame, model: sklearn.base.BaseEstimator, horizon: int = 1) -> pd.Series:
    """Forecast the given time series data using the given model and horizon"""
    pass

def anomaly_detection(data: pd.DataFrame, model: sklearn.base.BaseEstimator) -> List[int]:
    """Detect anomalies in the given data using the given model"""
    pass
