from pypromql.result.prometheus_result import PrometheusResult, Metric


def test_load_successfully_with_warnings():
    # arrange
    response = {
        'status': 'success',
        'data': {
            'resultType': 'vector',
            'result': [
                {
                    'metric': {
                        '__name__': 'scrape_duration_seconds',
                        'instance': 'localhost:9090',
                        'job': 'prometheus'
                    },
                    'value': [1686403514.415, '0.0145338']
                }
            ]
        },
        'warnings': 'x'
    }
    expected_status = 'success'
    expected_result_type = 'vector'
    expected_warnings = 'x'
    expected_metrics = [
        Metric(timestamp=1686403514.415,
               value=0.0145338,
               labels={
                   '__name__': 'scrape_duration_seconds',
                   'instance': 'localhost:9090',
                   'job': 'prometheus'
               })]
    # act
    result = PrometheusResult(prometheus_api_response=response)
    # assert
    assert result.status == expected_status \
           and result.result_type == expected_result_type \
           and result.metrics == expected_metrics \
           and result.warnings == expected_warnings


def test_load_failed_result_with_warnings():
    # arrange
    response = {
        'status': 'failed',
        'errorType': 'x',
        'error': 'x',
        'warnings': 'x'
    }
    expected_status = 'failed'
    expected_error_type = 'x'
    expected_error = 'x'
    expected_warnings = 'x'
    # act
    result = PrometheusResult(prometheus_api_response=response)
    # assert
    assert result.status == expected_status \
           and result.error_type == expected_error_type \
           and result.error == expected_error \
           and result.warnings == expected_warnings


def test_load_failed_result_without_warnings():
    # arrange
    response = {
        'status': 'failed',
        'errorType': 'x',
        'error': 'x'
    }
    expected_status = 'failed'
    expected_error_type = 'x'
    expected_error = 'x'
    # act
    result = PrometheusResult(prometheus_api_response=response)
    # assert
    assert result.status == expected_status \
           and result.error_type == expected_error_type \
           and result.error == expected_error \
           and not hasattr(result, 'warnings')


def test_load_successfully_result():
    # arrange
    response = {
        'status': 'success',
        'data': {
            'resultType': 'vector',
            'result': [
                {
                    'metric': {
                        '__name__': 'scrape_duration_seconds',
                        'instance': 'localhost:9090',
                        'job': 'prometheus'
                    },
                    'value': [1686403514.415, '0.0145338']
                }
            ]
        }
    }
    expected_status = 'success'
    expected_result_type = 'vector'
    expected_metrics = [
        Metric(timestamp=1686403514.415,
               value=0.0145338,
               labels={
                   '__name__': 'scrape_duration_seconds',
                   'instance': 'localhost:9090',
                   'job': 'prometheus'
               })
    ]

    # act
    result = PrometheusResult(prometheus_api_response=response)
    # assert
    assert result.status == expected_status \
           and result.result_type == expected_result_type \
           and result.metrics == expected_metrics
