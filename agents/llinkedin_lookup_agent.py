from langchain import hub
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.agents import create_react_agent, AgentExecutor


from tools.tools import get_profile_url


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    template = """givin the full name {name_of_person} I want you to get me a link to their linkedin profile page.
                        Your answer should contain only a URL"""

    react_prompt = hub.pull("hwchase17/react")

    tool_for_agent = [
        Tool(
            name="Crawl google 4 linkedin profile page",
            func=get_profile_url,
            description="useful for when you need to get the Linkedin profile URL of a person",
        )
    ]

    agent = create_react_agent(
        llm=llm,
        tools=tool_for_agent,
        prompt=react_prompt,
    )

    agent_executor = AgentExecutor(agent=agent, tools=tool_for_agent, verbose=True)

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    linkedin_profile_url = agent_executor.invoke(
        {"input": prompt_template.format_prompt(name_of_person=name)}
    )

    return linkedin_profile_url
