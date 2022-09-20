'''
FASTAPI code to load the pretrained CHIA NER Model
'''

import time,random,string
from fastapi import FastAPI, Request
from typing import Optional, List
from pydantic import BaseModel
from pathlib import Path
import spacy
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class Content(BaseModel):
    post_url:str
    content: str

class Payload(BaseModel):
    data: List[Content]

class SingleEntity(BaseModel):
    text: str
    entity_type: str

class Entities(BaseModel):
    post_url: str
    entities : List[SingleEntity]

app = FastAPI()
nlp = spacy.load("en_chia_ner_pipeline_trf",
                 disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"]
                 )
# nlp = spacy.load("en_chia_ner_pipeline_trf",
#                  disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"]
#                  )

# default root path
@app.get('/')
def root():
    return {
        'message':  'SpaCy NER Model using FastAPI'
    }

@app.post('/ner')
def get_ner(payload: Payload):
    tokenize_content:List[spacy.tokens.doc.Doc] = [
        nlp(content.content) for content in payload.data
    ]
    document_entities = []
    for doc in tokenize_content:
        document_entities.append([{'text':ent.text, 'entity_type':ent.label_.upper()} for ent in doc.ents])
    return [
        Entities(post_url=post.post_url, entities=ents)
        for post, ents in zip(payload.data, document_entities)
    ]