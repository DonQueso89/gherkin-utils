from setuptools import setup

setup(
    name="gherkin-utils",
    version="0.1",
    packages=["gherkin_utils"],
    # this requires a MANIFEST.in ( has no purpose now )
    include_package_data=True,
    # make setuptools aware of single file modules that are not part of an
    # import package
    py_modules=[],
    # minimal dependencies in order to run the project
    install_requires=["Click", "tabulate", "gherkin-official"],
    entry_points="""
        [console_scripts]
        gherkin2table=gherkin_utils.cli:gherkin_to_table
        gherkin2json=gherkin_utils.cli:gherkin_to_json
        ast_datatable2list=gherkin_utils.cli:ast_datatable_to_list
    """,
    python_requires=">=3.5",  # typing
    tests_require=["behave"],
    setup_requires=["setuptools_scm"],
    use_scm_version=True,
)
