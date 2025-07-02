from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    Basic Chatbot login implementation
    """

    def __init__(self,model):
        self.llm=model

    def process(self,state:State)->dict:
        """
        Represent the structure of the state and generates a chatbot response.
        """
        return{"messages":self.llm.invoke(state['messages'])}