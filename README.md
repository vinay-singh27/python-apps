# Entity Sentiment Analysis


## Project Description
- An NLP-based web application through Justpy that extracts the entities and identifies the specific polarity of the entity in the text
- The pipeline uses the Spacy NER model to extract the entities. It then constructs auxiliary sentences to identify the dependent phrase for the entity using the roberta-base-squad2 QA model.
- Finally, it uses the roberta sentiment classifier to assign the polarity of the phrase


## Files and data description
<pre>
Folder Structure
.
├──api
│   ├──api.py
│   ├──documentation.py
│   ├──main.py
├──example
│   ├──main.py
│   ├──text.ipynb
├──test_results
├──webapp
│   ├──about.py
│   ├──home.py
│   ├──layout.py
│   ├──page.py
│   ├──sentiment.py
├──app_main.py
├──data_cleaning.py
├──sentiment_analysis.py

</pre>


## Running Files
<pre>
Step 1: Create Virtual Environment:
    - conda create --name sentiment_env python=3.8
    - conda activate sentiment_env
Step 2 : Install packages
    - conda install --file requirements.txt
Step 3 : Train Churn Model
    - python app_main.py
</pre>
