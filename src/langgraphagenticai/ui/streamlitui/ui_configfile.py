from configparser import ConfigParser
import os

class Config:
   #def __init__(self,config_file="/src/langgraphagenticai/ui/uiconfigfile.ini"):
    def __init__(self, config_file=None):
        if config_file is None:
            config_file = os.path.join(os.path.dirname(__file__), 'uiconfigfile.ini')

        self.config=ConfigParser()
        self.config.read(config_file)

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
        
    def get_gemini_model_options(self):
        return self.config["DEFAULT"].get("GEMINI_MODEL_OPTIONS").split(", ")
    
    