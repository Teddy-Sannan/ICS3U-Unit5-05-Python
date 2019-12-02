#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: November 2019
# This program shows letter formatting


def letter(name, address, city, province, postal_code, apartment_number=None):
    # formats letter
    if apartment_number is not None:
        letter = "{0} \n{1} {2} \n{3} {4} {5}".format(name, apartment_number,
                                                      address, city,
                                                      province,
                                                      postal_code)

    letter = "{0} \n{1} \n{2} {3} {4}".format(name, address, city, province,
                                              postal_code)

    return letter


def main():
    # calls other functions
    while True:

        name = input("Enter your full name: ")
        apartment = input("Do you live in an apartment?(y/n): ")
        if apartment.upper() == "Y" or apartment.upper() == "YES":
            apartment_number = input("What is your apartment number: ")
        address = input("Enter your adress: ")
        city = input("Enter your city: ")
        province = input("Enter your province or territory \
(short form): ")
        postal_code = input("Enter your postal code: ")

        if apartment == "y":
            card = letter(name=name, address=address, city=city,
                          province=province, postal_code=postal_code,
                          apartment_number=apartment_number)

        else:
            card = letter(name=name, address=address, city=city,
                          province=province, postal_code=postal_code)
        print("")
        print(card)
        break


if __name__ == "__main__":
    main()
