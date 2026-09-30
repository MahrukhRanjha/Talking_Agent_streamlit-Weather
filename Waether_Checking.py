from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
import requests

llm = ChatGoogleGenerativeAI(
    api_key="AQ.Ab8RN6LGDjpUKCq4xxREvo-5Nllc7YjSMDkvpOA0OxHRK2kmwA",
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
    res = requests.get(
        f"https://p2pclouds.up.railway.app/v1/learn/weather?city={city}"
    )

    # Convert response to JSON
    data = res.json()

    return data


    agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful  Weather Assistant Use the get_weather tool whenever the user asks about weather."
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
