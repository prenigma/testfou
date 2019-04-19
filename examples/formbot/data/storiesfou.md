## happy path rebook delayed flight
* start
    - action_get_flight_details
    - utter_welcomes_passenger
	- utter_inform_delay
* feedback_negativ
	- utter_inform_flightsearch
	- utter_inform_pricefreeofcharge
	- action_search_flight
* select_flight{"selectedflightnumber":"EK 147"}
    - action_book_flight
* great
	- utter_askfurtherhelp
* ask_baggage
	- utter_baggage
* thankyou
    - utter_noworries

## happy path
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
    - form{"name": null}
    - action_search_flight
    - utter_slots_values
    
* thankyou
    - utter_noworries
## happy path starting with inform
* inform
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
    - form{"name": null}
    - action_search_flight
    - utter_slots_values
    
* thankyou
    - utter_noworries
## unhappy path
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
* chitchat
    - utter_chitchat
    - flightsearch_form
    - form{"name": null}
    - action_search_flight
    - utter_slots_values
* thankyou
    - utter_noworries

## unhappy path with inform starting
* inform
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
* chitchat
    - utter_chitchat
    - flightsearch_form
    - form{"name": null}
    - action_search_flight
    - utter_slots_values
* thankyou
    - utter_noworries    

## very unhappy path
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
* chitchat
    - utter_chitchat
    - flightsearch_form
* chitchat
    - utter_chitchat
    - flightsearch_form
* chitchat
    - utter_chitchat
    - flightsearch_form
    - form{"name": null}
    - action_search_flight
    - utter_slots_values
* thankyou
    - utter_noworries


## very unhappy path with inform starting
* inform
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
* chitchat
    - utter_chitchat
    - flightsearch_form
* chitchat
    - utter_chitchat
    - flightsearch_form
* chitchat
    - utter_chitchat
    - flightsearch_form
    - form{"name": null}
    - action_search_flight
    - utter_slots_values
* thankyou
    - utter_noworries

## stop but continue path
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
* stop
    - utter_ask_continue
* affirm
    - flightsearch_form
    - form{"name": null}
    - action_search_flight
    - utter_slots_values
* thankyou
    - utter_noworries

## stop and really stop path
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}

## chitchat stop but continue path
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
* chitchat
    - utter_chitchat
    - flightsearch_form
* stop
    - utter_ask_continue
* affirm
    - flightsearch_form
    - form{"name": null}
    - action_search_flight
    - utter_slots_values
* thankyou
    - utter_noworries

## stop but continue and chitchat path
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
* stop
    - utter_ask_continue
* affirm
    - flightsearch_form
* chitchat
    - utter_chitchat
    - flightsearch_form
    - form{"name": null}
    - action_search_flight
    - utter_slots_values
* thankyou
    - utter_noworries

## chitchat stop but continue and chitchat path
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
* chitchat
    - utter_chitchat
    - flightsearch_form
* stop
    - utter_ask_continue
* affirm
    - flightsearch_form
* chitchat
    - utter_chitchat
    - flightsearch_form
    - form{"name": null}
    - action_search_flight
    - utter_slots_values
* thankyou
    - utter_noworries

## chitchat, stop and really stop path
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
* chitchat
    - utter_chitchat
    - flightsearch_form
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
## Generated Story -4750950639521846139
* request_flightsearch
    - flightsearch_form
    - form{"name": "flightsearch_form"}
    - slot{"requested_slot": "destination"}
* form: inform{"destination": "london"}
    - form: flightsearch_form
    - slot{"destination": "london"}
    - slot{"requested_slot": "departuredate"}
* form: inform{"departuredate": "tomorrow"}
    - form: flightsearch_form
    - slot{"departuredate": "tomorrow"}
    - slot{"requested_slot": "flightclass"}
