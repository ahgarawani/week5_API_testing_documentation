import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# from flask_swagger_ui import get_swaggerui_blueprint
import random

from models import setup_db, Account


def create_app(test_config=None):
  # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/')
    def index():
      return jsonify({
        'success': True,
        'message': 'Hello World'
      })

    
    @app.route("/accounts/<int:account_id>")
    def get_accounts(account_id):
      try:
        account = Account.query.get(account_id)

        if account is None:
          abort(404)
        balance = account.format()["balance"]
        return jsonify({
          "success": True,
          "balance": balance
        })
      
      except:
        abort(404)

    # TODO Add routes using try/expect whenever applicable

    # TODO Add Error handlers
    @app.errorhandler(404)
    def not_found(error):
      return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found!"
      }), 404

    return app
