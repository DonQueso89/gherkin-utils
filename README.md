# Gherkin-utils
Utilities for working with Gherkin feature files and step implementation modules

### Application structure

The main idea is to have a module with pure functions that only implement
transformations on data. These transformations can be used through Coconut
function composition inside the entrypoint that exposes these (complex) transformations 
as a CLI (taking args or input from stdin) and writes the result to stdout.

By using well defined data formats, such as the gherkin Parser AST representation
and tablib.Dataset objects, these functions can make reliable assumptions about
the structure and API of the data they are operating on.

### Cool stuff used here

* Property-based testing
* BDD
* Coconut

### Roadmap

- [ ] Given a feature file with one or more ScenarioOutlines, output a column header
      that can be pasted into a Gherkin file as Examples table for each ScenarioOutline.
      Each header must be mappable to its ScenarioOutline
- [ ] Same as the previous feature, but include records from a datafile in any
      format in the output table, defaulting to None
- [ ] Given a feature file, generate a Python module of stub implementations with the
      correct imports, decorators and matching patterns passed to the decorator
