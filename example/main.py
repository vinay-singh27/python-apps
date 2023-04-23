import spacy
import pandas as pd
nlp = spacy.load("en_core_web_lg")

# doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

doc = nlp("Tesla is performing great and General Motors is performing bad")
result = []
for ent in doc.ents:
    result.append([ent.text, ent.label_])

result_df = pd.DataFrame(result, columns=['text', 'label'])
d = []
for idx, row in result_df.iterrows():
    d.append(f"{row['text']}  {row['label']}")

d = "\n".join(d)
print(d)
