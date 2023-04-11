import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    
    base_url = "https://api.openpath.com/orgs/"
    orgid = "2583"
    url = base_url + '{}/users'.format(orgid)
    userprincipalname = req.params.get('upn')
    status = req.params.get('status')
    ##Use Payload status of "S" to suspend the user and payload status of "A" to mark a user as active.
    payload = {"status": status}
    querystring = {"offset":"0","sort":"identity.lastName","order":"asc"}
    headers = {
        "Accept": "application/json",
        "Authorization": "Basic Y29ubm9yYithcGlAZGl2ZXJnZWl0LmNvbTpWc1VpYzh0TGgxZ0ZEY1hwTmRWb1kwS1NFbGVKOGQ=",
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    users = data['data']
    for user in users:
        useridentity = user['identity']
        userid = user['id']
        useremail = useridentity['email']
        if (useremail == userprincipalname.lower()):
            #print(useremail)
            print(useremail)
            print(userid)
            statusurl = "https://api.openpath.com/orgs/{}/users/{}/status".format(orgid,userid)
            userstatus = requests.request("PUT", statusurl, json=payload, headers=headers)
            return func.HttpResponse(status_code=200)
    return func.HttpResponse(status_code=400)