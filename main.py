"""Initialize pulling Jira issues."""
from flask import Flask, make_response, request
from flask_cors import CORS
from db import Database


def main(request):
    """Entry point."""
    headers = {
            'Access-Control-Allow-Origin': '*'
    }
    db = Database()
    authorName = request.args.get('author')
    records = db.create_json_response(authorName)
    return (records, 200, headers)
