from twilio.rest import Client

accountSID = 'AC01b432208feee10090562338435b9097'
authToken = '331703b5d5c406de75753fb7801d0eeb'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+13237680642'
myCellPhone = '+8615776686301'


def text_myself(message):
    twilioCli.messages.create(body=message, from_=myTwilioNumber, to=myCellPhone)

