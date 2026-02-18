from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from ytmusicapi import YTMusic, OAuthCredentials
import json
import os
from dotenv import load_dotenv

load_dotenv()
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
print(client_id)
print(client_secret)

ytmusic = YTMusic("oauth.json", oauth_credentials=OAuthCredentials(client_id={client_id}, client_secret={client_secret}))