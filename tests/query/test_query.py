from pypromql.query.prometheus_query import Query
from datetime import datetime


def test_simple_query():
    # arrange
    metric_name = 'scrape_duration_seconds'
    # act
    query = Query.metric(metric_name=metric_name)
    # assert
    assert metric_name == str(query)


def test_equal_label_query():
    # arrange
    expected_query = 'scrape_duration_seconds{job="prometheus"}'
    metric_name = 'scrape_duration_seconds'
    label_name = 'job'
    label_value = 'prometheus'
    # act
    query = Query.metric(metric_name=metric_name).label(label_name=label_name, label_value=label_value)
    # assert
    assert expected_query == str(query)


def test_not_equal_label_query():
    # arrange
    expected_query = 'scrape_duration_seconds{job!="prometheus"}'
    metric_name = 'scrape_duration_seconds'
    label_name = 'job'
    label_value = 'prometheus'
    # act
    query = Query.metric(metric_name=metric_name).label(label_name=label_name,
                                                        label_value=label_value,
                                                        match_operator='!=')
    # assert
    assert expected_query == str(query)


def test_between_datetime_query():
    # arrange
    expected_query = 'scrape_duration_seconds[1672531200s:1672617600s]'
    metric_name = 'scrape_duration_seconds'
    start_time = datetime(year=2023, month=1, day=1, hour=0, minute=0, second=0)
    end_time = datetime(year=2023, month=1, day=2, hour=0, minute=0, second=0)
    # act
    query = Query.metric(metric_name=metric_name).between_datetime(start_time=start_time, end_time=end_time)
    # assert
    assert expected_query == str(query)


def test_before_time_duration_query():
    # arrange
    expected_query = 'scrape_duration_seconds[5m]'
    metric_name = 'scrape_duration_seconds'
    time_duration = '5m'
    # act
    query = Query.metric(metric_name=metric_name).before_time_duration(time_duration=time_duration)
    # assert
    assert expected_query == str(query)


def test_offset_query():
    # arrange
    expected_query = 'scrape_duration_seconds offset 5m '
    metric_name = 'scrape_duration_seconds'
    offset_modifier = '5m'
    # act
    query = Query.metric(metric_name=metric_name).offset(offset_modifier=offset_modifier)
    # assert
    assert expected_query == str(query)
