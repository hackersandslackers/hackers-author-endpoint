"""Initialize pulling Jira issues."""
from flask import Flask, make_response, request
from flask_cors import CORS
from db import Database


def main(request):
    """Entry point."""
    db = Database()
    records = db.create_response()
    return records
