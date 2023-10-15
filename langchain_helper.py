from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType


from dotenv import load_dotenv
load_dotenv()

def langchain_pet_name_generator():
    llm = OpenAI(temperature = 0.7, model = 'gpt-3.5-turbo')

    name = llm("I have a dog pet and i want a cool name for him, please suggest.")

    return name

def langchain_prompt_chain_pet_name_generator(animal_type, pet_color):
    llm = OpenAI(temperature = 0.7)
    prompt_template_name =  PromptTemplate( 
        input_variables = ["animal_type", "pet_color"], 
        template = "I have a {animal_type} pet in {pet_color} color and i want a cool name for him, please suggest five cool names. It should be Indian name"
    )

    name_chain = LLMChain(llm=llm, prompt = prompt_template_name, output_key = "pet_name")

    response = name_chain({'animal_type' : animal_type, 'pet_color' : pet_color})
    return response

def langchain_agent():
    llm = OpenAI(temperature = 0.5)

    tools = load_tools(['wikipedia', 'llm-math'], llm = llm)
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = False
    )

    result = agent.run (
        "How many states in India and their capital and chif minister name?"
    )

    print(result)


if __name__ == "__main__":
    langchain_agent()


