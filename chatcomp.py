import openai

openai.api_type  = "azure"
openai.api_version  = "2023-08-01-preview"
openai.api_key  = "dvdffbfgbfb"
openai.api_base = "https://3ktbkv6m9d.execute-api.ap-south-1.amazonaws.com/dev/request/v1"

# Create the completion request
output = openai.ChatCompletion.create(
    headers={
        "Helicone-Auth": "Bearer sk-helicone-kjll5bq-ywceloy-ujfo7ea-5jh7wwq",
        "Helicone-User-Id": "Abhishek Srivastava"
    },
    engine="GPT4-8K",
    messages=[{"role" :"user", "content": "Hii"}],
    model="gpt-4",
    temperature=0.5   
)
print(output.choices[0].message)
