from setuptools import setup, find_packages

setup(
    name='gherkin-utils',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['cli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        gherkin2table=cli:gherkin2table
        gherkin2json=cli:gherkin2json
        readable_datatable=cli:readable_datatable
    ''',
)
