from typing import Type
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
from ricai_srs_helper import RicaiSRSHelper

class RicaiSRSMatchCodeSchema(BaseModel):
    file_dir: str = Field(..., description="The SRS document directory")
    code: str = Field(..., description="The code to retrieve requirements for")
    pass

class RicaiSRSMatchCodeTool(BaseTool):
    """
    RicAI Read requirements for specific code tool

    Attributes:
        name : The name.
        description : The description.
        args_schema : The args schema.
    """
    name = "RicaiSRSMatchCode"
    description = (
        "A tool for reading requirements for specific code from document."
    )
    args_schema: Type[BaseModel] = RicaiSRSMatchCodeSchema

    class Config:
        arbitrary_types_allowed = True
    
    def _execute(self, file_dir: str, code: str):
        """
        Execute the RicAI Read requirements for specific code tool.

        Args:
            file_dir: The SRS document directory
            code: The code to retrieve requirements for

        Returns:
            Specific requirements if successful. or error message.
        """
        try:
            weaviate_url = self.get_tool_config("WEAVIATE_URL")
            weaviate_key = self.get_tool_config("WEAVIATE_API_KEY")
            openai_key = self.get_tool_config("OPENAI_API_KEY")
            
            ricai_srs_helper = RicaiSRSHelper(
                weaviate_url=weaviate_url,
                weaviate_key=weaviate_key,
                openai_key=openai_key,
                file_dir=file_dir
            )                        
            result = ricai_srs_helper.match_code_with_requirements(code)
            return result
        except Exception as err:
            return f"Error: Unable to retrieve SRS document - {err}"