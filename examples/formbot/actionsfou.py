# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union

import json

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
        destination = tracker.get_slot("destination")
        print("DESTINATION: ", destination)
        proposedFlights = [flight for flight in concerts if flight['destination'].lower()==destination.lower()]
        description = ", ".join([c["flightNumber"] for c in concerts])
        output_json = json.dumps(proposedFlights)
        print("PROPOSED FLIGHTS: ", output_json)
        dispatcher.utter_message("{}".format(description))
        return [SlotSet("flightoptions", output_json)]   

class BookFlightActions(Action):
    def name(self):
        return 'action_book_flight'

    def run(self, dispatcher, tracker, domain):
        concerts = [
            {"flightNumber": "EK 144", "destination": "London", "depatureDate": "2019-04-16T10:00:00.000Z"},
            {"flightNumber": "EK 145", "destination": "Toronto", "depatureDate": "2019-04-16T10:00:00.000Z"},
            {"flightNumber": "EK 146", "destination": "Frankfurt", "depatureDate": "2019-04-16T10:00:00.000Z"},
            {"flightNumber": "EK 147", "destination": "London", "depatureDate": "2019-04-17T10:00:00.000Z"}
        ]
        selectedflightnumber = tracker.get_slot("selectedflightnumber")
        print("selectedflightnumber: ", selectedflightnumber)
        proposedFlights = [flight for flight in concerts if flight['flightNumber'].lower()==selectedflightnumber.lower()]
        description = ", ".join([c["flightNumber"] for c in proposedFlights])
        output_json = json.dumps(proposedFlights)
        print("PROPOSED FLIGHTS: ", output_json)
        dispatcher.utter_message("{}".format(description))
        return [SlotSet("selectedflight", output_json)]         

class GetPassengerFlightDetails(Action):
    def name(self):
        return 'action_get_flight_details'

    def run(self, dispatcher, tracker, domain):

        destination = "London"
        flightclass = "Economy"
        passengername = "John"
        hourdelay = "7"
        
        description = " we called get passenger flight details "
        dispatcher.utter_message("{}".format(description))
        return [SlotSet("destination", destination), SlotSet("flightclass", flightclass), SlotSet("passengername", passengername),
    SlotSet("hourdelay", hourdelay)]    


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
