def cross_val_score(model: sklearn.base.BaseEstimator, X: pd.DataFrame, y: pd.Series, k: int = 5) -> List[float]:
    """Calculate the cross-validation score for the given model and data"""
    pass

def grid_search_cv(model: sklearn.base.BaseEstimator, X: pd.DataFrame, y: pd.Series, params: Dict[str, List[Any]]) -> Dict[str, Any]:
    """Perform grid search cross-validation for the given model and data"""
    pass
