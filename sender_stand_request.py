import configuration
import requests

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER_PATH,
                         json=body)  

def get_new_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_NEW_ORDER_PATH, params = {"t": track})
    
