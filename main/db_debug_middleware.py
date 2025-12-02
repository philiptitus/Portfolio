import time
from django.utils.deprecation import MiddlewareMixin
from django.db import connection, reset_queries


class DBDebugMiddleware(MiddlewareMixin):
    """Middleware to log database queries"""
    
    def process_request(self, request):
        reset_queries()
        request._db_start_time = time.time()
        return None
    
    def process_response(self, request, response):
        elapsed = time.time() - request._db_start_time
        path = request.path
        query_count = len(connection.queries)
        
        if query_count > 0:
            total_time = sum(float(q['time']) for q in connection.queries)
            status = f"DB QUERIES: {query_count}, TIME: {total_time:.3f}s"
        else:
            status = "NO DB QUERIES (✓ Cached)"
        
        print(f"[DB] {path} - {status} - Response time: {elapsed:.3f}s")
        
        # Optional: Print individual queries
        if query_count > 0 and query_count <= 5:
            for i, q in enumerate(connection.queries, 1):
                print(f"  Query {i}: {q['sql'][:100]}... ({q['time']}s)")
        
        return response
