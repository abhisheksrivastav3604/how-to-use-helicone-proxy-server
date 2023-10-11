# How to use helicone proxy server using different method.

## Description

This repository demonstrates to how to use helicone proxy server with methods like cURL, Lang chain, and Chat completion helps us understand how well it works.

**Helicone proxy server link**: `https://3ktbkv6m9d.execute-api.ap-south-1.amazonaws.com/dev/request/v1`


## Prerequisite

  ### Required modules:-
  `pip install langchain`<br/>
  `pip install openai`<br/>
  
  ### Required Information:-
  1.  openai.api_type - we use azure openai key so we need set as "azure"
  2.  openai.api_version - This specifies the version of the Azure OpenAI API. To check, you can refer to this link: https://learn.microsoft.com/en-us/azure/ai-services/openai/reference
  3.  openai.api_base - i.e.  Helicone proxy server Link
  4.  Helicone Authentication key - It specified as "Bearer <Helicone-Auth-Key>"
  5.  Helicone User Id - User Name
  6.  engine - It specify the Azure OpenAI engine
  7.  model_name - It specifies the specific model within the chosen engine
  8.  temperature - It controls the randomness of the generated text.



## How to run :-

Step-by-step user guide [video](https://drive.google.com/file/d/1_Lj1xmXMB-60cgm5uK_ven639Ts3Q0Lf/view?usp=sharing)

1. Run the below command to clone this repo:
```
git clone https://github.com/madgical-ai/how-to-use-helicone-proxy-server.git
```
2. For cURL test :
   ```
   --request POST \
   --url `https://3ktbkv6m9d.execute-api.ap-south-1.amazonaws.com/dev/request/<engine name>/v1/chat`
   --header `Helicone-Auth: <Helicone-Auth-key>' \
   --header `Helicone-User-Id: <User-name>` \
   --data `{
	"model": "gpt-4",
	"temperature": 0.5,
	"messages": [
		{
			"role": "user",
			"content": "Hii"
		}
	  ]
        }'
   ```
3. For Langchain prompt test :
   ```
   you have to run this command in your terminal `langchain_prompt.py`
   ```
4. For Langchain agent test :
   ```
   you have to run this command in your terminal `langchain_agent.py`
   ```
5. For ChatCompletion test :
   ```
   you have to run this command in your terminal `chatcomp.py`
   ```
   


