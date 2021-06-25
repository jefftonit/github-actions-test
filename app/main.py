import logging
import os
logger = logging.getLogger(__name__)



async def app(scope, receive, send):
    logger.debug('log my app')
    tester = os.getenv('TEST_VAR')
    body = 'Hello, world version dev! test var: %s' % tester
    bodyBytes = body.encode()
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
        'body': bodyBytes,
    })