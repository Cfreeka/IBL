import pytest
from datetime import datetime

from validator_collection.validators import timedelta


def calculate_age_in_minutes():
    pass


def test_age_in_minutes():
    # Test case 1: Birth date is today
    datetime.now().strftime("%Y-%m-%d")
    assert calculate_age_in_minutes() == 0

    # Test case 2: Birth date is exactly 1 year ago
    (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")
    assert calculate_age_in_minutes() == 525600

    # Test case 3: Birth date is 18 years ago
    (datetime.now() - timedelta(days=365 * 18)).strftime("%Y-%m-%d")
    assert calculate_age_in_minutes() == 9460800

    # Test case 4: Birth date is in the future
    with pytest.raises(ValueError):
        (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d")
        calculate_age_in_minutes()
