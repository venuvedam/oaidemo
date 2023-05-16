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
partner="TCS"
customer="Civca Australia"
solution_area="Data and AI"
description="What we have in mind is some independent review from Microsoft of Altitude for both the technical deployment and cost optimisation (FinOps) to ensure we are in the best position to continue the migration of our Australian customers to Azure at pace. Context below: As briefly discussed last week on our call, Civica Australia is now starting to onboard a significant amount of Local Government customers onto our ‘Altitude ERP’ deployed in Azure. For context we now have three Beta customer live on Altitude and another 10 in the process to go live, and hope we might add double digits yearly for the coming years. A challenge for Altitude is around storage and logs which makes up a large % of our Azure spend. Altitude is our flagship product in Australia and a significant group-wide contributor to our existing and future ($30m+ MACC due to renew in June) and we would like reassurance that we are taking a best practice approach which helps us to control our cloud costs into the future."
geo="APAC"
azurekvuri = "https://venukv.vault.azure.net/"
azurekeyname = "oai-api-key"
apibase = "https://venuoai.openai.azure.com/"
deploymentName = "VenuDavinci003"

oaiPrompt = 'Write an email response as if you are a PhD student responding officially to '+name+ \
    ' acknowledging the request for helping the partner organization named'+ partner + \
    ' working with the customer organization named '+customer+ 'in the area '+solution_area+ \
    'and include a summary of '+description+\
    'as concise bullet points. Ask for a call to discuss this further. Your output should be a properly formatted email in proper British English with line breaks after the greeting and before the sign off'

# oaiPrompt = "Write a python code to store this information in a dataverse: " + name +"," + partner + "," + customer + "," + solution_area + "," + description + "," + geo

# Send a completion call to generate an answer
responsetext=processData(oaiPrompt, azurekeyname, azurekvuri, apibase, "azure", "2022-12-01", deploymentName)
print(responsetext)