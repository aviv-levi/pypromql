PyPromql - Python PromQL Query Builder
=======================================

.. _intro_start:

|Docs|  |PyPi|  |License|

Abstract
--------

What is |Brand|?

|Brand| is a Python library that simplifies the creation and execution of PromQL queries.
With |Brand|, developers can effortlessly construct and run PromQL queries with ease and simplicity.
It provides a convenient and intuitive interface for working with Prometheus Query Language (PromQL).

.. _intro_end:

Read the docs: http://pypromql.readthedocs.io/en/latest/

Installation
------------

.. _installation_start:

To install |Brand| run the following command:

.. code-block:: bash

    pip install pypromql


.. _installation_end:


Tutorial
--------

.. _tutorial_start:

The main classes in pypromql are ``pypromql.query.Query`` and ``pypromql.result.PrometheusResult``.

.. code-block:: python

    from pypromql.query import Query
    from pypromql.result import PrometheusResult


Create simple query
^^^^^^^^^^^^^^^^^^^
The entry point for building queries is ``pypromql.query.Query``.


.. code-block:: python

    promql_query = Query.metric('up').label('job', 'prometheus')


.. code-block:: promql

    up{job="prometheus"}

To convert the query into raw PromQL, it can be cast to a string.

.. code-block:: python

    str(promql_query)

Alternatively, you can use the `to_promql()` function:

.. code-block:: python

    promql_query.to_promql()

Execute query
^^^^^^^^^^^^^^^^^^^
First, we need to create a ``pypromql.PrometheusConnection``.

.. code-block:: python

    connection = PrometheusConnection(prometheus_base_url='http://my-host-name:my-port/')
    
Then, we execute our query and get the result using ``PrometheusResult.from_query_builder``.

.. code-block:: python

    result = PrometheusResult.from_query_builder(promql_query, connection)


.. _appendix_start:

.. |Brand| replace:: *PyPromql*

.. _appendix_end:

.. _available_badges_start:

.. |Docs| image:: https://readthedocs.org/projects/pypromql/badge/?version=latest
   :target: http://pypromql.readthedocs.io/en/latest/
.. |PyPi| image:: https://img.shields.io/pypi/v/pypromql.svg?style=flat
   :target: https://pypi.python.org/pypi/pypromql
.. |License| image:: https://img.shields.io/bower/l/p
   :target: https://opensource.org/license/mit/

.. _available_badges_end:
