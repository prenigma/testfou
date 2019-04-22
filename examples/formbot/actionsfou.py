# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union

import json

from datetime import date

from datetime import datetime

from rasa_core_sdk import ActionExecutionRejection, Action
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT


class SearchFlightsActions(Action):
    def name(self):
        return 'action_search_flight'

    def run(self, dispatcher, tracker, domain):
        concerts = [
            {"flightNumber": "EK 144", "destination": "London", "depatureDate": "2019-04-16T10:00:00.000Z"},
            {"flightNumber": "EK 145", "destination": "Toronto", "depatureDate": "2019-04-16T10:00:00.000Z"},
            {"flightNumber": "EK 146", "destination": "Frankfurt", "depatureDate": "2019-04-16T10:00:00.000Z"},
            {"flightNumber": "EK 147", "destination": "London", "depatureDate": "2019-04-17T10:00:00.000Z"}
        ]

        segments = [{
            "id": 1,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-21",
            "origin_display_date": "Sun, Apr 21",
            "origin_time": "04:15 AM",
            "destinationcode": "LHR",
            "destination": "London",
            "destination_date": "2019-04-21",
            "destination_display_day": "Sun, Apr 21",
            "destination_time": "7:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 571",
            "number_stops": "0"
        },
        {
            "id": 2,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-21",
            "origin_display_date": "Sun, Apr 21",
            "origin_time": "08:15 AM",
            "destinationcode": "LHR",
            "destination": "London",
            "destination_date": "2019-04-21",
            "destination_display_day": "Sun, Apr 21",
            "destination_time": "11:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 576",
            "number_stops": "0"
        },
        {
            "id": 3,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-22",
            "origin_display_date": "Mon, Apr 22",
            "origin_time": "04:15 AM",
            "destinationcode": "LHR",
            "destination": "London",
            "destination_date": "2019-04-22",
            "destination_display_day": "Mon, Apr 22",
            "destination_time": "7:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 571",
            "number_stops": "0"
        },
        {
            "id": 4,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-22",
            "origin_display_date": "Mon, Apr 22",
            "origin_time": "08:15 AM",
            "destinationcode": "LHR",
            "destination": "London",
            "destination_date": "2019-04-22",
            "destination_display_day": "Mon, Apr 22",
            "destination_time": "11:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 576",
            "number_stops": "0"
        }
        ]


        destination = tracker.get_slot("destination")
        flightclass = tracker.get_slot("flightclass")
        headcount = tracker.get_slot("headcount")
        print("DESTINATION: ", destination)
        proposedFlights = [flight for flight in segments if flight['destination'].lower()==destination.lower()]
        data = {}
        data['type'] = 'flightoptions'
        data['trip_class'] = flightclass
        data['price'] = "0"
        data['duration'] = "7hrs 25 mins"
        data['passengers'] = {"adults": headcount, "children": 0, "infants":0}
        data['segments'] = proposedFlights
        json_data = json.dumps(data)
        #dispatcher.utter_message(output_json)
        dispatcher.utter_attachment(json_data)
        return [SlotSet("flightoptions", json_data)]   

class BookFlightActions(Action):
    def name(self):
        return 'action_book_flight'

    def run(self, dispatcher, tracker, domain):
        
        segments = [{
            "id": 1,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-21",
            "origin_display_date": "Sun, Apr 21",
            "origin_time": "04:15 AM",
            "destinationcode": "LHR",
            "destination": "London",
            "destination_date": "2019-04-21",
            "destination_display_day": "Sun, Apr 21",
            "destination_time": "7:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 571",
            "number_stops": "0"
        },
        {
            "id": 2,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-21",
            "origin_display_date": "Sun, Apr 21",
            "origin_time": "08:15 AM",
            "destinationcode": "LHR",
            "destination": "London",
            "destination_date": "2019-04-21",
            "destination_display_day": "Sun, Apr 21",
            "destination_time": "11:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 576",
            "number_stops": "0"
        },
        {
            "id": 3,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-22",
            "origin_display_date": "Mon, Apr 22",
            "origin_time": "04:15 AM",
            "destinationcode": "LHR",
            "destination": "London",
            "destination_date": "2019-04-22",
            "destination_display_day": "Mon, Apr 22",
            "destination_time": "7:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 571",
            "number_stops": "0"
        },
        {
            "id": 4,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-22",
            "origin_display_date": "Mon, Apr 22",
            "origin_time": "08:15 AM",
            "destinationcode": "LHR",
            "destination": "London",
            "destination_date": "2019-04-22",
            "destination_display_day": "Mon, Apr 22",
            "destination_time": "11:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 576",
            "number_stops": "0"
        }
        ]
        selectedflightnumber = tracker.get_slot("selectedflightnumber")
        print("selectedflightnumber: ", selectedflightnumber)
        if(selectedflightnumber is not None):
            proposedFlights = [flight for flight in segments if flight['flight_number'].lower()==selectedflightnumber.lower()]
            output_json = json.dumps(proposedFlights)
            print("PROPOSED FLIGHTS: ", output_json)
            dispatcher.utter_message("Perfect, i rebooked you")
            return [SlotSet("selectedflight", output_json)]
        else:
            dispatcher.utter_message("Please select a flight")         

class GetPassengerFlightDetails(Action):
    def name(self):
        return 'action_get_flight_details'

    def run(self, dispatcher, tracker, domain):

        destination = "London"
        flightclass = "Economy"
        passengername = "John"
        hourdelay = "7"
        headcount = "2"
        
        sender = tracker.current_state()['sender_id']
        print("SENDER")
        print(sender)
        #description = " we called get passenger flight details "
        #dispatcher.utter_message("{}".format(description))
        return [SlotSet("destination", destination), SlotSet("flightclass", flightclass), SlotSet("passengername", passengername),
    SlotSet("hourdelay", hourdelay), SlotSet("headcount", headcount)]


