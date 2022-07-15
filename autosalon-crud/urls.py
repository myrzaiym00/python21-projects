from salon.views import *

url_patterns = [
    ("create-car/", create_car),
    ("listing-cars/", listing_cars),
    ("retrieve-car/id", retrieve_car),
    ("update-car/id", update_car),
    ("delete-car/id", delete_car),
    ('create-comment/', create_comment),
    ('like-car/', like_car),
]