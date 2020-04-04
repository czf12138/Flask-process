from bson import json_util as jsonb
import json

#拿到的的数据转换为 bson 对象，然后通过json.loads()方法将其转换为json能处理的字符串，
# 然后在转换为json对象；由此，可以写一个通用处理方法，
def bson_to_json(documentList):
    return json.dumps(json.loads(jsonb.dumps(documentList)))