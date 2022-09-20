from typing import List, Dict
from ...main import id_nlp


def get_entities(sentence) -> List[Dict]:
    doc = id_nlp(sentence)
    print(doc)
    for ent in doc.ents:
        print(ent.text, ent.start_char,ent.end_char, ent.label_)
    return (ent.text, ent.start_char,ent.end_char, ent.label_)