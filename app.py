#!/usr/bin/env python3

from aws_cdk import core

from python_static_site.python_static_site_stack import MyStack


app = core.App()
MyStack(
    app,
    "static-site-cdk-2",
    env=core.Environment(region="us-east-1", account="821330209644"),
)

app.synth()
