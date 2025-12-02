import time
import hashlib
from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache


class CacheDebugMiddleware(MiddlewareMixin):
    """Middleware to log cache hits and misses"""
    
    def process_request(self, request):
        request._cache_start_time = time.time()
        return None
    
    def process_response(self, request, response):
        elapsed = time.time() - request._cache_start_time
        path = request.path
        
        # Simple heuristic: if response is very fast (<50ms), it's likely from cache
        # Cache hits are typically 0.001-0.010s, misses are 0.5s+
        if elapsed < 0.05:
            cache_status = "✓ CACHE HIT"
        else:
            cache_status = "✗ CACHE MISS"
        
        print(f"[CACHE] {path} - {cache_status} - {response.status_code} - {elapsed:.3f}s")
        
        return response