* form: inform{"flightclass": "business"}
    - form: flightsearch_form
    - slot{"flightclass": "business"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_continue

## Generated Story 7580058393619038318
* request_flightsearch{"departuredate": "tomorrow", "destination": "Moscow", "flightclass": "business"}
    - flightsearch_form
    - form{"name": "flightsearch_form"}
    - slot{"destination": "Moscow"}
    - slot{"departuredate": "tomorrow"}
    - slot{"flightclass": "business"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_flight
    - utter_slots_values

## Generated Story -2437810962546508059
* request_flightsearch{"destination": "paris", "flightclass": "economy", "departuredate": "next monday"}
    - flightsearch_form
    - form{"name": "flightsearch_form"}
    - slot{"destination": "paris"}
    - slot{"departuredate": "next monday"}
    - slot{"flightclass": "economy"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_flight
    - utter_return_proposed_flights

## Generated Story 3905010269921189340
* request_flightsearch{"departuredate": "tomorrow", "destination": "paris", "flightclass": "business"}
    - flightsearch_form
    - form{"name": "flightsearch_form"}
    - slot{"destination": "paris"}
    - slot{"departuredate": "tomorrow"}
    - slot{"flightclass": "business"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_flight
    - utter_return_proposed_flights
    - utter_slots_values
* request_flightsearch{"destination": "toronto", "departuredate": "saturday", "flightclass": "first"}
    - flightsearch_form
    - form{"name": "flightsearch_form"}
    - slot{"destination": "toronto"}
    - slot{"departuredate": "saturday"}
    - slot{"flightclass": "first"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_flight
    - utter_return_proposed_flights
* request_flightsearch{"departuredate": "today", "destination": "london", "flightclass": "business"}
    - flightsearch_form
    - form{"name": "flightsearch_form"}
    - slot{"destination": "london"}
    - slot{"departuredate": "today"}
    - slot{"flightclass": "business"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_flight
    - utter_return_proposed_flights

## Generated Story 5528514219437258813
* request_flightsearch{"departuredate": "tomorrow", "destination": "london", "flightclass": "economy"}
    - flightsearch_form
    - form{"name": "flightsearch_form"}
    - slot{"destination": "london"}
    - slot{"departuredate": "tomorrow"}
    - slot{"flightclass": "economy"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_flight
    - utter_return_proposed_flights

## Generated Story 7965771063100883480
* request_flightsearch{"departuredate": "tomorrow", "destination": "london", "flightclass": "economy"}
    - flightsearch_form
    - form{"name": "flightsearch_form"}
    - slot{"destination": "london"}
    - slot{"departuredate": "tomorrow"}
    - slot{"flightclass": "economy"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_flight
    - slot{"flightoptions": "[{\"flightNumber\": \"EK 144\", \"destination\": \"London\", \"depatureDate\": \"2019-04-16T10:00:00.000Z\"}, {\"flightNumber\": \"EK 147\", \"destination\": \"London\", \"depatureDate\": \"2019-04-17T10:00:00.000Z\"}]"}

## Generated Story -5878234090979552501
* start
    - action_get_flight_details
    - utter_welcomes_passenger
    - utter_inform_delay
* feedback_negativ
    - utter_inform_flightsearch
    - utter_inform_pricefreeofcharge
    - action_search_flight
* select_flight{"selectedflightnumber":"EK 147"}
    - action_book_flight
* great
    - utter_askfurtherhelp
* ask_baggage
    - utter_baggage
* thankyou
    - utter_noworries
    - utter_noworries

## Generated Story 9061664769805808833
* start
    - action_get_flight_details
    - utter_welcomes_passenger
    - utter_inform_delay
* feedback_negativ
    - utter_inform_flightsearch
    - utter_inform_pricefreeofcharge
    - action_search_flight
* select_flight{"selectedflightnumber":"EK 147"}
    - action_book_flight
* great
    - utter_askfurtherhelp
* ask_baggage
    - utter_baggage
* thankyou
    - utter_noworries

## Generated Story 4762444670612914425
* start
    - action_get_flight_details
    - utter_welcomes_passenger
    - utter_inform_delay
* feedback_negativ
    - utter_inform_flightsearch
    - utter_inform_pricefreeofcharge
    - action_search_flight
* select_flight{"selectedflightnumber":"EK 147"}
    - action_book_flight
* great
    - utter_askfurtherhelp
* ask_baggage
    - utter_baggage
* thankyou
    - utter_noworries

## Generated Story -6638156372600576819
* start
    - action_get_flight_details
    - utter_welcomes_passenger
    - utter_inform_delay
* feedback_negativ
    - utter_inform_flightsearch
    - utter_inform_pricefreeofcharge
    - action_search_flight
* select_flight{"selectedflightnumber":"EK 147"}
    - action_book_flight
* ask_baggage
    - utter_baggage
* thankyou
    - utter_noworries

## Generated Story 856459988357202731
* start
    - action_get_flight_details
    - slot{"destination": "London"}
    - slot{"flightclass": "Economy"}
    - slot{"passengername": "John"}
    - slot{"hourdelay": "7"}
    - utter_welcomes_passenger
    - utter_inform_delay
* feedback_negativ
    - utter_inform_flightsearch
    - utter_inform_pricefreeofcharge
    - action_search_flight
    - slot{"flightoptions": "[{\"flightNumber\": \"EK 144\", \"destination\": \"London\", \"depatureDate\": \"2019-04-16T10:00:00.000Z\"}, {\"flightNumber\": \"EK 147\", \"destination\": \"London\", \"depatureDate\": \"2019-04-17T10:00:00.000Z\"}]"}
* select_flight{"selectedflightnumber":"EK 147"}
    - action_book_flight
* great
    - utter_askfurtherhelp
* ask_baggage
    - utter_baggage
* thankyou
    - utter_noworries

## Generated Story 3860683669444366323
* start
    - action_get_flight_details
    - slot{"destination": "London"}
    - slot{"flightclass": "Economy"}
    - slot{"passengername": "John"}
    - slot{"hourdelay": "7"}
    - utter_welcomes_passenger
    - utter_inform_delay
* feedback_negativ
    - utter_inform_flightsearch
    - utter_inform_pricefreeofcharge
    - action_search_flight
    - slot{"flightoptions": "[{\"flightNumber\": \"EK 144\", \"destination\": \"London\", \"depatureDate\": \"2019-04-16T10:00:00.000Z\"}, {\"flightNumber\": \"EK 147\", \"destination\": \"London\", \"depatureDate\": \"2019-04-17T10:00:00.000Z\"}]"}
* select_flight{"selectedflightnumber":"EK 147"}
    - action_book_flight
* great
    - utter_askfurtherhelp
* ask_baggage
    - utter_baggage
* thankyou
    - utter_noworries

## Generated Story -8126855454972832583
* start
    - action_get_flight_details
    - slot{"destination": "London"}
    - slot{"flightclass": "Economy"}
    - slot{"passengername": "John"}
    - slot{"hourdelay": "7"}
    - utter_welcomes_passenger
    - utter_inform_delay
* feedback_negativ
    - utter_inform_flightsearch
    - utter_inform_pricefreeofcharge
    - action_search_flight
    - slot{"flightoptions": "[{\"flightNumber\": \"EK 144\", \"destination\": \"London\", \"depatureDate\": \"2019-04-16T10:00:00.000Z\"}, {\"flightNumber\": \"EK 147\", \"destination\": \"London\", \"depatureDate\": \"2019-04-17T10:00:00.000Z\"}]"}
* select_flight{"selectedflightnumber":"EK 147"}
    - action_book_flight
* great
    - utter_askfurtherhelp
* ask_baggage
    - utter_baggage
* thankyou
    - utter_noworries

