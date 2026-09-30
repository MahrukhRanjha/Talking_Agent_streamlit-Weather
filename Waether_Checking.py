```python
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
import requests
import streamlit as st


# -----------------------------
# Gemini LLM
# -----------------------------
llm = ChatGoogleGenerativeAI(
    api_key=st.secrets["GEMINI_API_KEY"],
    model="gemini-3.6-flash",
    temperature=2,
    max_tokens=None,
    timeout=None,
    max_retries=2
)


# -----------------------------
# Weather Tool
# -----------------------------
def get_weather(city: str) -> dict:
    """Get weather for a given city."""

    response = requests.get(
        f"https://p2pclouds.up.railway.app/v1/learn/weather?city={city}"
    )

    response.raise_for_status()

    return response.json()


# -----------------------------
# Create Agent
# -----------------------------
agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt=(
        "You are a helpful assistant. "
        "Use the get_weather tool when the user asks about weather."
    )
)


# -----------------------------
# Run Agent
# -----------------------------
response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Tell me the weather of Lahore?"
            }
        ]
    }
)


# -----------------------------
# Display Result
# -----------------------------
st.write(response["messages"][-1].content)
```
