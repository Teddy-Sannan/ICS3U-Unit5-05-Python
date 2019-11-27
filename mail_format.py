#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: November 2019
# This program shows the volume of a cylinder


def mailing(name1, address1, city1, province1, postal_code1):
    print(name1)
    print(address1)
    print(city1, province1, postal_code1)


def main():
    while True:
        name = input("Enter the name of the reciever: ")
        address = input("Enter the address: ")
        city = input("Enter the city: ")
        province = input("Enter the province: ")
        postal_code = input("Enter the postal code: ")
        print()

        try:
            mailing(name, address, city, province, postal_code)
        except ValueError:
            print("Invalid Input")
            continue
        else:
            break


if __name__ == "__main__":
    main()
