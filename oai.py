import os
import requests
import json
import openai
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


def processData(startPhrase, apikeyname, keyvaulturl, api_base, api_type, api_version, deployment_name):

    #create a credential object using default Azure Credentials
    credential = DefaultAzureCredential()
    #create a secret client using this credential and the key vault url
    secret_client = SecretClient(vault_url=keyvaulturl, credential=credential)

    openai.api_key = secret_client.get_secret(apikeyname).value

    openai.api_base =  api_base
    # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
    openai.api_type = api_type
    openai.api_version = api_version # this may change in the future

    deployment_name=deployment_name #This will correspond to the custom name you chose for your deployment when you deployed a model. 

    # Send a completion call to generate an answer
    # startPhrase = 'Write an email response as if you are a PhD student responding officially to '+requester_name+ \
    # ' acknowledging the request for helping the partner organization named'+ partner + \
    # ' working with the customer organization named '+customer+ 'in the area '+solution_area+ \
    # 'and include a summary of '+description+\
    # 'as concise bullet points. Ask for a call to discuss this further. Your output should be a properly formatted email in proper British English with line breaks after the greeting and before the sign off'
    
    response = openai.Completion.create(engine=deployment_name, prompt=startPhrase, max_tokens=1000)
    
    return response['choices'][0]['text']
