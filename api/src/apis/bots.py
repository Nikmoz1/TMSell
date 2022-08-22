from flask_restx import Namespace, fields, Resource, abort
from flask_restx.reqparse import RequestParser
from http import HTTPStatus
from src.services import BotsService

bots_ns = Namespace('bots',
                    description='The service provides the functionality needed '
                                'to manage bots')

bot_model = bots_ns.model("Bots", {
    "comment": fields.String(required=True),
    "login": fields.String(required=True),
    "password": fields.String(required=True),
    "steam_id": fields.String(required=True),
    "shared_secret": fields.String(required=True),
    "identity_secret": fields.String(required=True),
    "steam_api": fields.String(required=True),
    "tm_api": fields.String(required=True),
    "google_drive": fields.String(required=True),
    "proxy": fields.String(required=True),
    "is_active": fields.Boolean()},

                          )
bots_get_model = bots_ns.inherit("Bot", bot_model, {
    "bot": fields.Nested(bot_model, skip_none=True)
})

bot_del_model = bots_ns.model("BotDel", bot_model, {
    "login": fields.String(required=True)
})


@bots_ns.route("/")
@bots_ns.doc(description="Endpoint to manage bots")
class BotsManage(Resource):
    req_parser = RequestParser()
    # req_parser.add_argument('bots', location=["login", "type"])
    req_parser.add_argument('comment', type=str, location="json", required=True)
    req_parser.add_argument('login', type=str, location="json", required=True)
    req_parser.add_argument('password', type=str, location="json", required=True)
    req_parser.add_argument('steam_id', type=str, location="json", required=True)
    req_parser.add_argument('shared_secret', type=str, location="json", required=True)
    req_parser.add_argument('identity_secret', type=str, location="json", required=True)
    req_parser.add_argument('steam_api', type=str, location="json", required=True)
    req_parser.add_argument('tm_api', type=str, location="json", required=True)
    req_parser.add_argument('google_drive', type=str, location="json", required=True)
    req_parser.add_argument('proxy', type=str, location="json", required=True)
    resp_model = bots_ns.model("CreateBotResponseModel", {
        "message": fields.String(),
        "status_code": fields.Integer(),
        "bot_data": fields.Nested(bot_model)
    })

    @bots_ns.expect(req_parser, validate=True)
    @bots_ns.marshal_with(resp_model, skip_none=True)
    @bots_ns.response(int(HTTPStatus.CREATED), "New bot was successfully add.", resp_model)
    @bots_ns.response(int(HTTPStatus.CONFLICT), "The bot already exists")
    @bots_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @bots_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    def post(self):
        bot_data = self.req_parser.parse_args()
        res, msg, code = BotsService.save_bot(**bot_data)
        print()
        return {
                   "message": msg,
                   "status_code": HTTPStatus.CREATED,
                   "bot_data": res
               }, code

    @bots_ns.marshal_with(bots_get_model, code=200, envelope="bots", skip_none=True)
    @bots_ns.response(int(HTTPStatus.OK), "Success.")
    @bots_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    def get(self):
        return BotsService.get_bots()

    @bots_ns.expect(req_parser, validate=True)
    @bots_ns.marshal_with(resp_model, skip_none=True)
    @bots_ns.response(int(HTTPStatus.ACCEPTED), "Bot updated", resp_model)
    @bots_ns.response(int(HTTPStatus.CONFLICT), "The bot already exists")
    @bots_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @bots_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    def put(self):
        bot_data = self.req_parser.parse_args()
        res, msg, code = BotsService.del_bot(**bot_data)
        return {
                   "message": msg,
                   "status_code": HTTPStatus.CREATED,
                   "bot_data": res
               }, code

    del_parser = RequestParser()
    del_parser.add_argument('login', type=str, location="json", required=True)

    @bots_ns.expect(del_parser, validate=True)
    @bots_ns.marshal_with(resp_model, skip_none=True)
    @bots_ns.response(int(HTTPStatus.OK), "Success. Bot delete")
    @bots_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    def delete(self):
        bot_data = self.del_parser.parse_args()
        res, msg, code = BotsService.del_bot(**bot_data)
        return {
                   "message": msg,
                   "status_code": HTTPStatus.CREATED,
                   "bot_data": res
               }, code


@bots_ns.route("/switch_active")
class BotStatusAPI(Resource):
    req_parser = RequestParser()
    req_parser.add_argument('login', type=str, location="json", default=True, required=False)
    req_parser.add_argument('is_active', type=bool, location="json", default=None, required=False)

    resp_model = bots_ns.model("ChangeStatusBotResponseModel", {
        "message": fields.String(),
        "status_code": fields.Integer(),
        "bot_data": fields.Nested(bot_model)
    })

    @bots_ns.expect(req_parser, validate=True)
    @bots_ns.marshal_with(resp_model, skip_none=True)
    @bots_ns.response(int(HTTPStatus.ACCEPTED), "Bot updated", resp_model)
    @bots_ns.response(int(HTTPStatus.CONFLICT), "The bot already exists")
    @bots_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @bots_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    def put(self):
        bot_data = self.req_parser.parse_args()
        res, msg, code = BotsService.put_status_bot(**bot_data)
        return {
                   "message": msg,
                   "status_code": HTTPStatus.CREATED,
                   "bot_data": res
               }, code


    # res, msg, code = JobService.save_job(**job_data)
    # return {
    #            "message": msg,
    #            "status_code": HTTPStatus.CREATED,
    #            "job_data": res
    # #        }, code
