import connexion
from swagger_server.models.body_2 import Body2
from swagger_server.models.inline_response_200_3 import InlineResponse2003
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def delete_order(orderId):
    """
    Delete purchase order by ID
    For valid response try integer IDs with positive integer value.         Negative or non-integer values will generate API errors
    :param orderId: ID of the order that needs to be deleted
    :type orderId: int

    :rtype: None
    """
    return 'do some magic!'


def get_inventory():
    """
    Returns pet inventories by status
    Returns a map of status codes to quantities

    :rtype: Dict[str, int]
    """
    return 'do some magic!'


def get_order_by_id(orderId):
    """
    Find purchase order by ID
    For valid response try integer IDs with value &gt;&#x3D; 1 and &lt;&#x3D; 10.         Other values will generated exceptions
    :param orderId: ID of pet that needs to be fetched
    :type orderId: int

    :rtype: InlineResponse2003
    """
    return 'do some magic!'


def place_order(body):
    """
    Place an order for a pet
    
    :param body: order placed for purchasing the pet
    :type body: dict | bytes

    :rtype: InlineResponse2003
    """
    if connexion.request.is_json:
        body = Body2.from_dict(connexion.request.get_json())
    return 'do some magic!'
