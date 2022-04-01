from redis_om import get_redis_connection
from config import settings
inventory = get_redis_connection(
    host=settings.HOST,
    port=settings.PORT,
    password=settings.PASSWORD,
    decode_responses = True
)