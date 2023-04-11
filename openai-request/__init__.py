import logging
import requests
import openai
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    openai.api_type = "azure"
    openai.api_base = "https://uta-ops-openai.openai.azure.com/"
    openai.api_version = "2022-12-01"
    openai.api_key = "c9e35888d9c2461794cc499b81c58e1f"

    prompt = req.params.get('prompt')

    response = openai.Completion.create(
        engine="ops-ai-deployment",
        prompt=textprompt,
        temperature=.3,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        best_of=3,
        stop=None)

    
    return func.HttpResponse(response["choices"][0]["text"])
    return func.HttpResponse(status_code=400)
