from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from main.models import WebhookEvent

@method_decorator(csrf_exempt, name='dispatch')
class GithubWebhookView(View):
    
    def post(self, request, *args, **kwargs):
        try:
            # Parse the incoming JSON payload from the request
            payload = json.loads(request.body)
            
            # Extract the event type (e.g., push, pull request, etc.)
            event_type = request.headers.get('X-GitHub-Event', 'Unknown')
            
            # Extract relevant information from the payload
            repository_name = payload['repository']['full_name']
            repository_url = payload['repository']['html_url']
            pusher = payload['pusher']['name']
            head_commit = payload['head_commit']
            commit_message = head_commit['message']
            commit_url = head_commit['url']
            
            # Customize the description by appending commit message to 'New Updates: '
            description = f"New Updates: {commit_message}"
            
            # Save the event to the database
            WebhookEvent.objects.create(
                event_type=event_type,
                description=description,
                repository=repository_name,
                repository_url=repository_url,
                commit_url=commit_url,
                pusher=pusher
            )
            
            # Return a success response
            return JsonResponse({"message": "Webhook received and processed successfully"}, status=200)
        
        except KeyError as e:
            # Handle missing key errors in payload
            return JsonResponse({"error": f"Missing key in payload: {str(e)}"}, status=400)
        
        except json.JSONDecodeError:
            # Handle JSON parsing errors
            return JsonResponse({"error": "Invalid JSON payload"}, status=400)
        
        except Exception as e:
            # Handle any other exceptions
            return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)
