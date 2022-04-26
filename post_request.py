token = "5241964759:AAHkHOSNmsA2Ge6hka2YwHC_JNY3PwyRFbI" # add your token here
url = "<base-api-url>/api/posts"
try:
    payload = d
    payload = json.dumps(payload)
    headers = {
        'token': token,
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        }
    r = requests.post(url, data=payload, headers=headers)
    if r.ok:
        print ('success')
    else:
        print ('something went wrong')
              
except:
    logging.exception('error in POST request')
    raise
                 
{
    "type" : "image", # can be image, text, video
    "data" : "",
    "filename": "4bf4b1cc-516b-469d-aa38-be6762d417a5", #filename you put on s3
    "userId" : 169 # for telegram_bot this should be 169
}
