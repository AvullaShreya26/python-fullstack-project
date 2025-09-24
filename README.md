
# Simple Event Registration System
A web application that allows an admin to post events and users to register for those events.

Helps organizers manage event registration efficiently and digitally.

Provides users a simple interface to view events and sign up.

Helps the admin track attendees easily without manual lists.

# Features

 # Admin Features

 Create Events – Admin can add new events with details like title, date, time, venue, and maximum attendees.

View Attendees – Admin can see the list of users registered for each event.

Manage Events – Admin can edit or delete events if needed.

 # User Features

View Events – Users can browse all upcoming events.

Register for Events – Users can register by providing their name, email, and optionally phone number.

Confirmation – Users receive a confirmation (optional, via email or notification).

 # Advanced Features

Limit Registrations – Prevent registration if maximum attendees are reached.

Search / Filter Events – Users can filter events by date, category, or venue.

Admin Dashboard – Shows analytics like total registrations per event.

Email Notifications – Send confirmation or reminders to users about events.

# projet structure

EVENT-REGISTRATION/
|
|---src/                   # core application logic
|     |---logic.py          #business logic and task
|operations
|     |__db.py              #database operations
|
|-----API/                  #backend api
|      |__main.py           #FASTAPI endpoints
|
|----Frontend/              #fortened application
|     |__app.py             #streamlit interface
|
|____requirements.txt       #python dependencies
|
|____readme.md              #python documentation
|
|____.env                  #python variables



# QUICK START
## prerequiestes

- python 3.8 or higher
- A supabase account 
- Git(Push,cloning)
### 1. clone or downlod the project

# option 1:  clone with git 
git clone <repository-url>
# option2 :Download and extra the zip files

### 2.install Dependencies
# install all python related packages
pip install -r requirements.txt

### 3. Setup Supabase Database
1.create a supabase project
2.create the task table
-go to supabase sql editor
RUN the SQL command:

  CREATE TABLE IF NOT EXISTS events (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title TEXT NOT NULL,                  -- Event title
    description TEXT,                     -- Event description
    date DATE NOT NULL,                   -- Event date
    time TIME,                            -- Event time
    venue TEXT,                           -- Event location
    max_attendees INT,                    -- Max number of participants
    created_at TIMESTAMP DEFAULT NOW()    -- Record creation time
);


CREATE TABLE IF NOT EXISTS registrations (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    event_id BIGINT NOT NULL,             -- References the event
    name TEXT NOT NULL,                   -- User name
    email TEXT NOT NULL,                  -- User email
    phone TEXT,                           -- Optional phone number
    registered_at TIMESTAMP DEFAULT NOW(),-- Registration time
    FOREIGN KEY (event_id) REFERENCES events(id)  -- Link to Events table
);
'''



