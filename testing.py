import pytest
from mycore_refactored import calculate_mean_duration, calculate_total_duration
from counting_crew_members import calculate_crew_size

def test_mean_duration():
    durations = [10, 15, 20, 5]
    expected = 12.5 / 60
    actual = calculate_mean_duration(durations)
    assert actual == pytest.approx(expected)

def test_total_duration():
    durations = [10, 15, 20, 5]
    expected = 50 / 60
    actual = calculate_total_duration(durations)
    assert actual == pytest.approx(expected)


def test_calculate_crew_size():
    total_duration = 8  # 8 hours
    mean_duration = 2  # 2 hours per crew member
    expected_crew_size = 4
    actual_crew_size = calculate_crew_size(total_duration, mean_duration)
    assert actual_crew_size == expected_crew_size