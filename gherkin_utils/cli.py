import json

import click

from gherkin_utils import transformations


@click.command()
@click.argument("path_to_feature_file")
@click.option(
    "--path_to_datafile",
    help="Absolute path to JSON file with records to add to the table",
    default=None,
)
def gherkin_to_table(path_to_feature_file: str, path_to_datafile: str):
    """Convert a 1 or more ScenarioOutlines from a feature file to gherkin tables
       that can be pasted into the Examples section of the ScenarioOutline
    """
    with open(path_to_feature_file) as fd:
        data = None
        if path_to_datafile is not None:
            data = json.load(open(path_to_datafile))

        ast = transformations.ast_from_gherkin_file(fd)

        for scenario in ast["feature"]["children"]:
            if scenario["type"] == "ScenarioOutline":
                click.echo("Table for ScenarioOutline '" + scenario["name"] + "'")
                headers = transformations.placeholders_from_scenario_outline(scenario)
                if data is not None:
                    data = [[row[h] for h in headers] for row in data]

                click.echo(
                    transformations.columns_to_gherkin_table(headers, table_data=data,)
                )
                click.echo()


@click.command()
@click.argument("path_to_feature_file")
def gherkin_to_json(path_to_feature_file: str):
    """Convert a complete gherkinfile to the JSON representation of its AST
    """
    with open(path_to_feature_file) as fd:
        ast = transformations.ast_from_gherkin_file(fd)
        click.echo(json.dumps(ast))


@click.command()
@click.argument("datatable")
def ast_datatable_to_list(datatable: str):
    """Convert an AST datatable representation to a JSON list of objects
    """
    click.echo(
        json.dumps(transformations.list_from_ast_datatable(json.loads(datatable)))
    )
