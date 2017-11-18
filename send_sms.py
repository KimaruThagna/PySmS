from twilio.rest import Client
from credentials import *
import numpy as np
# put your own credentials here
account_sid = sid
auth_token = a_token
client = Client(account_sid, auth_token)
#at this point, anything available in python is at your disposal as long as you send
# string in the message body
#eg lets find the euclidian distance between points A and B
A=[4,2]
B=[3,-10]
dist=np.linalg.norm(np.array(A)-np.array(B))

client.messages.create(
  to=My_cell,
  from_=my_twilio,
  body="The euclidian distance between [4,2] and [3,-10] is"+dist,
  media_url="https://climacons.herokuapp.com/clear.png")

