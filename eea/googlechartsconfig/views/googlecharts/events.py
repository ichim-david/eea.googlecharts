""" Handle events
"""
from eea.daviz.views.events import facet_deleted

def googlechart_facet_deleted(obj, evt):
    """ Cleanup removed facet from view properties
    """
    return facet_deleted(obj, evt, 'googlechart.googlecharts')
