from flask import Blueprint
from flask import request
from utils.model_inference import model


model_bp = Blueprint("modelController", __name__, url_prefix="/model")


@model_bp.route("/getAnswer")
def getAnswer():
    '''
    TODO
    此处被java 接口调用，返回模型推理结果
    :return model_answer(json/String):
    '''
    sent = request.args.get("sent", type=str)
    response=model.inference(sent)
    print(sent)
    return response
