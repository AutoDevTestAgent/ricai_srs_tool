from abc import ABC
from typing import List

from superagi.tools.base_tool import BaseToolkit, BaseTool
from ricai_srs_read_all import RicaiSRSReadAllTool
from ricai_srs_read_feature import RicaiSRSReadFeatureTool
from ricai_srs_match_code import RicaiSRSMatchCodeTool

class RicaiSRSToolkit(BaseToolkit, ABC):
    name: str = "RicAI SRS Toolkit"
    description: str = "Toolkit containing tools for SRS extraction from a document."

    def get_tools(self) -> List[BaseTool]:
        return [
            RicaiSRSReadAllTool(),
            RicaiSRSReadFeatureTool(),
            RicaiSRSMatchCodeTool(),
            ]

    def get_env_keys(self) -> List[str]:
        return [
            "WEAVIATE_URL",
            "WEAVIATE_API_KEY",
            "OPENAI_API_KEY",
            ]