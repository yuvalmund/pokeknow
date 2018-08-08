import facebook
import http.client, urllib.request, urllib.parse, urllib.error, base64, sys, json
from PIL import Image

photo_url = list()
def getPhotos(access_token):
        count = 0
        graph = facebook.GraphAPI(access_token="EAAJZAtEg62TMBAAoHf9d4av22I84kPTsQxjLG86EuWOcMKhfLxoP4yhqUe6swY9dqu3tiqI3jPrGh9MbkBmOIbgBUr0Nu44tPiRzlDSKTLZBZAUOv2vWKvU3vnUydWIPep8TifF7dLXZCpiPySFck4ZAHMp2jrZCYSqvLt0mvPnbUCfeNnfPlCrvwup6r901EZD", version="2.12")
        albums = graph.get_connections(id='me', connection_name='albums')
        for album in albums['data']:
            curr = graph.get_connections(id=album['id'], connection_name='photos')
            for photo in curr['data']:
                if count <= 50:
                    count = count + 1
                    curr_photo = graph.get_connections(id=photo['id'], connection_name='picture')
                    photo_url.append(curr_photo['url'])

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'add9d59bec4a434d96aa72156f76d56a',
}

params = urllib.parse.urlencode({
    # Request parameters
    'maxCandidates': '1',
})

alltags = {}

transtags = {'outdoorsy': ['outdoor','boat','water','lake','river','dock','riding','city','march','street', 'tree', 'grass', 'bush'],'social': ['social','person','man','posing','camera','photo','city','band','parade','talk','family','crowd'],'happy': ['happy','smiling','young','summer','cheerleader','play','light','dancing','singing','laughing'],'dark': ['dark','demons','black','dead','scar','fear','pain','ghost','cloudy','shadow'],'intelligent':['intelligent','person','man','glasses','woman','plans','hero','thoughts','book','brain','robot','library'],'foodie': ['food','young','ice-cream','pizza','eat','melon','soda','meat','milk','vegetables','apple','hamburger'], 'angry': ['angry','broken','scar','break','annoy','violence','displeasure','hate','hate','bully','punch','kick'], 'gabay':['outdoor','man','posing','photo','city','summer']}

def tag_pic(url):
    try:
        conn = http.client.HTTPSConnection('westeurope.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/tag?%s" % params, body, headers)
        response = conn.getresponse()
        data = json.loads(response.read().decode("utf-8"))

        for tag in data["tags"]:
            if tag["confidence"] >= float(sys.argv[1]):
                try:
                    if tag["name"] not in alltags:
                        alltags[tag["name"]] = 1
                    else:
                        alltags[tag["name"]] = alltags[tag["name"]] + 1
                except KeyError as e:
                    print(data)

        conn.close()

    except Exception as e:
        print(e)
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

getPhotos("stuff")

for url in photo_url:
    body = "{'url':'" + url + "'}"
    tag_pic(body)

finaltags = {}
sumno = 0
catindex = {'outdoorsy' : 0,'social' : 1,'happy' : 2,'dark' : 3,'intelligent' : 4,'foodie' : 5,'angry' : 6 , 'gabay' : 7 }
retarr = [[0,0,0,0,0,0,0,0,"name"]]

for tag in alltags:
    #print(tag + " : " + str(alltags[tag]))
    for cat in transtags:
        if tag in transtags[cat]:
            if cat not in finaltags:
                finaltags[cat] = alltags[tag]
            else:
                finaltags[cat] = finaltags[cat] + alltags[tag]
            sumno = sumno + alltags[tag]

for tag in finaltags:
    retarr[0][catindex[tag]] = int((finaltags[tag]/sumno)*10)+1
    print(tag + " : " + str(retarr[0][catindex[tag]]))

print(retarr)

Image.open("./Charmander.png").show()

