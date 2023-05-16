import os
import requests
import json
import openai
from oai import processData

# name = input("Enter your name: ")
# partner = input("Enter your partner's name: ")
# customer = input("Enter the customer's name: ")
# solution_area = input("Enter the solution area: ")
# description = input("Enter the description of the ask: ")
# geo = input("Enter the Geo: ") 
name="Venu"
partner="Fabrikam"
customer="Contoso"
solution_area="Data and AI"
description="Contoso is embarking on a cloud transformation exercise with Fabrikam helping them onboard 3 mission critical applications onto Azure. Need help with reviewing the solution architecture and suggest best practices."
geo="APAC"

#Azure Key Vault Details
azurekvuri = "Your Azure Key Vault URI here"
azurekeyname = "Name of the API Key in Key Vault"

#Azure OpenAI Instance Details
apibase = "Your OpenAI Instance base URL"
deploymentName = "Your Model Deployment Name"
# You can modify the prompt to suit your use case. 
oaiPrompt = 'Write an email response as if you are a PhD student responding officially to '+name+ \
    ' acknowledging the request for helping the partner organization named'+ partner + \
    ' working with the customer organization named '+customer+ 'in the area '+solution_area+ \
    'and include a summary of '+description+\
    'as concise bullet points. Ask for a call to discuss this further. Your output should be a properly formatted email in proper British English with line breaks after the greeting and before the sign off'

# oaiPrompt = "Write a python code to store this information in a dataverse: " + name +"," + partner + "," + customer + "," + solution_area + "," + description + "," + geo

# Send a completion call to generate an answer
responsetext=processData(oaiPrompt, azurekeyname, azurekvuri, apibase, "azure", "2022-12-01", deploymentName)
print(responsetext)