class LoginAction(Action):
    def name(self):
        return 'action_login'

    def run(self, dispatcher, tracker, domain):

        username = tracker.get_slot("username")
        password = tracker.get_slot("password")
        photolink = 'https://doc-0k-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/7sl1nkb3c9ek1rhpbtit7gsfhbjjd7f9/1555725600000/11429114590258316664/*/1usBdf8hMCTBFhtkwlVAvOgiTi7HWEqjY' 
        data = {}
        profile = {}
        profile['name'] = username
        profile['photo'] = photolink
        profile['weather'] = 'Clear with periodic 28'
        profile['language'] = "fr_FR"
        milesstatus = {}
        milesstatus['awardmiles'] = "46,000 M"
        milesstatus['statusmiles'] = "30,000"
        milesstatus['flightsegment'] = "7"
        milesstatus['evoucher'] = "2"
        milesstatus['percentage'] = "25"
        milesstatus['lastdestination'] = "Singapur"
        profile['milesstatus'] = milesstatus
        activity = {}
        activity['date'] = "15.04.2019"
        activity['destination'] = "Singapur - Dubai"
        activity['awardmiles'] = "15,000"
        activity['executivebonus'] = "2,500"
        activity['statusmiles'] = "15,000"
        activity['executivebonus'] = "2,500"
        activity['flightnumber'] = "EK450"
        activity["flightclass"] = "Business Class"

        activity2 = {}
        activity2['date'] = "10.02.2019"
        activity2['destination'] = "London - Dubai"
        activity2['awardmiles'] = "15,000"
        activity2['executivebonus'] = "2,500"
        activity2['statusmiles'] = "15,000"
        activity2['executivebonus'] = "2,500"
        activity2['flightnumber'] = "EK150"
        activity2["flightclass"] = "Business Class"

        activities = [activity, activity2]

        profile['activities'] = activities

        data['sender'] = username
        data['profile'] = profile
        json_data = json.dumps(data) 
        #description = " we called get passenger flight details "
        dispatcher.utter_attachment(json_data)
        return [SlotSet("profile_type", "operations")]   

class SearchChangeDesttinationFlightsActions(Action):
   def name(self):
       return 'action_search_change_destination_flight'

   def run(self, dispatcher, tracker, domain):

       
       segments = [{
            "id": 1,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-21",
            "origin_display_date": "Sun, Apr 21",
            "origin_time": "04:15 AM",
            "destinationcode": "LHR",
            "destination": "Toronto",
            "destination_date": "2019-04-21",
            "destination_display_day": "Sun, Apr 21",
            "destination_time": "7:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 171",
            "number_stops": "0"
        },
        {
            "id": 2,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-21",
            "origin_display_date": "Sun, Apr 21",
            "origin_time": "08:15 AM",
            "destinationcode": "LHR",
            "destination": "Toronto",
            "destination_date": "2019-04-21",
            "destination_display_day": "Sun, Apr 21",
            "destination_time": "11:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 176",
            "number_stops": "0"
        },
        {
            "id": 3,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-22",
            "origin_display_date": "Mon, Apr 22",
            "origin_time": "04:15 AM",
            "destinationcode": "LHR",
            "destination": "Toronto",
            "destination_date": "2019-04-22",
            "destination_display_day": "Mon, Apr 22",
            "destination_time": "7:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 171",
            "number_stops": "0"
        },
        {
            "id": 4,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-22",
            "origin_display_date": "Mon, Apr 22",
            "origin_time": "08:15 AM",
            "destinationcode": "LHR",
            "destination": "Toronto",
            "destination_date": "2019-04-22",
            "destination_display_day": "Mon, Apr 22",
            "destination_time": "11:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 176",
            "number_stops": "0"
        }
        ] 
       destination = tracker.get_slot("destination")
       flightclass = tracker.get_slot("flightclass")
       headcount = tracker.get_slot("headcount")
       print("DESTINATION: ", destination)
       proposedFlights = [flight for flight in segments if flight['destination'].lower()==destination.lower()]
       data = {}
       data['type'] = 'flightoptions'
       data['trip_class'] = flightclass
       data['price'] = "0"
       data['duration'] = "7hrs 25 mins"
       data['passengers'] = {"adults": headcount, "children": 0, "infants":0}
       data['segments'] = proposedFlights
       json_data = json.dumps(data)
       #dispatcher.utter_message(output_json)
       dispatcher.utter_attachment(json_data) 
       return [SlotSet("flightoptions", json_data)]  

class SearchUpgradeFlightsActions(Action):
    def name(self):
        return 'action_search_upgrade_flight'

    def run(self, dispatcher, tracker, domain):
        segments = [{
            "id": 1,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-21",
            "origin_display_date": "Sun, Apr 21",
            "origin_time": "04:15 AM",
            "destinationcode": "LHR",
            "destination": "Toronto",
            "destination_date": "2019-04-21",
            "destination_display_day": "Sun, Apr 21",
            "destination_time": "7:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 171",
            "number_stops": "0"
        },
        {
            "id": 2,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-21",
            "origin_display_date": "Sun, Apr 21",
            "origin_time": "08:15 AM",
            "destinationcode": "LHR",
            "destination": "Toronto",
            "destination_date": "2019-04-21",
            "destination_display_day": "Sun, Apr 21",
            "destination_time": "11:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 176",
            "number_stops": "0"
        },
        {
            "id": 3,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-22",
            "origin_display_date": "Mon, Apr 22",
            "origin_time": "04:15 AM",
            "destinationcode": "LHR",
            "destination": "Toronto",
            "destination_date": "2019-04-22",
            "destination_display_day": "Mon, Apr 22",
            "destination_time": "7:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 171",
            "number_stops": "0"
        },
        {
            "id": 4,
            "origincode": "DXB",
            "origin": "Dubai",
            "origin_date": "2019-04-22",
            "origin_display_date": "Mon, Apr 22",
            "origin_time": "08:15 AM",
            "destinationcode": "LHR",
            "destination": "Toronto",
            "destination_date": "2019-04-22",
            "destination_display_day": "Mon, Apr 22",
            "destination_time": "11:00 PM",
            "airline": "Emirates Airlines",
            "flight_number": "EK 176",
            "number_stops": "0"
        }
        ] 
        destination = tracker.get_slot("destination")
        flightclass = tracker.get_slot("flightclass")
        headcount = tracker.get_slot("headcount")
        print("DESTINATION: ", destination)
        proposedFlights = [flight for flight in segments if flight['destination'].lower()==destination.lower()]
        data = {}
        data['type'] = 'flightoptions'
        data['trip_class'] = flightclass
        data['price'] = "0"
        data['duration'] = "7hrs 25 mins"
        data['passengers'] = {"adults": headcount, "children": 0, "infants":0}
        data['segments'] = proposedFlights
        json_data = json.dumps(data)
        #dispatcher.utter_message(output_json)
        dispatcher.utter_attachment(json_data) 
        return [SlotSet("flightoptions", json_data)]

