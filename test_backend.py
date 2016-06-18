import cherrypy


with open("bon.example.json") as jsonfile:
    data = jsonfile.read()


class HelloWorld(object):
    def index(self):
        cherrypy.response.headers['Access-Control-Allow-Origin'] = "*"
        return '{"id":"93r32-23r-32r-23rsd",'\
               '"url":"http://localhost:8080/93r32-23r-32r-23rsd"}'
        return data
    index.exposed = True


cherrypy.quickstart(HelloWorld())
