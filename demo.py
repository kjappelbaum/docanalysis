import os
from docanalysis import DocAnalysis
ethic_statement_creator = DocAnalysis()
dict_for_entities = ethic_statement_creator.extract_entities_from_papers(
    "ethics statement",
    10,
    os.path.join(
        os.getcwd(), "corpus", "ethics_statement_2",
    ),
    os.path.join(
        os.getcwd(), "ethics_dictionary", "ethics_key_phrases", "ethics_key_phrases.xml"
    ),
)
list_with_orgs = ethic_statement_creator.extract_particular_fields(
    dict_for_entities, 'ORG')
with open('org.text', 'w') as f:
    f.write(str(list_with_orgs))
list_with_gpe = ethic_statement_creator.extract_particular_fields(
    dict_for_entities, 'GPE')
with open('GPE.text', 'w') as f:
    f.write(str(list_with_gpe))