class BookRestaurantActions(Action):
    def name(self):
        return 'action_book_restaurant'

    def run(self, dispatcher, tracker, domain):
        
        restaurants = [
        {
            "id": "1",
            "name": "Paul",
            "stars": 4,
            "cuisine_restaurant": "French restaurant",
            "photoCount": 3,
            "photos": [
                {
                    "url": "https://doc-0k-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/ub92u1vofsvsou59ri3mbm5gq3jfckkk/1555725600000/11429114590258316664/*/1Khq6ncv3CRwW1B2bHPEoSUG-oS5a7OPZ",

                },

                {
                    "url": "https://doc-0s-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/dcruvqc2ttls5e4i2r91t8ib2q3h5adt/1555725600000/11429114590258316664/*/117xov5OqO8AclNi5BOcguAPy6XRjDTEO"
                },

                {
                    "url": "https://doc-0o-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/po701g4t0mkiesg0ip287gsslephi4ee/1555725600000/11429114590258316664/*/1h3Aqx1Ja1-EoSldvHejhMXstTnCWkdWP"
                }
            ],
            "address": "Concourse B,Terminal 3,Dubai International Airport - Dubai",
            "Reservation": "Sun, Apr 21, 2 people",
            "cuisine": "French",
            "open_time":{
                "Monday": "24 hours open",
                "Tuesday": "24 hours open",
                "Wednesday": "24 hours open",
                "Thursday": "24 hours open",
                "Friday": "24 hours open",
                "Saturday": "24 hours open",
                "Sunday": "24 hours open"
            }
        },


        {
            "id": "2",
            "name": "Hard Rock Cafe",
            "stars": 4,
            "cuisine_restaurant": "American restaurant",
            "photoCount": 3,
            "photos": [
                {
                    "url": "https://doc-04-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/a76ujr439avju72a6s7mqm59jaujljj3/1555725600000/11429114590258316664/*/1CEdYSP_Q5LO8wgjcYHvpV0EVVkU6B7eC"

                },

                {
                    "url": "https://doc-0o-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/v0uudi4johan6fg37s0qjjobct8cnfau/1555725600000/11429114590258316664/*/1APP8Qz5lwgO6-ZIUgTmIcY0qBnpMsJ2x"
                },

                {
                    "url": "https://doc-08-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/47cfrnu2pghv96i7dpjr40hs7fpenhpo/1555725600000/11429114590258316664/*/1-NXaVrNAH-KMn5QffbDvTtNiYrXfhsTt"
                }
            ],
            "address": "Gate 25, Terminal 3 - Dubai International Airport Concourse B - Dubai",
            "Reservation": "Sun, Apr 21, 2 people",
            "cuisine": "French",
            "open_time":{
                "Monday": "24 hours open",
                "Tuesday": "24 hours open",
                "Wednesday": "24 hours open",
                "Thursday": "24 hours open",
                "Friday": "24 hours open",
                "Saturday": "24 hours open",
                "Sunday": "24 hours open"
            }
        }
        ]


        selectedflightnumber = tracker.get_slot("selectedrestaurantid")
        print("selectedrestaurantid: ", selectedflightnumber)
        proposedFlights = [flight for flight in restaurants if flight['id']==selectedflightnumber]
        output_json = json.dumps(proposedFlights)
        print("PROPOSED FLIGHTS: ", output_json)
        dispatcher.utter_message("Perfect, i booked for you a table")
        return [SlotSet("selectedrestaurant", proposedFlights)]  

class SearchRestaurantsActions(Action):
    def name(self):
        return 'action_search_restaurant'

    def run(self, dispatcher, tracker, domain):
        restaurants = [
        {
            "id": "1",
            "name": "Paul",
            "stars": 4,
            "cuisine_restaurant": "French restaurant",
            "photoCount": 3,
            "photos": [
                {
                    "url": "https://doc-0k-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/ub92u1vofsvsou59ri3mbm5gq3jfckkk/1555725600000/11429114590258316664/*/1Khq6ncv3CRwW1B2bHPEoSUG-oS5a7OPZ",

                },

                {
                    "url": "https://doc-0s-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/dcruvqc2ttls5e4i2r91t8ib2q3h5adt/1555725600000/11429114590258316664/*/117xov5OqO8AclNi5BOcguAPy6XRjDTEO"
                },

                {
                    "url": "https://doc-0o-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/po701g4t0mkiesg0ip287gsslephi4ee/1555725600000/11429114590258316664/*/1h3Aqx1Ja1-EoSldvHejhMXstTnCWkdWP"
                }
            ],
            "address": "Concourse B,Terminal 3,Dubai International Airport - Dubai",
            "Reservation": "Sun, Apr 21, 2 people",
            "cuisine": "French",
            "open_time":{
                "Monday": "24 hours open",
                "Tuesday": "24 hours open",
                "Wednesday": "24 hours open",
                "Thursday": "24 hours open",
                "Friday": "24 hours open",
                "Saturday": "24 hours open",
                "Sunday": "24 hours open"
            }
        },


        {
            "id": "2",
            "name": "Hard Rock Cafe",
            "stars": 4,
            "cuisine_restaurant": "American restaurant",
            "photoCount": 3,
            "photos": [
                {
                    "url": "https://doc-04-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/a76ujr439avju72a6s7mqm59jaujljj3/1555725600000/11429114590258316664/*/1CEdYSP_Q5LO8wgjcYHvpV0EVVkU6B7eC"

                },

                {
                    "url": "https://doc-0o-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/v0uudi4johan6fg37s0qjjobct8cnfau/1555725600000/11429114590258316664/*/1APP8Qz5lwgO6-ZIUgTmIcY0qBnpMsJ2x"
                },

                {
                    "url": "https://doc-08-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/47cfrnu2pghv96i7dpjr40hs7fpenhpo/1555725600000/11429114590258316664/*/1-NXaVrNAH-KMn5QffbDvTtNiYrXfhsTt"
                }
            ],
            "address": "Gate 25, Terminal 3 - Dubai International Airport Concourse B - Dubai",
            "Reservation": "Sun, Apr 21, 2 people",
            "cuisine": "French",
            "open_time":{
                "Monday": "24 hours open",
                "Tuesday": "24 hours open",
                "Wednesday": "24 hours open",
                "Thursday": "24 hours open",
                "Friday": "24 hours open",
                "Saturday": "24 hours open",
                "Sunday": "24 hours open"
            }
        }
        ]

        data = {}
        data['type'] = 'restaurantoptions'
        data['restaurants'] = restaurants
        json_data = json.dumps(data)

       
        dispatcher.utter_attachment(json_data)
        return [SlotSet("restaurantoptions", restaurants)]  


