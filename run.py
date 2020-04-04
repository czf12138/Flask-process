from app import app
from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop


s = HTTPServer(WSGIContainer(app))
s.listen(8011) # 监听 9900 端口
IOLoop.current().start()
# if __name__ == '__main__':
#     app.run(host = '127.0.0.1', port = 8011, debug = True)

