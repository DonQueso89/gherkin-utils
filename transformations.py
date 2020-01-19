import re
from gherkin.parser import Parser
from gherkin.token_scanner import TokenScanner
from typing import Set, TextIO, List
from tabulate import tabulate


def ast_from_gherkin_file(fd: TextIO) -> dict:
    """Parse a file with a gherkin document into an Abstract Syntax Tree

    Parameters
    ----------
    fd : file-like object
        filedescriptor of file containing gherking document

    Returns
    -------
    ast : dict
        a dictionary representation of the gherkin file as returned
        by gherkin.parser.Parser.parse
    """
    fd.seek(0)
    return Parser().parse(TokenScanner(fd.read()))


def placeholders_from_scenario_outline(scenario_outline: dict) -> Set[str]:
    """Parse all placeholders from a Scenario Outline

    Parameters
    ----------
    scenario_outline : dict
        representation of a Scenario outline as returned by
        gherkin.parser.Parser.parse

    Returns
    -------
    placeholders : Set[str]
    """
    placeholders = set()
    for step in scenario_outline["steps"]:
        placeholders |= set(re.findall(r"<(\w+)>", step["text"]))

    return placeholders


def columns_to_gherkin_table_header(columns: List[str]) -> str:
    """Convert a set of columns to a Gherkin table header

    Parameters
    ----------
    columns : List[str]
        the column names of the table

    Returns
    -------
    table : str
        table representation that can be pasted into a Gherkin file
        the empty string if columns is empty
    """
    if columns:
        return tabulate([], headers=columns, tablefmt="github").splitlines()[0]
    return ""
