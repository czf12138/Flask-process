#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,jsonify,abort, request,json
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)


#配置mongodb数据库信息
app.config['MONGODB_SETTINGS'] = {
    'db':   'demo',
    'host': '47.112.237.128',
    'port': 27027
}
#获取mongodb数据库操作对象
#app.config.from_pyfile('config.json')
db = MongoEngine(app)
from models.process import Process

CORS(app, supports_credentials=True) # 用于处理跨域问题
@app.route('/process', methods=['POST'])
def add_process():
  if not request.json or not 'attr' in request.json or not 'nodeList' in request.json or not 'linkList' in request.json:
    print(request)
    abort(400)
  process = Process(processId=request.json['process_id'],processdata=request.json,).save();
  output = {"code":20000,'process_id' : process.processId, 'message' : "添加工艺路线数据成功"}
  return jsonify({'result' : output})

 #根据id获取工艺流程
@app.route('/process/<string:process_id>', methods=['GET'])
def getprocess(process_id):
     process = Process.objects.get(**{"processId": process_id});
     # process = Process.objects(processId=process_id).first();

     if not process:
       output_error = {'process': None, 'message': "未查询到该流程"}
       return jsonify({'result': output_error})
     output = {"code":20000,'process': process, 'message': "成功获取该Id工艺流程"}
     return jsonify({'result': output})

 #根据id删除工艺流程
@app.route('/process/<string:process_id>', methods=['DELETE'])
def deleteprocess(process_id):
     if not process_id:
       output_error = {'process': None, 'message': "传入流程ID为空"}
       return jsonify({'result': output_error})

     process = Process.objects(processId=process_id).delete();
     if process>0:
       output = {'process': process, 'message': "成功删除该Id工艺流程"}
       return jsonify({'result': output})
     output = {"code":20000,'process': process, 'message': "删除该Id工艺流程失败"}
     return jsonify({'result': output})

 #根据id修改工艺流程
@app.route('/process/<string:process_id>', methods=['PUT'])
def updateprocess(process_id):
     if not process_id:
       output_error = {'process': None, 'message': "传入流程ID为空"}
       return jsonify({'result': output_error})

     process = Process.objects(processId=process_id).delete();

     process = Process(processId=process_id, processdata=request.json).save();

     # process.save();
     output = {"code":20000,'process': process, 'message': "修改流程信息成功"}
     return jsonify({'result': output})

@app.route('/process', methods=['GET'])
def getProcessList():
    mongo = PyMongo(app, uri="mongodb://localhost:27027/demo")
    # db.news.find({}, {id: 1, title: 1})
    processList=[]
    processes = mongo.db.process.find({},{'processdata.attr':1,'_id':0})
    for i in processes:
        processList.append(i['processdata']['attr'])
    data=[{"id":attr['id'],"name":attr['processName'],"desc":attr['processDesc'],"status":attr['processStatus']} for attr in processList ]
    output = {"code": 20000, 'process': data, 'message': "查询流程信息成功"}
    return  jsonify({'result': output})

@app.route('/hello/<string:name>', methods=['GET'])
def gettest(name):
        return jsonify({'result': "hello"+name})




