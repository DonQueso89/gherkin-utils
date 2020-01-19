import click
import transformations


@click.command()
@click.argument("path_to_feature_file")
@click.option(
    "--datafile",
    help="Absolute path to JSON file with records to add to the table",
    default=None,
)
def gherkin2table(path_to_feature_file: str, datafile: str):
    """Convert a 1 or more ScenarioOutlines from a feature file to gherkin tables
       that can be pasted into the Examples section of the ScenarioOutline
    """
    if datafile is not None:
        raise NotImplementedError('passing data to table is not yet implemented')

    with open(path_to_feature_file) as fd:
        ast = transformations.ast_from_gherkin_file(fd)
        for scenario in ast["feature"]["children"]:
            if scenario["type"] == "ScenarioOutline":
                click.echo("Table for ScenarioOutline '" + scenario["name"] + "'")
                click.echo(
                    transformations.columns_to_gherkin_table_header(
                        transformations.placeholders_from_scenario_outline(
                            scenario
                        )
                    )
                )
                click.echo()


if __name__ == '__main__':
    gherkin2table()
