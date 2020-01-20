import click
import transformations
import json


@click.command()
@click.argument("path_to_feature_file")
@click.option(
    "--path_to_datafile",
    help="Absolute path to JSON file with records to add to the table",
    default=None,
)
def gherkin2table(path_to_feature_file: str, path_to_datafile: str):
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
                    transformations.columns_to_gherkin_table(
                        headers,
                        table_data=data,
                    )
                )
                click.echo()


if __name__ == '__main__':
    gherkin2table()
