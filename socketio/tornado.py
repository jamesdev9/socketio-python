import sys
if sys.version_info >= (3, 5):
    try:
        from engineio.async_drivers.tornado import get_tornado_handler as \
            get_engineio_handler
    except ImportError:
        from engineio.async_tornado import get_tornado_handler as \
            get_engineio_handler


def get_tornado_handler(socketio_server):
    return get_engineio_handler(socketio_server.eio)
