"""Initialize pulling Jira issues."""
from flask import Flask, make_response, request
from flask_cors import CORS
from db import Database


def main(request):
    """Entry point."""
    db = Database()
    authorName = request.args.get('author')
    records = db.create_response(authorName)
    return records
