from supabase import create_client
import os

url = os.environ.get("url")
key = os.environ.get("key")
supabase = create_client(url, key)

def log_error(msg):
    try:
        supabase.table("logss").insert({
            "error": str(msg)
        }).execute()
    except Exception as e:
        print(e)
        