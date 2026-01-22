# tests/test_model.py
import pytest
from app.model import predict

# check that prediction is an integer
def test_predict_returns_int():
    features = [5.1, 3.5, 1.4, 0.2]
    prediction = predict(features)
    assert isinstance(prediction, int)

# check that prediction is within expected range for iris dataset
def test_predict_output_range():
    features = [5.1, 3.5, 1.4, 0.2]
    prediction = predict(features)
    assert prediction in [0,1,2]

# Check that invalid input length raises an error
def test_predict_invalid_input_length():
    features = [1,2]  
    with pytest.raises(ValueError):
        predict(features)
