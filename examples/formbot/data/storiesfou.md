## happy path rebook change destination flight and HOTEL
* start
    - action_get_flight_details
    - utter_welcomes_passenger
* change_destination{"destination":"destination"}
    - utter_inform_flightsearch
    - action_search_change_destination_flight
* select_flight{"selectedflightnumber":"EK 147"}
    - action_book_flight
* great
	- utter_askfurtherhelp
* ask_baggage
	- utter_baggage
* great
	- utter_askfurtherhelp
* ask_hotel
    - action_search_hotel
* select_hotel{"selectedrhotelid":"1"}
    - action_book_hotel
* thankyou
    - utter_noworries

## happy path rebook upgrade flight
* start
    - action_get_flight_details
    - utter_welcomes_passenger
    - utter_inform_delay
* upgrade
    - action_search_upgrade_flight
* thankyou
    - utter_noworries
    - utter_askfurtherhelp
* ask_restaurant
    - action_search_restaurant
* select_restaurant{"selectedrestaurantid":"2"}
    - action_book_restaurant
* great
	- utter_askfurtherhelp
* thankyou
    - utter_noworries

## login
* select_login{"username": "fouad", "password": "admin"}
    - action_login

## get delayed flights
* ask_delayed_flights
    - action_get_delayed_flights

## give vouchers to passengers
* give_voucher{"pnr":"XKDFL5", "passenger_id":"1", "voucher_type":"HOTEL"}
    - action_give_voucher

## change language 
* change_language
    - action_change_language

## show passenger lounge
* show_lounge
    - action_show_lounge
    - action_listen

## show passenger lounge again
* show_lounge
    - action_show_lounge
    - action_listen
* show_lounge
    - action_show_lounge
    - action_listen

## show me articles on aid duty free
* show_onair_shopping_article
    - action_show_dutyfree_articles
    - action_listen

## show me articles on aid duty free again
* show_onair_shopping_article
    - action_show_dutyfree_articles
    - action_listen
* show_onair_shopping_article
    - action_show_dutyfree_articles
    - action_listen    

## show me my voucher
* myvoucher
    - action_show_voucher
    - action_listen

## show me my voucher again
* myvoucher
    - action_show_voucher
    - action_listen
* myvoucher
    - action_show_voucher
    - action_listen    

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

## Generated Story 4548957576817830631
* ask_restaurant
    - action_search_restaurant
    - slot{"restaurantoptions": [{"Reservation": "Sun, Apr 21, 2 people", "address": "Concourse B,Terminal 3,Dubai International Airport - Dubai", "cuisine": "French", "cuisine_restaurant": "French restaurant", "id": "1", "name": "Paul", "open_time": {"Friday": "24 hours open", "Monday": "24 hours open", "Saturday": "24 hours open", "Sunday": "24 hours open", "Thursday": "24 hours open", "Tuesday": "24 hours open", "Wednesday": "24 hours open"}, "photoCount": 3, "photos": [{"url": "https://doc-0k-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/ub92u1vofsvsou59ri3mbm5gq3jfckkk/1555725600000/11429114590258316664/*/1Khq6ncv3CRwW1B2bHPEoSUG-oS5a7OPZ"}, {"url": "https://doc-0s-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/dcruvqc2ttls5e4i2r91t8ib2q3h5adt/1555725600000/11429114590258316664/*/117xov5OqO8AclNi5BOcguAPy6XRjDTEO"}, {"url": "https://doc-0o-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/po701g4t0mkiesg0ip287gsslephi4ee/1555725600000/11429114590258316664/*/1h3Aqx1Ja1-EoSldvHejhMXstTnCWkdWP"}], "stars": 4}, {"Reservation": "Sun, Apr 21, 2 people", "address": "Gate 25, Terminal 3 - Dubai International Airport Concourse B - Dubai", "cuisine": "French", "cuisine_restaurant": "American restaurant", "id": "2", "name": "Hard Rock Cafe", "open_time": {"Friday": "24 hours open", "Monday": "24 hours open", "Saturday": "24 hours open", "Sunday": "24 hours open", "Thursday": "24 hours open", "Tuesday": "24 hours open", "Wednesday": "24 hours open"}, "photoCount": 3, "photos": [{"url": "https://doc-04-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/a76ujr439avju72a6s7mqm59jaujljj3/1555725600000/11429114590258316664/*/1CEdYSP_Q5LO8wgjcYHvpV0EVVkU6B7eC"}, {"url": "https://doc-0o-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/v0uudi4johan6fg37s0qjjobct8cnfau/1555725600000/11429114590258316664/*/1APP8Qz5lwgO6-ZIUgTmIcY0qBnpMsJ2x"}, {"url": "https://doc-08-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/47cfrnu2pghv96i7dpjr40hs7fpenhpo/1555725600000/11429114590258316664/*/1-NXaVrNAH-KMn5QffbDvTtNiYrXfhsTt"}], "stars": 4}]}
