from twilio.rest import Client

account_sid = 'ACb52c0997326e019d1138cd3cc63e08df'
auth_token = 'fa6a06305d338e99863e61272dce1da0'

client = Client(account_sid, auth_token)

sender='+5585997788739'
receiver='+5585986118491'

message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body='Boa noite',
                              to='whatsapp:+558597788739'
                          )

print(message.sid)

 curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
     echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
     sudo apt-get update && sudo apt-get install yarn
