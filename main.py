"""Initialize pulling Jira issues."""
from flask import Flask, request, jsonify, make_response
from db import Database


def main(request):
    """Entry point."""
    db = Database()
    authorName = request.args.get('author')
    if authorName:
        records = db.create_json_response(authorName)
        response = jsonify(records)
        response.headers.set('Access-Control-Allow-Origin', '*')
        response.headers.set('Access-Control-Allow-Methods', 'GET, POST')
        return response
    return make_response('Author name not provided.')
