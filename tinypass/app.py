#!/usr/bin/env python3
import os
import aws_cdk as cdk
from tinypass.tinypass_stack import TinypassStack
from dotenv import load_dotenv
load_dotenv()


app = cdk.App()
TinypassStack(app, os.getenv("APP_NAME"),)
app.synth()
