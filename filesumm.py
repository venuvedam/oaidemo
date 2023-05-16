import os
import requests
import json
import openai
from oai import processData

MyTextFile=open("RentersReform.txt", "r")   
MyString=MyTextFile.read()
MyTextFile.close()

#Azure Key Vault Details
azurekvuri = "Your Azure Key Vault URI here"
azurekeyname = "Name of the API Key in Key Vault"

#Azure OpenAI Instance Details
apibase = "Your OpenAI Instance base URL"
deploymentName = "Your Model Deployment Name"

oaiPrompt = "Summarize this in five bullet points: " + MyString

# oaiPrompt = "Write a python code to store this information in a dataverse: " + name +"," + partner + "," + customer + "," + solution_area + "," + description + "," + geo

# Send a completion call to generate an answer
responsetext=processData(oaiPrompt, azurekeyname, azurekvuri, apibase, "azure", "2022-12-01", deploymentName)
print(responsetext)
