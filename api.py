#!/usr/bin/env python
# coding: utf-8

# In[5]:


from flask import Blueprint
from flask_restful import Api
#from resources.Hello import Hello
import data_barchart
from flask_restful import Resource
from flask import Flask
from flask import request


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    
class Hello_(Resource):
    def get(self):
        return data_barchart.Hello()
    
class allData_Call_And_Put_Company_(Resource):
    def get(self):
        data = request.get_json()
        return str(data_barchart.allData_Call_And_Put_Company(data))
    
class strike_Price_Call_And_Put_Company_(Resource):
    def get(self):
        data = request.get_json()
        return str(data_barchart.strike_Price_Call_And_Put_Company(data))
    
class IV_Call_And_Put_Company_(Resource):
    def get(self):
        data = request.get_json()
        return str(data_barchart.IV_Call_And_Put_Company(data))
    
class strikePrice_350_Call_And_Put_Company_(Resource):
    def get(self):
        data = request.get_json()
        return str(data_barchart.strikePrice_350_Call_And_Put_Company(data))

# class Hello(Resource):
#     def get(self):
#         return {"message": "Hello, World!"}

# Route
api.add_resource(HelloWorld, '/test')
api.add_resource(Hello_, '/Hello')
api.add_resource(allData_Call_And_Put_Company_, '/allData_Call_And_Put_Company')
api.add_resource(strike_Price_Call_And_Put_Company_, '/strike_Price_Call_And_Put_Company')
api.add_resource(IV_Call_And_Put_Company_, '/IV_Call_And_Put_Company')
api.add_resource(strikePrice_350_Call_And_Put_Company_, '/strikePrice_350_Call_And_Put_Company')

#if __name__ == '__main__':
app.run(debug=True)


# In[ ]:




