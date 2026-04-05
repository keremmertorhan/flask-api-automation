"""
Testing module for my app
"""
from app import calculate_square

def test_calculate_square():
    """Test calculate_square function"""
    assert 4 == calculate_square(2)
