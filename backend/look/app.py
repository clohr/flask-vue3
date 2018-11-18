import falcon
import os
from .images import ImageStore, Resource, Item

def create_app(image_store):
    image_resource = Resource(image_store)
    api = falcon.API()
    api.add_route('/images', image_resource)
    api.add_route('/images/{name}', Item(image_store))
    return api


def get_app():
    storage_path = os.environ.get('LOOK_STORAGE_PATH', './uploads')
    image_store = ImageStore(storage_path)
    return create_app(image_store)