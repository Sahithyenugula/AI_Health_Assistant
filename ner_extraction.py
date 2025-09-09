from transformers import pipeline

def extract_named_entities(text):
    model_name = "d4data/biomedical-ner-all"
    nlp = pipeline(
        "ner", 
        model=model_name, 
        aggregation_strategy="simple"
    )
    entities = nlp(text)
    entities = [{"entity": ent["entity_group"], "word": ent["word"]} for ent in entities]
    return entities

if __name__ == "__main__":
    sample_text = "Patient diagnosed with diabetes and prescribed Metformin."
    sample_text1 = "Patient suffering from hypertension and was given Lisinopril."
    sample_entities = extract_named_entities(sample_text)
    sample_entities1 = extract_named_entities(sample_text1)
    print(sample_entities1)