class SearchHotelsActions(Action):
    def name(self):
        return 'action_search_hotel'

    def run(self, dispatcher, tracker, domain):
        hotels= [
        {
            "id": 1,
            "name": "Sleep n'fly by yarn, sleep lounge",
            "address": "International Dubai Airport - Terminal 3, Concource A, opposite Gate A1 - Dubai",
            "stars": 4,
            "numberRoom": "1 Room",
            "numberAdults": "1 Adult",
            "stay_duration": "Apr 21 - Apr 21, 1 night",
            "room_description": "One Bedroom",
            "price": "AED 348,00 /per Traveller",
            "photoCount": 3,
            "photos": [
                {
                    "url": "https://doc-0c-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/g147qncu7q1284crr8kf0vkt6denjedn/1555725600000/11429114590258316664/*/1BqkIOov9jj-DcrDWwvTraArcpEzWnaum"
                },

                {
                    "url": "https://doc-0g-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/shqqoravt2af12m54bo8s888ni9kl9pp/1555718400000/11429114590258316664/*/1ahEIMoocW79gu1Tgnit6ibhkCikAHy5Q"
                },

                {
                    "url": "https://doc-14-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/9iftr05026at0pmhrqvo3vlelojnbc7s/1555718400000/11429114590258316664/*/1FieFZPRmRm-oLKozCr4ZHkU-CqFSDk3F"
                }
            ],
            "Stay": "Sun, Apr 21, 2 poeple",
            "facilities": [
                "Air conditioning",
                "Wake-up service",
                "Linens",
                "Entire unit located on ground floor"
            ],
            "room": "One Room",
            "hotel_description": "Conveniently located opposite Gate A1 at A-Gate (Terminal 3, inside the DXB transit area), the Sleep'n fly Sleep Lounge is inspired by Scandinavian design for comfort, style ans necessity"
        },
         {  "id":2,
            "name": "Le meridien",
            "address": "International Dubai Airport - Terminal 3, Concource A, opposite Gate A1 - Dubai",
            "stars": 4,
            "numberRoom": "1 Room",
            "numberAdults": "1 Adult",
            "stay_duration": "Apr 21 - Apr 21, 1 night",
            "room_description": "One Bedroom",
            "price": "AED 348,00 /per Traveller",
            "photoCount": 3,
            "photos": [
                {
                    "url": "https://doc-0c-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/g147qncu7q1284crr8kf0vkt6denjedn/1555725600000/11429114590258316664/*/1BqkIOov9jj-DcrDWwvTraArcpEzWnaum"
                },

                {
                    "url": "https://doc-0g-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/shqqoravt2af12m54bo8s888ni9kl9pp/1555718400000/11429114590258316664/*/1ahEIMoocW79gu1Tgnit6ibhkCikAHy5Q"
                },

                {
                    "url": "https://doc-14-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/9iftr05026at0pmhrqvo3vlelojnbc7s/1555718400000/11429114590258316664/*/1FieFZPRmRm-oLKozCr4ZHkU-CqFSDk3F"
                }
            ],
            "Stay": "Sun, Apr 21, 2 poeple",
            "facilities": [
                "Air conditioning",
                "Wake-up service",
                "Linens",
                "Entire unit located on ground floor"
            ],
            "room": "One Room",
            "hotel_description": "Conveniently located opposite Gate A1 at A-Gate (Terminal 3, inside the DXB transit area), the Sleep'n fly Sleep Lounge is inspired by Scandinavian design for comfort, style ans necessity"
        }
        ]

        data = {}
        data['type'] = 'hoteloptions'
        data['hotels'] = hotels
        json_data = json.dumps(data)
        
        print("PROPOSED HOTEL: ", hotels)
        dispatcher.utter_attachment(json_data) 
        return [SlotSet("hoteloptions", hotels)]  

