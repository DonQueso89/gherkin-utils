import pytest
import transformations


@pytest.mark.parametrize("_input,output", [
    (["test1", "test2"], "| test1   | test2   |"),
    (["test1"], "| test1   |"),
    ([], ""),
])
def test_columns_to_gherkin_table_header(_input, output):
    assert transformations.columns_to_gherkin_table_header(_input) == output


def test_ast_from_gherkin_file_one_feature_one_scenario(tmpdir):
    fd = tmpdir.join("test")
    fd.write(
        """
        Feature: a test feature
            Scenario: a test scenario
    """
    )
    fd = fd.open()

    assert transformations.ast_from_gherkin_file(fd) == {
        "type": "GherkinDocument",
        "feature": {
            "type": "Feature",
            "tags": [],
            "location": {"line": 2, "column": 9},
            "language": "en",
            "keyword": "Feature",
            "name": "a test feature",
            "children": [
                {
                    "type": "Scenario",
                    "tags": [],
                    "location": {"line": 3, "column": 13},
                    "keyword": "Scenario",
                    "name": "a test scenario",
                    "steps": [],
                }
            ],
        },
        "comments": [],
    }


def test_ast_from_gherkin_file_one_feature_two_scenario_outlines(tmpdir):
    fd = tmpdir.join("test")
    fd.write(
        """
        Feature: a test feature
            Scenario Outline: a test scenario
            Given a dude

            Scenario Outline: another test scenario
            Given another dude
    """
    )
    fd = fd.open()

    assert transformations.ast_from_gherkin_file(fd) == {
        "type": "GherkinDocument",
        "feature": {
            "type": "Feature",
            "tags": [],
            "location": {"line": 2, "column": 9},
            "language": "en",
            "keyword": "Feature",
            "name": "a test feature",
            "children": [
                {
                    "type": "ScenarioOutline",
                    "tags": [],
                    "location": {"line": 3, "column": 13},
                    "keyword": "Scenario Outline",
                    "name": "a test scenario",
                    "steps": [
                        {
                            "type": "Step",
                            "location": {"line": 4, "column": 13},
                            "keyword": "Given ",
                            "text": "a dude",
                        }
                    ],
                    "examples": [],
                },
                {
                    "type": "ScenarioOutline",
                    "tags": [],
                    "location": {"line": 6, "column": 13},
                    "keyword": "Scenario Outline",
                    "name": "another test scenario",
                    "steps": [
                        {
                            "type": "Step",
                            "location": {"line": 7, "column": 13},
                            "keyword": "Given ",
                            "text": "another dude",
                        }
                    ],
                    "examples": [],
                },
            ],
        },
        "comments": [],
    }


def test_ast_from_gherkin_file_one_feature_one_scenario_outline_with_placeholders(
    tmpdir,
):
    fd = tmpdir.join("test")
    fd.write(
        """
        Feature: a test feature
            Scenario Outline: a test scenario
            Given a dude with a "<weapon>"  and a "<mammal>"
    """
    )
    fd = fd.open()

    assert transformations.ast_from_gherkin_file(fd) == {
        "type": "GherkinDocument",
        "feature": {
            "type": "Feature",
            "tags": [],
            "location": {"line": 2, "column": 9},
            "language": "en",
            "keyword": "Feature",
            "name": "a test feature",
            "children": [
                {
                    "type": "ScenarioOutline",
                    "tags": [],
                    "location": {"line": 3, "column": 13},
                    "keyword": "Scenario Outline",
                    "name": "a test scenario",
                    "steps": [
                        {
                            "type": "Step",
                            "location": {"line": 4, "column": 13},
                            "keyword": "Given ",
                            "text": 'a dude with a "<weapon>"  and a "<mammal>"',
                        }
                    ],
                    "examples": [],
                }
            ],
        },
        "comments": [],
    }
