from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
import requests

llm = ChatGoogleGenerativeAI(
    api_key="AQ.Ab8RN6LveDNe-VTRWb8xxcNfkmjQXCIyY9QyJFCUgPixhXn-FA",
    model="gemini-3.6-flash",
    temperature=2,
    max_tokens=None,
    timeout=None,
    max_retries=2
)
import requests

def get_weather(city: str) -> dict:
    """Get weather for a given city."""

    # Send GET request to the Weather API
    response = requests.get(
        f"https://p2pclouds.up.railway.app/v1/learn/weather?city={city}"
    )

    # Check if the request was successful
    response.raise_for_status()

    # Convert response to JSON
    return response.json()




agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful assistant. "
    "Use the get_weather tool when the user asks about weather."
)
# Run the agent
response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Tell me wheater of lahore?"
            }
        ]
    }
)
print(response["messages"][-1].content)
