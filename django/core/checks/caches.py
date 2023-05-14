from django.conf import settings
from django.core.cache import DEFAULT_CACHE_ALIAS

from . import Error, Tags, register

E001 = Error(
    f"You must define a '{DEFAULT_CACHE_ALIAS}' cache in your CACHES setting.",
    id='caches.E001',
)


@register(Tags.caches)
def check_default_cache_is_configured(app_configs, **kwargs):
    return [E001] if DEFAULT_CACHE_ALIAS not in settings.CACHES else []
