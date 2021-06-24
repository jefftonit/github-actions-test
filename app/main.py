import logging
logger = logging.getLogger(__name__)



async def app(scope, receive, send):
    logger.debug('log my app')
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
        'body': b'Hello, world version2!',
    })