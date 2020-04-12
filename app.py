#!/usr/bin/env python3

from aws_cdk import core

from python_static_site.python_static_site_stack import PythonStaticSiteStack


app = core.App()
PythonStaticSiteStack(app, "python-static-site")

app.synth()
