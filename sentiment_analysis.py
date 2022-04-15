# import libraries
import sys
import spacy
from spacy import displacy
import pandas as pd
from scipy.special import softmax
import warnings
# import transformers
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
from transformers import AutoModelForSequenceClassification
# import utilis functions
from data_cleaning import data_cleaning

warnings.filterwarnings('ignore')


class PredictSentiment:

    def __init__(self):

        # define data cleaning dictionary
        self.data_cleaning_params = {'htmldecode': True,
                                     'remove_tags': True,
                                     'remove_hashtags': True,
                                     'remove_links': True,
                                     'remove_punct': False,
                                     'contraction_correction': False,
                                     'slang_correction': False,
                                     'replace_emoji': False,
                                     'replace_repeat': False,
                                     'remove_stopwds': False,
                                     'remove_non_ascii': True,
                                     'remove_RT': True,
                                     }

        # initialize scibert and attach UMLs Entity Linker
        print("initializing spacy")
        self.nlp = spacy.load("en_core_web_lg")
        print("Successfully Loaded spacy en_core_web_lg")

        # initialize RoBERTa base SQUAD model
        print("initializing RoBERTa base SQUAD model")
        model_name = "deepset/roberta-base-squad2"
        self.nlp_qa = pipeline('question-answering', model=model_name, tokenizer=model_name)
        self.qa_model = AutoModelForQuestionAnswering.from_pretrained(model_name)
        self.qa_tokenizer = AutoTokenizer.from_pretrained(model_name)
        print("Successfully RoBERTa base SQUAD model")

        # initialize roberta sentimental analysis(sa) model
        self.sa_roberta_tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
        self.sa_roberta_model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base"
                                                                                   "-sentiment")
        print("Successfully RoBERTa sentimental analysis(sa) model")

    def data_processing(self, tweet_dataframe):
        """
        This method preprocess the input dataframe.
        The data cleaning pipeline can be controlled using
        the initializing variable
        :param tweet_dataframe: input dataframe
        :return: prepared_dataframe with added Clean_text column
        """

        tweet_dataframe['Clean_text'] = tweet_dataframe['content']
        tweet_dataframe['Clean_text'] = tweet_dataframe['Clean_text'].apply(
            lambda x: data_cleaning(x, **self.data_cleaning_params))

        # drop exact duplicate clean texts
        prepared_dataframe = tweet_dataframe.drop_duplicates(subset=['Clean_text'])

        return prepared_dataframe

    def extract_entities(self, clean_text):
        """

        :param clean_text:
        :return:
        """

        # identify the entities in the dataset
        entity_results = []
        doc = self.nlp(clean_text)
        for ent in doc.ents:
            entity_results.append([ent.text, ent.label_])

        # create dataframe of the entities
        entity_df = pd.DataFrame(data=entity_results, columns=['Entity', 'Type'])
        entity_df['Clean_text'] = clean_text

        return entity_df

    def extract_entity_dependent_phrase(self, dataframe):
        """

        :param dataframe:
        :return:
        """

        dataframe.reset_index(drop=True, inplace=True)
        results = []
        for idx, row in dataframe.iterrows():
            # create QA input
            qa_input = {'question': f"what do you think about {row['Entity']}",
                        'context': row['Clean_text']}

            # predict from the QA model
            res = self.nlp_qa(qa_input)
            result_qa_m = [res['answer'], res['score']]

            results.append(result_qa_m)

        results_df = pd.DataFrame(results, columns=['Answer', 'Answer_Score'])
        dataframe = pd.concat([dataframe, results_df], axis=1)
        dataframe = dataframe[dataframe['Answer_Score'] > 0.1]

        return dataframe

    def roberta_sentiment_analysis(self, text):

        encoded_input = self.sa_roberta_tokenizer(text, return_tensors='pt')
        output = self.sa_roberta_model(**encoded_input)
        scores = output[0][0].detach().numpy()
        return softmax(scores)

    def extract_roberta_sentiment(self, dataframe):

        dataframe['Roberta_Polarity_Score'] = dataframe['Answer'].apply(lambda x: self.roberta_sentiment_analysis(x))

        # roberta labels
        dataframe['Roberta_Score'] = dataframe['Roberta_Polarity_Score'].apply(lambda x: x.max())
        dataframe['Roberta_label'] = dataframe['Roberta_Polarity_Score'].apply(lambda x: x.argmax())
        dataframe['Roberta_label'] = dataframe['Roberta_label'].map({0: 'Negative', 1: 'Neutral', 2: 'Positive'})

        return dataframe

    def predict_sentiment(self, text):

        # create dataframe for the text
        tweet_dataframe = pd.DataFrame(data=[text], columns=['content'])

        # data cleaning
        processed_dataframe = self.data_processing(tweet_dataframe)

        # extract the clean text
        clean_text = processed_dataframe['Clean_text'].iloc[0]

        # extract the entities
        entity_df = self.extract_entities(clean_text)

        # extract dependent phrase for the entities
        entity_df = self.extract_entity_dependent_phrase(entity_df)

        # predict sentiment on the text
        sentiment_df = self.extract_roberta_sentiment(entity_df)

        string_result = []
        for idx, row in sentiment_df.iterrows():
            string_result.append(f"{row['Entity']}   {row['Roberta_label']}")

        string_result = "\n".join(string_result)

        return string_result