* select_restaurant{"selectedrestaurantid": "1"}
    - slot{"selectedrestaurantid": "1"}
    - action_book_restaurant
* ask_hotel
    - action_search_hotel
    - slot{"hoteloptions": [{"Stay": "Sun, Apr 21, 2 poeple", "address": "International Dubai Airport - Terminal 3, Concource A, opposite Gate A1 - Dubai", "facilities": ["Air conditioning", "Wake-up service", "Linens", "Entire unit located on ground floor"], "hotel_description": "Conveniently located opposite Gate A1 at A-Gate (Terminal 3, inside the DXB transit area), the Sleep'n fly Sleep Lounge is inspired by Scandinavian design for comfort, style ans necessity", "id": 1, "name": "Sleep n'fly by yarn, sleep lounge", "numberAdults": "1 Adult", "numberRoom": "1 Room", "photoCount": 3, "photos": [{"url": "https://doc-0c-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/g147qncu7q1284crr8kf0vkt6denjedn/1555725600000/11429114590258316664/*/1BqkIOov9jj-DcrDWwvTraArcpEzWnaum"}, {"url": "https://doc-0g-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/shqqoravt2af12m54bo8s888ni9kl9pp/1555718400000/11429114590258316664/*/1ahEIMoocW79gu1Tgnit6ibhkCikAHy5Q"}, {"url": "https://doc-14-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/9iftr05026at0pmhrqvo3vlelojnbc7s/1555718400000/11429114590258316664/*/1FieFZPRmRm-oLKozCr4ZHkU-CqFSDk3F"}], "price": "AED 348,00 /per Traveller", "room": "One Room", "room_description": "One Bedroom", "stars": 4, "stay_duration": "Apr 21 - Apr 21, 1 night"}, {"Stay": "Sun, Apr 21, 2 poeple", "address": "International Dubai Airport - Terminal 3, Concource A, opposite Gate A1 - Dubai", "facilities": ["Air conditioning", "Wake-up service", "Linens", "Entire unit located on ground floor"], "hotel_description": "Conveniently located opposite Gate A1 at A-Gate (Terminal 3, inside the DXB transit area), the Sleep'n fly Sleep Lounge is inspired by Scandinavian design for comfort, style ans necessity", "id": 2, "name": "Le meridien", "numberAdults": "1 Adult", "numberRoom": "1 Room", "photoCount": 3, "photos": [{"url": "https://doc-0c-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/g147qncu7q1284crr8kf0vkt6denjedn/1555725600000/11429114590258316664/*/1BqkIOov9jj-DcrDWwvTraArcpEzWnaum"}, {"url": "https://doc-0g-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/shqqoravt2af12m54bo8s888ni9kl9pp/1555718400000/11429114590258316664/*/1ahEIMoocW79gu1Tgnit6ibhkCikAHy5Q"}, {"url": "https://doc-14-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/9iftr05026at0pmhrqvo3vlelojnbc7s/1555718400000/11429114590258316664/*/1FieFZPRmRm-oLKozCr4ZHkU-CqFSDk3F"}], "price": "AED 348,00 /per Traveller", "room": "One Room", "room_description": "One Bedroom", "stars": 4, "stay_duration": "Apr 21 - Apr 21, 1 night"}]}
