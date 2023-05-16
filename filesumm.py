import os
import requests
import json
import openai
from oai import processData

MyTextFile=open("RentersReform.txt", "r")   
MyString=MyTextFile.read()
MyTextFile.close()

azurekvuri = "https://venukv.vault.azure.net/"
azurekeyname = "oai-api-key"
apibase = "https://venuoai.openai.azure.com/"
deploymentName = "VenuDavinci003"

oaiPrompt = "Summarize this in five bullet points: " + MyString

# oaiPrompt = "Write a python code to store this information in a dataverse: " + name +"," + partner + "," + customer + "," + solution_area + "," + description + "," + geo

# Send a completion call to generate an answer
responsetext=processData(oaiPrompt, azurekeyname, azurekvuri, apibase, "azure", "2022-12-01", deploymentName)
print(responsetext)