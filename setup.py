from setuptools import setup, find_packages


def get_readme_file():
    with open('README.md', 'r') as f:
        return f.read()


def get_requirements():
    with open('requirements.txt', 'r') as f:
        return f.read().splitlines()


setup(
    name='PyPromql',
    version='0.0.1',
    author='Aviv Levi',
    author_email='60aviv60@gmail.com',
    description='PyPromql is a Python library that simplifies the creation and execution of PromQL queries.',
    long_description=get_readme_file(),
    long_description_content_type='text/markdown',
    url='https://github.com/aviv-levi/pypromql.git',
    packages=find_packages(),
    install_requires=get_requirements(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='pypromql, py-promql, prometheus-query-builder, promql-query-builder',
    license='MIT',
)
