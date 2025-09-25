# db.py
import os
from supabase import create_client
from dotenv import load_dotenv

# Environment variables
load_dotenv()
URL = os.getenv("SUPABASE_URL")
KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(URL, KEY)

# ------------- EVENTS ------------- #
def create_event(title: str, description: str, date: str, time: str, venue: str, max_attendees: int):
    data = {
        "title": title,
        "description": description,
        "date": date,
        "time": time,
        "venue": venue,
        "max_attendees": max_attendees
    }
    response = supabase.table("events").insert(data).execute()
    return response.data  

def get_all_events():
    response = supabase.table("events").select("*").execute()
    return response.data

def get_event_by_id(event_id: int):
    response = supabase.table("events").select("*").eq("id", event_id).single().execute()
    return response.data

def update_event(event_id: int, title=None, description=None, date=None, time=None, venue=None, max_attendees=None):
    """
    Update an existing event. Only provided fields will be updated.
    """
    data = {}
    if title: data["title"] = title
    if description: data["description"] = description
    if date: data["date"] = date
    if time: data["time"] = time
    if venue: data["venue"] = venue
    if max_attendees: data["max_attendees"] = max_attendees

    response = supabase.table("events").update(data).eq("id", event_id).execute()
    return response.data

def delete_event(event_id: int):
    response = supabase.table("events").delete().eq("id", event_id).execute()
    return response.data

# ------------- REGISTRATIONS ------------- #
def register_user(event_id: int, name: str, email: str, phone: str = None):
    data = {
        "event_id": event_id,
        "name": name,
        "email": email,
        "phone": phone
    }
    response = supabase.table("registrations").insert(data).execute()
    return response.data

def get_registrations_for_event(event_id: int):
    response = supabase.table("registrations").select("*").eq("event_id", event_id).execute()
    return response.data

def delete_registration(registration_id: int):
    response = supabase.table("registrations").delete().eq("id", registration_id).execute()
    return response.data
