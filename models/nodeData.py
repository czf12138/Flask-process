#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import db


# 类名定义 collection
class NodeData(db.Document):
    # 字段
    nodeList = db.ListField(db.StringField(max_length=30))
    linkList = db.ListField(db.StringField(max_length=30))
    attr = db.StringField()
    config = db.StringField()
    status = db.StringField()
    remarks = db.ListField(db.StringField(max_length=30))

    def __str__(self):
        return "nodeList:{} - linkList:{}".format(self.nodeList, self.linkList)
    
