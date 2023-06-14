PyPromql - Python PromQL Query Builder
=======================================

# Abstract

###  What is PyPromql?

PyPromql is a Python library that simplifies the creation and execution of PromQL queries.
With PyPromql, developers can effortlessly construct and run PromQL queries with ease and simplicity.
It provides a convenient and intuitive interface for working with Prometheus Query Language (PromQL).

# Installation

To install PyPromql run the following command:

```bash
    pip install pypromql
```

# Tutorial
The main classes in pypromql are ``pypromql.query.Query`` and ``pypromql.result.PrometheusResult``.

```python
    from pypromql.query import Query
    from pypromql.result import PrometheusResult
```

## Create simple query

The entry point for building queries is ``pypromql.query.Query``.

```python
    promql_query = Query.metric('up').label('job', 'prometheus')
```

```promql
    up{job="prometheus"}
```

To convert the query into raw PromQL, it can be cast to a string.

```python
    str(promql_query)
```
Alternatively, you can use the `to_promql()` function:

```python
    promql_query.to_promql()
```

## Execute query

First, we need to create a ``pypromql.PrometheusConnection``.

```python
    connection = PrometheusConnection(prometheus_base_url='http://my-host-name:my-port/')
```    
Then, we execute our query and get the result using ``PrometheusResult.from_query_builder``.

```python
    result = PrometheusResult.from_query_builder(promql_query, connection)
```
