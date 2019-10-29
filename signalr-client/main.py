from requests import Session
from signalr import Connection

with Session() as session:
    Connection("http://174.116.248.94/hhii", session)
