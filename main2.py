# from langchain import OpenAI
# from langchain_experimental.agents.agent_toolkits import create_csv_agent
# import os

# # Set the OpenAI API key properly
# os.environ['OPENAI_API_KEY'] = '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'

# # Define the file path
# filePath = "C:/Users/AMRIT RAJ/Desktop/kirti doc/DATA.csv"

# # Initialize the OpenAI instance
# llm = OpenAI(temperature=0, Openai_api_key=os.getenv('OPENAI_API_KEY'))

# # Create the CSV agent
# agent = create_csv_agent(llm, filePath, verbose=True)

# # # Run a query with the agent
# # response = agent.run("how many students passed")
# # print(response)

from langchain import OpenAI
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
import os

os.environ['OPENAI_API_KEY'] = 'dummy_key'
#export OPENAI_API_KEY="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"
filePath="C:\Users\AMRIT RAJ\Desktop\kirti doc\DATA.csv"
llm=OpenAI(temperature=0,Openai_api_key='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')
agent = create_csv_agent(llm, filePath, verbose=True)
agent.run("how many students passed")