#!/bin/bash
# A bash Script making the the server to respond with a message containing.
curl -sL -X PUT 0.0.0.0:5000/catch_me -d "user_id=98"
