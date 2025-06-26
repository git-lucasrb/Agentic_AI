import streamlit as st
import os

from src.langgraphagenticai.ui.streamlitui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user.controls={}