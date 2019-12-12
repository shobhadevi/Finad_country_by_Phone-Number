from phonenumbers import geocoder
from phonenumbers import carrier
import phonenumbers
# Code to find country
ch_number=phonenumbers.parse("+2349072266969","CH")
print("Country :")
print(geocoder.description_for_number(ch_number,"en"))

# Code to find sim
ro_number=phonenumbers.parse("+2349072266969","RO")
print("Company :")
print(carrier.name_for_number(ro_number,"en"))