class BookHotelsActions(Action):
    def name(self):
        return 'action_book_hotel'

    def run(self, dispatcher, tracker, domain):
        hotels= [
        {
            "id": "1",
            "name": "Sleep n'fly by yarn, sleep lounge",
            "address": "International Dubai Airport - Terminal 3, Concource A, opposite Gate A1 - Dubai",
            "stars": 4,
            "numberRoom": "1 Room",
            "numberAdults": "1 Adult",
            "stay_duration": "Apr 21 - Apr 21, 1 night",
            "room_description": "One Bedroom",
            "price": "AED 348,00 /per Traveller",
            "photoCount": 3,
            "photos": [
                {
                    "url": "https://doc-0c-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/g147qncu7q1284crr8kf0vkt6denjedn/1555725600000/11429114590258316664/*/1BqkIOov9jj-DcrDWwvTraArcpEzWnaum"
                },

                {
                    "url": "https://doc-0g-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/shqqoravt2af12m54bo8s888ni9kl9pp/1555718400000/11429114590258316664/*/1ahEIMoocW79gu1Tgnit6ibhkCikAHy5Q"
                },

                {
                    "url": "https://doc-14-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/9iftr05026at0pmhrqvo3vlelojnbc7s/1555718400000/11429114590258316664/*/1FieFZPRmRm-oLKozCr4ZHkU-CqFSDk3F"
                }
            ],
            "Stay": "Sun, Apr 21, 2 poeple",
            "facilities": [
                "Air conditioning",
                "Wake-up service",
                "Linens",
                "Entire unit located on ground floor"
            ],
            "room": "One Room",
            "hotel_description": "Conveniently located opposite Gate A1 at A-Gate (Terminal 3, inside the DXB transit area), the Sleep'n fly Sleep Lounge is inspired by Scandinavian design for comfort, style ans necessity"
        },
         {  "id": "2",
            "name": "Le meridien",
            "address": "International Dubai Airport - Terminal 3, Concource A, opposite Gate A1 - Dubai",
            "stars": 4,
            "numberRoom": "1 Room",
            "numberAdults": "1 Adult",
            "stay_duration": "Apr 21 - Apr 21, 1 night",
            "room_description": "One Bedroom",
            "price": "AED 348,00 /per Traveller",
            "photoCount": 3,
            "photos": [
                {
                    "url": "https://doc-0c-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/g147qncu7q1284crr8kf0vkt6denjedn/1555725600000/11429114590258316664/*/1BqkIOov9jj-DcrDWwvTraArcpEzWnaum"
                },

                {
                    "url": "https://doc-0g-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/shqqoravt2af12m54bo8s888ni9kl9pp/1555718400000/11429114590258316664/*/1ahEIMoocW79gu1Tgnit6ibhkCikAHy5Q"
                },

                {
                    "url": "https://doc-14-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/9iftr05026at0pmhrqvo3vlelojnbc7s/1555718400000/11429114590258316664/*/1FieFZPRmRm-oLKozCr4ZHkU-CqFSDk3F"
                }
            ],
            "Stay": "Sun, Apr 21, 2 poeple",
            "facilities": [
                "Air conditioning",
                "Wake-up service",
                "Linens",
                "Entire unit located on ground floor"
            ],
            "room": "One Room",
            "hotel_description": "Conveniently located opposite Gate A1 at A-Gate (Terminal 3, inside the DXB transit area), the Sleep'n fly Sleep Lounge is inspired by Scandinavian design for comfort, style ans necessity"
        }
        ]

        selectedflightnumber = tracker.get_slot("selectedhotelid")
        print("selectedhotelid: ", selectedflightnumber)
        proposedFlights = [flight for flight in hotels if flight['id']==selectedflightnumber]
       
        dispatcher.utter_message("Perfect, i booked for you the requested hotel")
       
        return [SlotSet("hoteloptions", proposedFlights)]  

class SearchTasksDeplayedFlightActions(Action):
    
    def name(self):
        return 'action_get_delayed_flights'

    def run(self, dispatcher, tracker, domain):

        flightdelayed1 = {}
        flightdelayed1['flightNumber'] = "EK 145"
        flightDelayedPassengers1 =  [
                    {
                        "id": 1,
                        "pnr": 'XKDFK2',
                        "birthday": '04.04.1981',
                        "accompaniedPassengers": 0,
                        "statusMiles": '30,000',
                        "flightSegments": '7',
                        "eVouchers": '2',
                        "hasHotel": True,
                        "hasMeal": False
                    },
                    {
                        "id": 2,
                        "pnr": 'XKDFK1',
                        "birthday": '04.04.1982',
                        "accompaniedPassengers": 0,
                        "statusMiles": '60,000',
                        "flightSegments": '2',
                        "eVouchers": '0',
                        "hasHotel": False,
                        "hasMeal": True
                    }]
        flightdelayed1['flightDelayedPassengers'] = flightDelayedPassengers1

        flightdelayed2 = {}
        flightdelayed2['flightNumber'] = "EK 147"
        flightDelayedPassengers2 =  [
                    {
                        "id": 1,
                        "pnr": 'XKDFL5',
                        "birthday": '04.04.1981',
                        "accompaniedPassengers": 0,
                        "statusMiles": '10,000',
                        "flightSegments": '7',
                        "eVouchers": '2',
                        "hasHotel": True,
                        "hasMeal": False
                    },
                    {
                        "id": 2,
                        "pnr": 'XKDFL6',
                        "birthday": '04.04.1982',
                        "accompaniedPassengers": 0,
                        "statusMiles": '5,000',
                        "flightSegments": '2',
                        "eVouchers": '0',
                        "hasHotel": False,
                        "hasMeal": True
                    }]
        flightdelayed2['flightDelayedPassengers'] = flightDelayedPassengers2              

        flightsDelayed = [flightdelayed1, flightdelayed2]
       
        data = {}
        data['type'] = 'delayedflights'
        data['delayedflights'] = flightsDelayed
        json_data = json.dumps(data)
        
        print("deplayed flights: ", json_data)
        dispatcher.utter_attachment(json_data) 
        return [SlotSet("delayedflights", json_data)]

class GiveVoucherAction(Action):

    def name(self):
        return "action_give_voucher"


    def run(self, dispatcher, tracker, domain):
        pnr = tracker.get_slot("pnr")
        passenger_id = tracker.get_slot("passenger_id")
        voucher_type = tracker.get_slot("voucher_type")
        text_msg = "We will give passenger "+ pnr + "a voucher of type " + voucher_type
        print(text_msg)
        dispatcher.utter_message(text_msg)

