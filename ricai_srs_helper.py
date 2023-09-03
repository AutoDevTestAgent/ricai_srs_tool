import json
import weaviate
import os
import openai

from dotenv import load_dotenv
from llama_index import SimpleDirectoryReader, VectorStoreIndex, ServiceContext, set_global_service_context
from llama_index.node_parser import SimpleNodeParser
from llama_index.llms import OpenAI

class RicaiSRSHelper:
    def __init__(self, weaviate_url, weaviate_key, openai_key, file_dir):
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

        load_dotenv()

        self.openai_key = openai_key

        # TODO: recheck provided config parameters
        llm = OpenAI(model="gpt-4", temperature=0, max_tokens=256)
        service_context = ServiceContext.from_defaults(llm=llm)
        set_global_service_context(service_context)
        
        document = SimpleDirectoryReader(file_dir).load_data()
        parser = SimpleNodeParser.from_defaults()
        nodes = parser.get_nodes_from_documents(documents=document)
        index = VectorStoreIndex(nodes)
        # TODO: consider changing to other retriever type
        self.query_engine = index.as_query_engine()

    def retrieve_all_requirements(self):
        response = self.query_engine.query("Retrieve all the contents of the document")
        
        print(response.source_nodes)
        print(response.get_formatted_sources())

        return response

    def retrieve_specific_feature_requirements(self, feature):
        response = self.query_engine.query(f"Retrieve all the requirements for the feature: {feature}")
        
        print(response.source_nodes)
        print(response.get_formatted_sources())

        return response

    def match_code_with_requirements(self, code):
        # TODO: determine in what format will the code be passed
        responses = []
        for c_part in code:
            r = self.query_engine.query(f"Retrieve all requirements for the code: {c_part}")
                    
            print(r.source_nodes)
            print(r.get_formatted_sources())

            responses.append(r)
        return responses