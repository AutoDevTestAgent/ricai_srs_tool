from typing import Type
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
from ricai_srs_helper import RicaiSRSHelper

class RicaiSRSReadAllSchema(BaseModel):
    # TODO: determine params to pass
    # repository: str = Field(..., description="The Github repository to use for testing")
    pass

class RicaiSRSReadAllTool(BaseTool):
    """
    RicAI Read all requirements from document tool

    Attributes:
        name : The name.
        description : The description.
        args_schema : The args schema.
    """
    name = "RicaiSRSReadAll"
    description = (
        "A tool for reading all requirements from document."
    )
    args_schema: Type[BaseModel] = RicaiSRSReadAllSchema

    class Config:
        arbitrary_types_allowed = True
    
    def _execute(self, repository: str):
        """
        Execute the RicAI Read all requirements from document tool.

        Args:
            repository: The Github repository to use for testing

        Returns:
            All requirements if successful. or error message.
        """
        try:
            weaviate_url = self.get_tool_config("WEAVIATE_URL")
            weaviate_key = self.get_tool_config("WEAVIATE_API_KEY")
            openai_key = self.get_tool_config("OPENAI_API_KEY")
            
            ricai_srs_helper = RicaiSRSHelper(
                weaviate_url=weaviate_url,
                weaviate_key=weaviate_key,
                openai_key=openai_key
            )                        
            result = ricai_srs_helper.retrieve_all_requirements()
            return result
        except Exception as err:
            return f"Error: Unable to retrieve SRS document - {err}"