class SearchOverviewVoucherForAFlightActions(Action):
    
    def name(self):
        return 'action_vouchers_for_flight'

    def run(self, dispatcher, tracker, domain):

    
        flightVouchers = {
                "id": 1,
                "number": 'XKDFKR1',
                "birthday": '04.04.1981',
                "accompaniedPassengers": 0,
                "statusMiles": '30,000',
                "flightSegments": '7',
                "eVouchers": '2',
                "hasHotel": True,
                "hasMeal": False
            },{
                "id": 2,
                "number": 'XKDFKR2',
                "birthday": '04.04.1982',
                "accompaniedPassengers": 0,
                "statusMiles": '50,000',
                "flightSegments": '2',
                "eVouchers": '0',
                "hasHotel": False,
                "hasMeal": True
            }
        flightVouchers2 = {
                "id": 1,
                "number": 'FKDFKR1',
                "birthday": '04.04.1991',
                "accompaniedPassengers": 0,
                "statusMiles": '30,000',
                "flightSegments": '17',
                "eVouchers": '20',
                "hasHotel": True,
                "hasMeal": False
            },{
                "id": 2,
                "number": 'FKDFKR2',
                "birthday": '04.04.1992',
                "accompaniedPassengers": 0,
                "statusMiles": '50,000',
                "flightSegments": '20',
                "eVouchers": '0',
                "hasHotel": False,
                "hasMeal": True
            }

        vouchersummary = [
            {
            "flightnumber": "EK 144",
            "vouchers": flightVouchers
            },
            {
            "flightnumber": "EK 145",
            "vouchers": flightVouchers2    
            }
        ]
        
         
        flightnumber = tracker.get_slot('voucherflight')
        text_msg = "Overview of Vouchers Given to Flight "+flightnumber
        error_msg = "No data available for the flight you entered "+flightnumber   
        print("VOUCHER FLIGHT NUMBER ", flightnumber)
        flightnumber = flightnumber.replace(" ", "")
        print("VOUCHER FLIGHT NUMBER without spaces", flightnumber)
        proposedvouchersummary = [flight for flight in vouchersummary if flight["flightnumber"].replace(" ", "").lower()==flightnumber.lower()]
        print("SIZE ", len(proposedvouchersummary))
        if (len(proposedvouchersummary) == 0):
            dispatcher.utter_message(error_msg)
            return  

        data = {}
        data['type'] = 'overviewvouchers'
        data['vouchersummary'] = proposedvouchersummary
        json_data = json.dumps(data)
        
        print("deplayed flights: ", json_data)
        dispatcher.utter_message(text_msg)
        dispatcher.utter_attachment(json_data) 
        #return [SlotSet("delayedflights", json_data)] 
        # 

class ShowRosterOverviewAction(Action):

    def name(self):
        return "action_show_roster"

    def run(self, dispatcher, tracker, domain):

        roster_date = tracker.get_slot("roster_date")
        today = date.today()
        # dd/mm/YY
        d1 = today.strftime("%d/%m/%Y")

        if (roster_date is None):
            print("d1 =", d1)
            roster_date = d1

        flights = [
        {
			"id": 1,
			"departure_time": "15:45",
            "arrival_time": "20:15",
            "departure_airport": "Dubai (DXB)",
            "arrival_airport": "London (LHR)",
            "flightdate": "22/04/2019"
		},
		{
			"id": 2,
			"departure_time": "09:55",
            "arrival_time": "12:55",
            "departure_airport": "London (LHR)",
            "arrival_airport": "Dubai (DXB)",
            "flightdate": "22/04/2019"
		},
		{
			"id": 3,
			"departure_time": "17:10",
            "arrival_time": "21:15",
            "departure_airport": "Dubai (DXB)",
            "arrival_airport": "Vienna (VIE)",
            "flightdate": "22/04/2019"
		},
		{
			"id": 4,
			"departure_time": "23:45",
            "arrival_time": "07:20",
            "departure_airport": "Vienna (VIE)",
            "arrival_airport": "Dubai (DXB)",
            "flightdate": "22/04/2019"
		},
        {
			"id": 5,
			"departure_time": "23:45",
            "arrival_time": "07:20",
            "departure_airport": "Vienna (VIE)",
            "arrival_airport": "Dubai (DXB)",
            "flightdate": "20/04/2019"
		},
        {
			"id": 6,
			"departure_time": "23:45",
            "arrival_time": "07:20",
            "departure_airport": "Vienna (VIE)",
            "arrival_airport": "Dubai (DXB)",
            "flightdate": "20/04/2019"
		},
        {
			"id": 7,
			"departure_time": "23:45",
            "arrival_time": "07:20",
            "departure_airport": "Vienna (VIE)",
            "arrival_airport": "Dubai (DXB)",
            "flightdate": "20/04/2019"
		}
	
	    ]
        overdueflights = [flight for flight in flights if datetime.strptime(flight["flightdate"], '%d/%m/%Y')  >= datetime.strptime(roster_date, '%d/%m/%Y')]

        completedflights = [flight for flight in flights if datetime.strptime(flight["flightdate"], '%d/%m/%Y')  < datetime.strptime(roster_date, '%d/%m/%Y')]

        data = {}
        overview = {}
        weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
        weekday = datetime.strptime(roster_date, '%d/%m/%Y').weekday()
        print(weekDays[weekday])
        overview["weekday"] = weekDays[weekday] 
        overview["completed_flights_count"] = len(completedflights)
        overview["overdue_flights_count"] = len(overdueflights)
        data["type"] = "showcrewrosteroverview"
        data['overview'] = overview
        data["completed_flights"] = completedflights
        data["overdue_flights"] = overdueflights
        json_data = json.dumps(data)
        
        print("ROSTER Overview: ", json_data)
       
        dispatcher.utter_attachment(json_data) 


class ShowOverviewTasksOnFlight(Action):

    def name(self):
        return "action_show_tasks_onflight"

    def run(self, dispatcher, tracker, domain):

        nextflightnumber = "EK 145" # Change it here to be read from DB
        data = {}
        overview = {}
        overview['title'] = "Tasks for your Flight"
        overview['flightnumber'] = nextflightnumber
        tasks = [
		{
			"id": 1,
			"description": "Deliver Article nr. 10 to Seat 04F"
		},
		{
			"id": 2,
			"description": "Organize a small Birthday-Surprise to Seat 02F :)"
		},
		{
			"id": 3,
			"description": "Diabetecs, special meal for Seat 02D"
		},
		{
			"id": 4,
			"description": "Passenger Seat 04A special vegan meal without salt"
		}
	
	    ]
        data['type'] = "showcrewonflighttasks"
        data['overview'] = overview
        data['tasks'] = tasks
        json_data = json.dumps(data)
        
        print("Tasks Overview for CREW: ", json_data)
       
        dispatcher.utter_attachment(json_data) 


