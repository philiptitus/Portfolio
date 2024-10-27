from django.core.mail import EmailMessage
import random
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from .models import *
import logging












import mimetypes
from supabase import create_client, Client

# Supabase configuration
SUPABASE_URL = settings.SUPABASE_URL  # Replace with your Supabase URL
SUPABASE_KEY = settings.SUPABASE_KEY  # Replace with your Supabase Key
BUCKET_NAME = "Portfolio"  # Replace with your bucket name

# Initialize the Supabase client
def init_supabase() -> Client:
    client = create_client(SUPABASE_URL, SUPABASE_KEY)
    return client

# Function to upload a file to Supabase bucket
def upload_file_to_supabase(file, bucket_name: str, destination_path: str):
    supabase = init_supabase()

    # Get the MIME type of the file based on its extension
    mime_type, _ = mimetypes.guess_type(file.name)

    # Default to 'application/octet-stream' if the MIME type cannot be determined
    if mime_type is None:
        mime_type = 'application/octet-stream'

    # Read the file content
    file_content = file.read()

    bucket = supabase.storage.from_(bucket_name)
    res = bucket.upload(destination_path, file_content, file_options={"content-type": mime_type})

    # Check for successful upload by status code or data presence
    if res.status_code == 200:  # Check for success (or adjust based on response status)
        public_url = bucket.get_public_url(destination_path)
        return public_url
    else:
        raise Exception(f"Upload failed with error: {res.json()}")  # Use .json() to inspect the error








logger = logging.getLogger(__name__)

# Function to delete a file from Supabase bucket
def delete_file_from_supabase(bucket_name: str, file_path: str):
    logger = logging.getLogger(__name__)
    supabase = init_supabase()
    bucket = supabase.storage.from_(bucket_name)

    logger.info(f"Attempting to delete file: {file_path}")

    res = bucket.remove([file_path])

    # Check if the deletion was successful
    if all(item['status_code'] == 200 for item in res):
        logger.info(f"Successfully deleted file: {file_path}")
        return True
    else:
        error_messages = [item['error'] for item in res if 'error' in item]
        logger.error(f"Delete failed with error: {error_messages}")
        raise Exception(f"Delete failed with error: {error_messages}")










