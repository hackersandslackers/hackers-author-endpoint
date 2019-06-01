"""Initialize pulling Jira issues."""
from flask import Flask, make_response, request, jsonify
from db import Database


def main(request):
    """Entry point."""
    db = Database()
    authorName = request.args.get('author')
    records = db.create_json_response(authorName)
    response = jsonify(records)
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Methods', 'GET, POST')
    return response
