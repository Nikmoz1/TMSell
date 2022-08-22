import json
from http import HTTPStatus
from src.models import Bots
from src import db
from flask_restx import abort
from flask import jsonify
class BotsService:

    @staticmethod
    def save_bot(**bot_data):
        # print(bot_data)
        login_checked = Bots.query.filter_by(login=bot_data.get("login")).first()
        if login_checked is None:
            bot = Bots(comment=bot_data.get("comment"),
                       login=bot_data.get("login"),
                       password=bot_data.get("password"),
                       steam_id=bot_data.get("steam_id"),
                       shared_secret=bot_data.get("shared_secret"),
                       identity_secret=bot_data.get("identity_secret"),
                       steam_api=bot_data.get("steam_api"),
                       tm_api=bot_data.get("tm_api"),
                       google_drive=bot_data.get("google_drive"),
                       proxy=bot_data.get("proxy"),
                       )
            db.session.add(bot)
            db.session.flush()
            db.session.commit()
            return (bot,
                    "Successfully created.",
                    HTTPStatus.CREATED
                    )
        else:
            abort(HTTPStatus.CONFLICT, f'the bot already exists', status='fail', bot_data=bot_data)

    @staticmethod
    def get_bots():
        response = []
        bots = Bots.query.all()
        for bot in bots:
            print(type(bot))
            response.append(bot)
        print(response)
        return response

    @staticmethod
    def del_bot(**bot_data):
        login_checked = Bots.query.filter_by(login=bot_data.get("login")).first()
        print(login_checked)
        if login_checked:
            db.session.delete(login_checked)
            db.session.commit()
            return (login_checked,
                    "Successfully delete.",
                    HTTPStatus.ACCEPTED)
        else:
            abort(HTTPStatus.CONFLICT, f'There is no such bot', status='fail', bot_data=bot_data)

    @staticmethod
    def put_bot(**bot_data):
        login_checked = Bots.query.filter_by(login=bot_data.get("login")).first()

        if login_checked:
            for key, value in bot_data.items():
                if value != "string":
                    setattr(login_checked, key, value)
            db.session.commit()
            return (login_checked,
                    "Successfully delete.",
                    HTTPStatus.ACCEPTED)
        else:
            abort(HTTPStatus.CONFLICT, f'There is no such bot', status='fail', bot_data=bot_data)

    @staticmethod
    def put_status_bot(**bot_data):
        if bot_data.get("login") == "string":
            response = []
            bots = Bots.query.all()
            for row in bots:
                row.is_active = bot_data.get("is_active")
                db.session.commit()
                response.append(row)
            return (response,
                    "Successfully put status",
                    HTTPStatus.ACCEPTED)
        else:
            login_checked = Bots.query.filter_by(login=bot_data.get("login")).first()
            if login_checked:
                print("check login")
                login_checked.is_active = bot_data.get("is_active")
                db.session.commit()
                return (login_checked,
                        "Successfully put status bot.",
                        HTTPStatus.ACCEPTED)
            else:
                abort(HTTPStatus.CONFLICT, f'There is no such bot', status='fail', bot_data=bot_data)


        # return (
        #     "Successfully created.",
        #     HTTPStatus.CREATED
        # )
        # job_link = job_data.get('job_link')
        # job = Jobs.objects(job_link=job_link).first()
        # if not job:
        #     return (
        #         Jobs(**job_data).save(),
        #         "Successfully created.",
        #         HTTPStatus.CREATED
        #     )
        # else:
        #     abort(HTTPStatus.CONFLICT, f'the job already exists', status='fail', job_data=job_data)
