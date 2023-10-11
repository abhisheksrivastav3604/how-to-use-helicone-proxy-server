import openai
from langchain.llms import AzureOpenAI
import os

openai.api_type  = "azure"
os.environ["OPENAI_API_KEY"]="9fb2f004510099a"
openai.api_version="2023-08-01-preview"
openai.api_base = "https://3ktbkv6m9d.execute-api.ap-south-1.amazonaws.com/dev/request/v1"

# Create the completion request
llm = AzureOpenAI(
    headers={
        "Helicone-Auth": "<Helicone-Auth-Key>",
        "Helicone-User-Id": "<User-Name>"
    },
    engine="GPT4-8k",
    model_name="gpt-4",
    temperature= 0.5

)
print(llm("Hii"))
