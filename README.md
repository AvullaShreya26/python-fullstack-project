
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
go to supabase sql editor
RUN the SQL command:
```sql
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

``` 
3. **Get your credentials

### 4.Configure environment variables

1.create a .env file in root folder
2.Add your supabase cerdentials to .env
SUPABASE_URL-your-project-url
sUPABASE_KEY-anony-key

### Example
SUPABASE_URL="https://gspuunxaovgfpaiughpv.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdzcHV1bnhhb3ZnZnBhaXVnaHB2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODIwODgsImV4cCI6MjA3MzY1ODA4OH0.Ky7gKQnRu2OPxkDZA0d67rKesZTv5Gw2kNO7gnuvl4g"

### 5.Run the Application

# streamlit frontend

streamlit run Frontend/app.py

the app will open in the browser at 'http://localhost:8080'

## FASTAPI backend

cd API
python main.py
The api will be available at 'http://localhost:8080'

### How to Use
For Admin

Login as admin (if authentication is implemented).

Add a new event by entering:

Title

Description

Date & Time

Venue

Maximum number of attendees

View all registrations for each event.

Edit or delete events if required.

For Users

Browse the list of upcoming events.

Click on an event to see details.

Register for the event by entering:

Name

Email

Optional phone number

Optional: receive confirmation or reminder emails.

### Technical Details

Database Design:

Events table stores event details.

Registrations table stores user registrations and links to events using event_id.

Data Flow:

Admin inserts event → stored in Events table.

User registers → stored in Registrations table with reference to event.

Admin fetches registration data for reporting.

Optional Enhancements:

Limit registrations if event is full.

Filter/search events by date or venue.

Send email notifications using a background job.

### Technologies used

***Frontend***: Streamlit (python web framework)
***Backend***: FastAPI (python REST API framework)
***Database***: Supabase (PostgreSQL based backend as a service)
***Language***: Python 3.8+

### Key Components
***src/db.py***: Database operations, handles all CRUD operations with Supabase

***src/logic.py**: Business logic, handles validation and processing

### Trouble shooting

***Supabase Connection**: Check SUPABASE_URL & SUPABASE_KEY in .env.

***Table Errors**: Verify table names (events, registrations) and column names match exactly.

**ID / UUID Issues**: Ensure event_id in registrations exists in events table.

**Data Not Showing**: Check SQL editor to confirm rows exist; verify query filters.

**Email / Reminders**: Test SMTP/API credentials; ensure scheduler is running.

**Python Errors**: Activate correct environment; install required packages (pip install supabase).




### Future Enhancements

***Search & Filter Events*** – Users can find events by date, category, or venue.

***User Dashboard*** – Users can view all events they registered for and track their registrations.

***Export & Analytics for Admin*** – Admin can export attendee lists and view registration trends.

***Automated Notifications*** – Send confirmation and reminder emails to users.

***Role-Based Access & Security*** – Differentiate admin and user permissions; add social/OTP login.

***Mobile-Friendly UI & Event Features*** – Responsive interface, waitlist system, categories, and feedback for events.

## Support

If you encounter any issues or have questions : 
  - contact : 9398699330
  - email : avulla26@gmail.com