* select_hotel{"selectedhotelid": "1"}
    - slot{"selectedhotelid": "1"}
    - action_book_hotel
    - slot{"hoteloptions": [{"Stay": "Sun, Apr 21, 2 poeple", "address": "International Dubai Airport - Terminal 3, Concource A, opposite Gate A1 - Dubai", "facilities": ["Air conditioning", "Wake-up service", "Linens", "Entire unit located on ground floor"], "hotel_description": "Conveniently located opposite Gate A1 at A-Gate (Terminal 3, inside the DXB transit area), the Sleep'n fly Sleep Lounge is inspired by Scandinavian design for comfort, style ans necessity", "id": "1", "name": "Sleep n'fly by yarn, sleep lounge", "numberAdults": "1 Adult", "numberRoom": "1 Room", "photoCount": 3, "photos": [{"url": "https://doc-0c-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/g147qncu7q1284crr8kf0vkt6denjedn/1555725600000/11429114590258316664/*/1BqkIOov9jj-DcrDWwvTraArcpEzWnaum"}, {"url": "https://doc-0g-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/shqqoravt2af12m54bo8s888ni9kl9pp/1555718400000/11429114590258316664/*/1ahEIMoocW79gu1Tgnit6ibhkCikAHy5Q"}, {"url": "https://doc-14-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/9iftr05026at0pmhrqvo3vlelojnbc7s/1555718400000/11429114590258316664/*/1FieFZPRmRm-oLKozCr4ZHkU-CqFSDk3F"}], "price": "AED 348,00 /per Traveller", "room": "One Room", "room_description": "One Bedroom", "stars": 4, "stay_duration": "Apr 21 - Apr 21, 1 night"}]}

## Generated Story -1327116923689532971
* ask_delayed_flights
    - action_get_delayed_flights
    - slot{"delayedflights": "{\"type\": \"delayedflights\", \"delayedflights\": [{\"flightNumber\": \"EK 145\", \"flightDelayedPassengers\": [{\"id\": 1, \"number\": \"XKDFK2\", \"birthday\": \"04.04.1981\", \"accompaniedPassengers\": 0, \"statusMiles\": \"30,000\", \"flightSegments\": \"7\", \"eVouchers\": \"2\", \"hasHotel\": true, \"hasMeal\": false}, {\"id\": 2, \"number\": \"XKDFK1\", \"birthday\": \"04.04.1982\", \"accompaniedPassengers\": 0, \"statusMiles\": \"60,000\", \"flightSegments\": \"2\", \"eVouchers\": \"0\", \"hasHotel\": false, \"hasMeal\": true}]}, {\"flightNumber\": \"EK 147\", \"flightDelayedPassengers\": [{\"id\": 1, \"number\": \"XKDFL5\", \"birthday\": \"04.04.1981\", \"accompaniedPassengers\": 0, \"statusMiles\": \"10,000\", \"flightSegments\": \"7\", \"eVouchers\": \"2\", \"hasHotel\": true, \"hasMeal\": false}, {\"id\": 2, \"number\": \"XKDFL6\", \"birthday\": \"04.04.1982\", \"accompaniedPassengers\": 0, \"statusMiles\": \"5,000\", \"flightSegments\": \"2\", \"eVouchers\": \"0\", \"hasHotel\": false, \"hasMeal\": true}]}]}"}
* ask_delayed_flights
    - action_get_delayed_flights
    - slot{"delayedflights": "{\"type\": \"delayedflights\", \"delayedflights\": [{\"flightNumber\": \"EK 145\", \"flightDelayedPassengers\": [{\"id\": 1, \"number\": \"XKDFK2\", \"birthday\": \"04.04.1981\", \"accompaniedPassengers\": 0, \"statusMiles\": \"30,000\", \"flightSegments\": \"7\", \"eVouchers\": \"2\", \"hasHotel\": true, \"hasMeal\": false}, {\"id\": 2, \"number\": \"XKDFK1\", \"birthday\": \"04.04.1982\", \"accompaniedPassengers\": 0, \"statusMiles\": \"60,000\", \"flightSegments\": \"2\", \"eVouchers\": \"0\", \"hasHotel\": false, \"hasMeal\": true}]}, {\"flightNumber\": \"EK 147\", \"flightDelayedPassengers\": [{\"id\": 1, \"number\": \"XKDFL5\", \"birthday\": \"04.04.1981\", \"accompaniedPassengers\": 0, \"statusMiles\": \"10,000\", \"flightSegments\": \"7\", \"eVouchers\": \"2\", \"hasHotel\": true, \"hasMeal\": false}, {\"id\": 2, \"number\": \"XKDFL6\", \"birthday\": \"04.04.1982\", \"accompaniedPassengers\": 0, \"statusMiles\": \"5,000\", \"flightSegments\": \"2\", \"eVouchers\": \"0\", \"hasHotel\": false, \"hasMeal\": true}]}]}"}
