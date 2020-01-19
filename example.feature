Feature: Converting a feature file to a table
    Scenario Outline: Converting a file with a single Scenario Outline
        Given a datafile "<datafilename>" and a feature file "<featurefilename>"
        When we convert the featurefile to table format
        Then the table columns equal those in the feature file
        And the rows from the feature file "testfeature.feature" are in the table
    
    Scenario Outline: Do some stuff
        Given a "<filename>"
        And parameter "<another_parameter>"
        When we convert the featurefile to "<format>" format
        Then the table columns equal those in the feature file
        And the rows from the feature file "<filename>" are in the table
