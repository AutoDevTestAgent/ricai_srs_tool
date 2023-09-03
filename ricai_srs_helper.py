import json
import weaviate
import os
import openai

class RicaiSRSHelper:
    def __init__(self, weaviate_url, weaviate_key, openai_key):
        """
        Initializes the RicaiSRSHelper with the provided Weaviate and Github credentials.
        Args:
            Weaviate_url (str): weaviate database connection url.
            Weaviate_api_key (str): weaviate database connection API key.
            Openai_api_key (str): OpenAI API key.
        """
        self.w_client = weaviate.Client(
            url=weaviate_url,
            auth_client_secret=weaviate.AuthApiKey(
                api_key=weaviate_key
            ),
            additional_headers={
                "X-OpenAI-Api-Key": openai_key
            },
        )

        self.openai_key = openai_key

    def retrieve_all_requirements(self):
        pass

    def retrieve_specific_feature_requirements(self, feature):
        pass

    def match_code_with_requirements(self, code):
        pass