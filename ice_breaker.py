import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from third_parties.linkedin import scrape_linkedin_profile
from agents.llinkedin_lookup_agent import lookup as linkedin_lookup_agent

load_dotenv()


if __name__ == "__main__":
    summary_template = """
    givin the Linkedin information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    linked_profile_url = linkedin_lookup_agent(name="Eden Marco")

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_res = scrape_linkedin_profile()

    res = chain.run(information=linkedin_res)

    print(res)
