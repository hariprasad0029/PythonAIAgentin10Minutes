"""
Comparison: Regular Python Object vs LangChain HumanMessage Print Output
"""

from langchain_core.messages import HumanMessage


class SimpleMessage:
    """Regular Python class without custom __str__/__repr__."""
    
    def __init__(self, content: str):
        self.content = content


# Regular Python object
regular_obj = SimpleMessage(content="Hello, this is a test message!")
print("Regular Python Object:")
print(regular_obj)

print("\n" + "-" * 50 + "\n")

# LangChain HumanMessage object
langchain_msg = HumanMessage(content="Hello, this is a test message!")
print("LangChain HumanMessage:")
print(langchain_msg)
