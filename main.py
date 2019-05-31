"""Initialize pulling Jira issues."""
from flask import Flask, make_response, request
from flask_cors import CORS
from db import Database


def main(request):
    """Entry point."""
    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }
    db = Database()
    authorName = request.args.get('author')
    records = db.create_json_response(authorName)
    return make_response(records, 200, headers)