* ask_delayed_flights
    - action_get_delayed_flights
    - slot{"delayedflights": "{\"type\": \"delayedflights\", \"delayedflights\": [{\"flightNumber\": \"EK 145\", \"flightDelayedPassengers\": [{\"id\": 1, \"number\": \"XKDFK2\", \"birthday\": \"04.04.1981\", \"accompaniedPassengers\": 0, \"statusMiles\": \"30,000\", \"flightSegments\": \"7\", \"eVouchers\": \"2\", \"hasHotel\": true, \"hasMeal\": false}, {\"id\": 2, \"number\": \"XKDFK1\", \"birthday\": \"04.04.1982\", \"accompaniedPassengers\": 0, \"statusMiles\": \"60,000\", \"flightSegments\": \"2\", \"eVouchers\": \"0\", \"hasHotel\": false, \"hasMeal\": true}]}, {\"flightNumber\": \"EK 147\", \"flightDelayedPassengers\": [{\"id\": 1, \"number\": \"XKDFL5\", \"birthday\": \"04.04.1981\", \"accompaniedPassengers\": 0, \"statusMiles\": \"10,000\", \"flightSegments\": \"7\", \"eVouchers\": \"2\", \"hasHotel\": true, \"hasMeal\": false}, {\"id\": 2, \"number\": \"XKDFL6\", \"birthday\": \"04.04.1982\", \"accompaniedPassengers\": 0, \"statusMiles\": \"5,000\", \"flightSegments\": \"2\", \"eVouchers\": \"0\", \"hasHotel\": false, \"hasMeal\": true}]}]}"}
* ask_delayed_flights
    - action_get_delayed_flights
    - slot{"delayedflights": "{\"type\": \"delayedflights\", \"delayedflights\": [{\"flightNumber\": \"EK 145\", \"flightDelayedPassengers\": [{\"id\": 1, \"number\": \"XKDFK2\", \"birthday\": \"04.04.1981\", \"accompaniedPassengers\": 0, \"statusMiles\": \"30,000\", \"flightSegments\": \"7\", \"eVouchers\": \"2\", \"hasHotel\": true, \"hasMeal\": false}, {\"id\": 2, \"number\": \"XKDFK1\", \"birthday\": \"04.04.1982\", \"accompaniedPassengers\": 0, \"statusMiles\": \"60,000\", \"flightSegments\": \"2\", \"eVouchers\": \"0\", \"hasHotel\": false, \"hasMeal\": true}]}, {\"flightNumber\": \"EK 147\", \"flightDelayedPassengers\": [{\"id\": 1, \"number\": \"XKDFL5\", \"birthday\": \"04.04.1981\", \"accompaniedPassengers\": 0, \"statusMiles\": \"10,000\", \"flightSegments\": \"7\", \"eVouchers\": \"2\", \"hasHotel\": true, \"hasMeal\": false}, {\"id\": 2, \"number\": \"XKDFL6\", \"birthday\": \"04.04.1982\", \"accompaniedPassengers\": 0, \"statusMiles\": \"5,000\", \"flightSegments\": \"2\", \"eVouchers\": \"0\", \"hasHotel\": false, \"hasMeal\": true}]}]}"}

## Generated Story -6511269173217550078
* ask_delayed_flights
    - action_get_flight_details
    - slot{"destination": "London"}
    - slot{"flightclass": "Economy"}
    - slot{"passengername": "John"}
    - slot{"hourdelay": "7"}
    - slot{"headcount": "2"}