class ShowOperationsTasksAction(Action):

    def name(self):
        return "action_show_operations_tasks"

    def run(self, dispatcher, tracker, domain):
        tasks = [
            {
                "id": 1,
                "title": 'Give Vouchers for Distrupted passenger on Flight EK 145',
                "time": '9:30 AM',
                "isIndicator": True
            },
            {
                "id": 2,
                "title": 'Give Vouchers for passenger on delayed Flight EK 146',
                "subTitle": 'Subtitle',
                "time": '11:40 AM',
                "isIndicator": False
            },
            {
                "id": 3,
                "title": 'Manage expected disruption on Gate B1',
                "subTitle": 'Subtitle',
                "time": '11:40 AM',
                "isIndicator": False
            },
            {
                "id": 4,
                "title": 'Call Team for Sync Meeting',
                "subTitle": 'Bad Weather expected tomorrow',
                "time": '11:40 AM',
                "isIndicator": False
            }
        ]
        data = {}
        overview = {}
        weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
        today = date.today()
        # dd/mm/YY
        d1 = today.strftime("%d/%m/%Y")
        weekday = datetime.strptime(d1, '%d/%m/%Y').weekday()
        print(weekDays[weekday])
        overview["weekday"] = weekDays[weekday] 
        completed = [task for task in tasks if task['isIndicator'] == True]
        overdue = [task for task in tasks if task['isIndicator'] == False]
        overview['completed_count'] = len(completed)
        overview['overdue_count'] = len(overdue)
        data['overview'] = overview
        data['tasks'] = tasks

        json_data = json.dumps(data)
        
        print("Tasks Overview for Operations: ", json_data)
       
        dispatcher.utter_attachment(json_data)    

class ChangeLanguageAction(Action):

    def name(self):
        return "action_change_language"

    def run(self, dispatcher, tracker, domain):
        language = tracker.get_slot("language")

        language_code = self.get_language_code(language)

        data={}
        data['type'] = "changelanguage"
        data['language'] = language_code
        json_data = json.dumps(data)

        print("We will now talk ", language)
        print("We will now talk language code", language_code)
        dispatcher.utter_attachment(json_data) 
        return [SlotSet("language_speak", language_code)]

    def get_language_code(self, language):
        switcher = {
        "english": "en_US",
        "french": "fr_FR",
        "german": "de_DE",
        "italian": "it_IT",
        "russian": "ru_RU",
        "arabic": "ar_AE",
        "chinese": "zh_CN",
        "hindi": "hi",
        "greek": "el",
        "spanish": "es_ES"
        }

        return switcher.get(language.lower(), "Invalid language")    



class ShowVoucherAction(Action):

    def name(self):
        return "action_show_voucher"

    def run(self, dispatcher, tracker, domain):
        voucher_type = tracker.get_slot("voucher_type")
        hotel_voucher = {
            "name": "Hotel Voucher",
            "information": "PRESENT THIS VOUCHER AT HOTEL CHECK-IN",
            "QR_code": "https://imagizer.imageshack.com/img923/6066/56rKD8.png",
            "passenger_name": "EDWARDS/SOPHIA",
            "booking_ref": "FPXLJJ",
            "hottel_name":"LE MERIDIEN",
            "room_description":"SINGLE",
            "meal":"BREAKFAST LUNCH"
        }
        
        meal_voucher= {
            "id": 1,
            "name": "Meal Voucher",
            "information": "PRESENT THIS VOUCHER AT RESTAURANT CHECK-IN",
            "QR_code": "https://imagizer.imageshack.com/img923/6066/56rKD8.png",
            "passenger_name": "ADAMS/JOHN",
            "booking_ref": "LJ6GA6",
            "resttaurantt_name":"Giraffe Stop",
            "meal":"International Restaurant"
        }

        sender = (tracker.current_state())["sender_id"]
        print("USER ID:", sender)

        #sender_id = (tracker.current_state())["sender"]
        #print("SENDER: ", sender_id)
        if(sender.lower()=="darshit"):
            voucher = hotel_voucher
            showoption = "showvoucherhotel"
        else:
            voucher = meal_voucher ## ADD later here if Meal, now not added since slot is not set
            showoption = "showvouchermeal"

        #if(voucher_type=="HOTEL"):
        #    voucher = hotel_voucher
        #   showoption = "showvoucherhotel"
        #else:
        #    voucher = meal_voucher ## ADD later here if Meal, now not added since slot is not set
        #    showoption = "showvouchermeal"

        data={}
        data['type'] = showoption
        data['voucher'] = voucher
        json_data = json.dumps(data)    
        
        dispatcher.utter_message("Here is your {vouchertype} Voucher")
        dispatcher.utter_attachment(json_data)
        return [SlotSet("voucher", voucher)]
              



class ShowLoungesAction(Action):

    def name(self):
        return "action_show_lounge"

    def run(self, dispatcher, tracker, domain):
        lounges = [

        {
            "id": 1,
            "photo": "https://imagizer.imageshack.com/img924/8836/zl7glO.png",
            "name": "Business Class Lounge",
            "address": "Terminal 3,Dubai International Airport - Dubai",
            "title": "Business Class Lounge",
            "open_now": "Open Now",
            "open_time":{
                "Monday": "24 hours open",
                "Tuesday": "24 hours open",
                "Wednesday": "24 hours open",
                "Thursday": "24 hours open",
                "Friday": "24 hours open",
                "Saturday": "24 hours open",
                "Sunday": "24 hours open"
            },
            "collaps_hours": "COLLAPS HOURS",
            "lounge_facilities": "Lounge Facilities",
            "lounge Facilites": [
                "Non-Smoking",
                "Shower",
                "Beer & Wine",
                "Newspaper & Magazines",
                "Spa Services",
                "TVs",
                "Wi-Fi"
            ],
            "collaps_facilities": "COLLAPS FACILITIES",
            "description": "In our Business Class Lounge in Dubai International airport Concourse B, you can now enjoy a personalised barista experience with Costa Coffee. A favourite among coffee lovers, Costa Coffee uses a unique blend from sustainably grown beans sourced from responsible farms. Replenish your caffeine levels in stylish surroundings with an espresso, soothe your soul with a fragrant herbal tea or indulge in a fresh pastry or cookie while you wait for your flight to board.",
            "directions": "Directions",
            "direction_photo": "https://imagizer.imageshack.com/img921/2062/xugq2v.png"        
        },

        {
            "id": 2,
            "photo": "https://imagizer.imageshack.com/img921/1920/6Y0rGn.png",
            "name": "First Class Lounge",
            "address": "Terminal 3,Dubai International Airport - Dubai",
            "titel": "FIRST Class Lounge",
            "open_now": "Open Now",
            "open_time":{
                "Monday": "24 hours open",
                "Tuesday": "24 hours open",
                "Wednesday": "24 hours open",
                "Thursday": "24 hours open",
                "Friday": "24 hours open",
                "Saturday": "24 hours open",
                "Sunday": "24 hours open"
            },
            "collaps_hours": "COLLAPS HOURS",
            "lounge_facilities": "Lounge Facilities",
            "lounge Facilites": [
                "Non-Smoking",
                "Shower",
                "Beer & Wine",
                "Newspaper & Magazines",
                "Spa Services",
                "TVs",
                "Wi-Fi"
            ],
            "collaps_facilities": "COLLAPS FACILITIES",
            "description": "Arrive feeling fully refreshed Our shower spas have everything you need to prepare for the next stage of your journey, including towels, luxury toiletries and hairdryers.",
            "directions": "Directions",
            "direction_photo": "https://imagizer.imageshack.com/img923/4965/Es8DNR.png"        
        }
        ]
        data={}
        data['type'] = "showlounges"
        data['lounges'] = lounges
        json_data = json.dumps(data)    
        
        dispatcher.utter_message("Here are a some lounges i would recommend")
        dispatcher.utter_attachment(json_data)



