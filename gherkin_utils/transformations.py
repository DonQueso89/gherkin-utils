import json
import re
from typing import List, Set, TextIO, Tuple

from gherkin.parser import Parser
from gherkin.token_scanner import TokenScanner
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


def list_from_ast_datatable(ast_datatable: dict) -> List[dict]:
    """Convert a gherkin AST DataTable representation to a list of dict

    Parameters
    ----------
    ast_datatable : dict
        representation of a DataTable outline as returned by
        gherkin.parser.Parser.parse

    Returns
    -------
    list representation of DataTable : List[dict]
    """
    result = []
    payload = ast_datatable['rows'][::-1]  # copy and reverse
    headers = [x['value'] for x in payload.pop()['cells']]
    while payload:
        result.append(dict(
            zip(
                headers,
                [x['value'] for x in payload.pop()['cells']]
            )
        ))
    return result


def columns_to_gherkin_table(columns: List[str], table_data=None) -> str:
    """Convert a set of columns to a Gherkin table header

    Parameters
    ----------
    columns : List[str]
        the column names of the table
    table_data : List[Tuple]
        optional records to add to the table, in the order of the columns

    Returns
    -------
    table : str
        table representation that can be pasted into a Gherkin file
        the empty string if columns is empty
    """
    if table_data is None:
        table_data = []
    if columns:
        table = tabulate(table_data, headers=columns, tablefmt="github").splitlines()
        return "\n".join([table[0]] + table[2:])
    return ""
