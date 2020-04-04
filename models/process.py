#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import db
from models.nodeData import NodeData

# 类名定义 collection
class Process(db.Document):
    # 字段
    # 流程id
    processId = db.StringField(required=True)
    # 流程数据
    processdata = db.ReferenceField(NodeData)
    #流程描述
    processattr= db.ReferenceField(NodeData)

    def __str__(self):
        return "processId:{} - processdata:{}".format(self.processId, self.processdata)

