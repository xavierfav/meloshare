from flask_socketio import SocketIO
from flask_jsglue import JSGlue
from flask_caching import Cache
import eventlet
eventlet.monkey_patch(socket=True)

socketio = SocketIO()
jsglue = JSGlue()
cache = Cache()
cache_kwargs = {
    'config': {
        'CACHE_TYPE': 'redis',
        'CACHE_REDIS_URL': 'redis://localhost'
    }
}
socketio_kwargs = {
    'message_queue': 'redis://localhost',
    'async_mode': 'eventlet'
}

EXTENSIONS = [
    (cache, cache_kwargs),
    (socketio, socketio_kwargs),
    jsglue
]
