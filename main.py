from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import datetime
import random

load_dotenv()

@tool
def calculator(a: float, b: float) -> str:
    """Perform basic arithmetic (addition) between two numbers."""
    return f"The result of adding {a} and {b} is {a + b}"

@tool
def unit_converter(meters: float) -> str:
    """Convert meters to feet."""
    feet = meters * 3.28084
    return f"{meters} meters is equal to {feet:.2f} feet"

@tool
def get_current_time() -> str:
    """Return the current date and time."""
    now = datetime.datetime.now()
    return now.strftime("Current date and time: %Y-%m-%d %H:%M:%S")

@tool
def summarize_text(text: str) -> str:
    """Return a very short summary of a given text (simulated)."""
    if len(text.split()) < 10:
        return "Text is too short to summarize."
    return f"Summary: {text[:50]}..."  # Simulated

@tool
def get_joke() -> str:
    """Tell a random programming-related joke."""
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "There are only 10 types of people in the world: those who understand binary and those who don't.",
        "Why do Java developers wear glasses? Because they don't C#!",
    ]
    return random.choice(jokes)

@tool
def greet(name: str) -> str:
    """Greets the user by name."""
    return f"Hello {name}! I'm happy to assist you today "

def main():
    model = ChatOpenAI(temperature=0)
    tools = [calculator, unit_converter, get_current_time, summarize_text, get_joke, greet]

    agent_executor = create_react_agent(model, tools)

    print("Welcome! I'm an AI assistant. How can I help you today? Type 'quit' to exit.")
    print("You can ask me to perform calculations, conversions, summaries, jokes, or more!")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "quit":
            break

        print("\nAssistant: ", end="")
        try:
            for chunk in agent_executor.stream({"messages": [HumanMessage(content=user_input)]}):
                if "agent" in chunk and "messages" in chunk["agent"]:
                    for message in chunk["agent"]["messages"]:
                        print(message.content, end="")
        except Exception as e:
            print(f"\n[Error]: {e}")
        print()

if __name__ == "__main__":
    main()
