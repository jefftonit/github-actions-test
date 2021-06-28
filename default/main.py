import logging
import os
logger = logging.getLogger(__name__)



async def app(scope, receive, send):
    logger.debug('hitting default app engine')
    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hitting app engine default app, try visiting one of the named services in App Engine. GAE requires you have a default service setup, this is essentially a shell app, you could optionally use this as a dispatcher for the other apps as well: https://cloud.google.com/appengine/docs/standard/nodejs/how-requests-are-routed#dispatch',
    })