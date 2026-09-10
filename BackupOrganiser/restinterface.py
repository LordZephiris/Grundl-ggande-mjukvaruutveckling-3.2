from flask import Flask, request, render_template
import json

app = Flask(__name__)

class RESTInterface:
    def __init__(self):
        self.setup_endpoints()

    def start(self,collection_manager, backup_manager):
        self.__cm = collection_manager
        self.__bm = backup_manager
        print("Listening on: http://localhost:5000/")
        app.run(debug=False, host="0.0.0.0", port=5000)

    def setup_endpoints(self):
        # "Normal" web pages
        @app.get('/')
        def startpage():
            return render_template('index.html')
        

        # API endpoins follow
        # These differ from the "normal" pages by
        # (where applicable) expecting JSON objects
        # and returning very terse status replies.

        @app.get('/api/Overview')
        def overview():
            return self.__cm.overview_json()

        @app.get('/api/List')
        def detailed_overview():
            return self.__cm.detailed_overview_json()

        @app.get('/api/Info')
        def info():
            name = request.args['name']
            result = self.__cm.info_json(name) 
            return (result,200) if result else (f"Cannot find any data collection with the name {name}", 404)

        @app.get('/api/Search')
        def search():
            name = request.args['name']
            return self.__cm.search_json(name)


        @app.post('/api/Collection')
        def add_collection():
            indata = request.get_json()
            result = self.__cm.add_collection(indata['name'],
                                              indata['description'],
                                              indata['creation_date'],
                                              indata['modification_date'],
                                              indata['still_updated'])
            return "ok", 201

        @app.post('/api/Backup')
        def add_backup():
            indata = request.get_json()
            collection = self.__cm.get(indata['name'])
            if collection:
                self.__bm.add_backup(collection, 
                                     indata['backupname'],
                                     indata['date'],
                                     indata['location'])
                return "ok", 201
            else:
                return f"Cannot find any data collection with the name {indata['name']}", 404

        @app.post('/api/Edit')
        def edit():
            indata = request.get_json()
            result = self.__cm.edit(indata['name'], indata['modification_date'], indata['still_updated'])
            if result:
                return "ok", 200
            else:
                return f"Cannot find any data collection with the name {indata['name']}", 404

        @app.post('/api/Unbackup')
        def unbackup():
            indata = request.get_json()
            collection = self.__cm.get(indata['name'])
            if collection:
                self.__bm.unbackup(collection, indata['backupname'], indata['date'])
                return "ok"
            else:
                return f"Cannot find any data collection with the name {indata['name']}", 404
            

        @app.delete('/api/Delete')
        def delete():
            collection_name = request.args['name']
            result = self.__cm.delete(collection_name)
            return ("ok",200) if result else (f"Cannot find any data collection with the name {collection_name}", 404)