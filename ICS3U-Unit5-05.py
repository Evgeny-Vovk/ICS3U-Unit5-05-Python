# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: December 2022
# ICS3U-Unit5-05.py File, learning functions with parameters in python.

import math


def mail_address(full_name, street_number, street_name, city, province, postal_code, apartment_number = None):

    address = full_name + "\n"
    if apartment_number:
        address += apartment_number + "-"
    address += street_number + " " + street_name + "\n" + city + " " + province + " " + postal_code
    return address.upper()


def main():

    apartment_number = None

    full_name = input("Enter your full name: ")
    question = input("Do you live in an apartment? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apartment_number = input("Enter your apartment number: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter your street name and type (Main St, Express pkwy...): ")
    city = input("Enter your city: ")
    province = input("Enter your province (as an abbreviation, ex: ON, BC...): ")
    postal_code = input("Enter your postal code (123 456): ")
    print("")
    try:
        if apartment_number:
            apartment_number_int = int(apartment_number)
        street_number_int = int(street_number)

        address = mail_address(full_name, street_number, street_name, city, province, postal_code, apartment_number)

        print(address)

    except ValueError:
        print("Invalid input, please try again.")
    print("\n\nDone.")


if __name__ == "__main__":
    main()