class BookLoungeAction(Action):

    def name(self):
        return "action_book_lounge"

    def run(self, dispatcher, tracker, domain):
        lounges = [{"id": 1, "name": "Business Class Lounge"}, {"id": 2, "name": "First Class Lounge"}]
        selectedloungeid = tracker.get_slot("selectedloungeid")
        print("selectedloungeid: ", selectedloungeid)
        selectedlounge = [flight for flight in lounges if flight['id']==selectedloungeid]
        print("selectedloungeid: ", selectedloungeid)
        dispatcher.utter_message("Perfect, i booked for you the requested lounge")
       
        return [SlotSet("selectedlounge", selectedlounge)] 




class ShowDutyFreeArticles(Action):

    def name(self):
        return "action_show_dutyfree_articles"

    def run(self, dispatcher, tracker, domain):

        onAir_dutyFree_shopping = [
        {
            "id": 1,
            "photo": "https://imagizer.imageshack.com/img923/986/Bd9b1x.png",
            "article_name":"Givenchy L'Interdit",
            "information": "Eau de parfum, 80 ml",
            "article_category": "FOR WOMEN",
            "price_AED": "AED 375",
            "Price_USD": "$ 150"
        },

        {
            "id": 2,
            "photo": "https://imagizer.imageshack.com/img924/8041/i87oKf.png",
            "article_name":"Giorgio Armani Si Passione",
            "information": "Eau de parfum, 50 ml",
            "article_category": "FOR WOMEN",
            "price_AED": "AED 350",
            "Price_USD": "$ 96"
        },

        {
            "id": 3,
            "photo": "https://imagizer.imageshack.com/img921/1360/chk4fr.png",
            "article_name":"Narciso Rodriguez Narciso Rouge",
            "information": "Eau de parfum, 90 ml",
            "article_category": "FOR WOMEN",
            "price_AED": "AED 405",
            "Price_USD": "$ 112"
        },

        {
            "id": 4,
            "photo": "https://imagizer.imageshack.com/img924/1/aNotN1.png",
            "article_name":"Jo Melone London",
            "information": "Cologne, 2 x 30ml",
            "article_category": "FOR WOMEN",
            "price_AED": "AED 380",
            "Price_USD": "$ 105"
        }
        ]
        data={}
        data['type'] = "showdutyfreearticles"
        data['articles'] = onAir_dutyFree_shopping
        json_data = json.dumps(data)    
        
        dispatcher.utter_message("Here are some of the articles i found for you")
        dispatcher.utter_message("If you buy directly buy from the app, i will deliver it to your seat, and then you can pay on the plane")
        dispatcher.utter_attachment(json_data)


class BuyArticleAction(Action):

    def name(self):
        return "action_buy_article"

    def run(self, dispatcher, tracker, domain):
        lounges = [{"id": 1, "name": "Parfum"}, {"id": 2, "name": "Flowers"}]
        selectedloungeid = tracker.get_slot("selectedarticleid")
        print("selectedloungeid: ", selectedloungeid)
        selectedlounge = [flight for flight in lounges if flight['id']==selectedloungeid]
        print("selectedloungeid: ", selectedloungeid)
        dispatcher.utter_message("Perfect, the article will be delivered to your seat")
       
        #return [SlotSet("selectedarticle", selectedlounge)] 
     
     
     
class FlightSearchForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "flightsearch_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["destination", "departuredate", "flightclass"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"destination": self.from_entity(entity="destination",
                                            not_intent="chitchat"),
                "departuredate": [self.from_entity(entity="departuredate",
                                                intent=["inform",
                                                        "request_flightsearch"]),
                               self.from_entity(entity="date")],
                "flightclass": self.from_entity(entity="flightclass",
                                                intent=["inform",
                                                        "request_flightsearch"])               
               }

    @staticmethod
    def destinations_db():
        # type: () -> List[Text]
        """Database of supported destination"""
        return ["london",
                "toronto",
                "moscow",
                "paris",
                "new york",
                "tunis",
                "larnaca",
                "madrid",
                "barcelona"]

    @staticmethod
    def flightclass_db():
        # type: () -> List[Text]
        """Database of supported flightclass"""
        return ["economy",
                "business",
                "first"]            

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:
        """Validate extracted requested slot
            else reject the execution of the form action
        """
        # extract other slots that were not requested
        # but set by corresponding entity
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        # we'll check when validation failed in order
        # to add appropriate utterances
        for slot, value in slot_values.items():
            if slot == 'destination':
                if value.lower() not in self.destinations_db():
                    dispatcher.utter_template('utter_wrong_destination', tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None

            elif slot == 'flightclass':
                if value.lower() not in self.flightclass_db():
                    dispatcher.utter_template('utter_wrong_flightclass',
                                              tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None


        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template('utter_submit', tracker)
        return []
