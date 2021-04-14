
# 🤖 ymca-auto-booker

A selenium-python app that automatically enrolls you in your preferred workout session (and soon group classes) at 
YMCA-YWCA National Capital Region locations.

## Background

As of March 19, 2021, Ottawa is in lockdown level red limiting gym capacity to just 10 persons per a session.  The YMCA 
allows limited booking of their classes daily at 7 AM for up to 7 days in advance. The most desirable slots are often 
booked within minutes of becoming available. This project was created so that users can automatically book workout sessions
before the time slot is filled.

## How it Works

Using Selenium WebDriver, the Python code will navigate through the YMCA site and book a workout session according to the
parameters set in the config file: location and preferred time slot(s). The app is hosted by Heroku and uses the scheduler 
to run the app daily at 7:00 AM EST to make bookings for 7 days in advance.

## Installation
1. ``` git clone https://github.com/StevenAdema/ymca-auto-booker.git ```
2. ``` pip install -r requirements.txt ```
3. ``` heroku create ```
4. ``` git push heroku main ```
5. ``` heroku addons: create scheduler:standard ```
6. ``` heroku addons:open scheudler ```
7. In the Heroku Scheduler Dashboard add a new job and set to 03:00 (07:00 EST)

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

## Demo

![YMCA auto-booking selenium bot](/config/demo.gif?raw=true)


