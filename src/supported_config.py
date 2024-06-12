# Candidate Extraction
supported_extraction_methods = ['action-object', 'action-object-ext', 't0pp-prompting']
extraction_prompt_template = "Given the following utterance: %s. The intent was to"

# Intent Label Generation
supported_label_generation_methods = ['most-frequent', 't0pp-prompting']
ilg_prompt_template = "Given these utterances: %s. What is the best fitting intent, if any, among the following: %s"