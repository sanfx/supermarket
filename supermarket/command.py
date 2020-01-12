# -*- coding: utf-8 -*-
"""This module represents the view of supermarket and shopping
cart checkout system.
"""

import argparse
import sys

# Local imports
from controller import print_receipts, read_user_cart_file
from constants import EPILOG, DESC
from inventory_utils import get_products
from model import ShoppingCart


class Supermarket(object):
    """Supermarket class containing methods that act as sub commands."""

    def __init__(self):
        """Constructor to initialize user interface."""
        super(Supermarket, self).__init__()
        self._products = get_products()
        self._parser = argparse.ArgumentParser(
            description=DESC,
            usage=self._epilog())
        self._parser.add_argument('command', help='Sub command to run')
        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = self._parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print 'Unrecognized command !'
            self._parser.print_help()
            exit(1)

        self._cart = ShoppingCart()
        self._cart_items = {}
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()

    def _epilog(self):
        """Help message."""
        return EPILOG.format(
            "\n\t".join([cmd for cmd in dir(self) if not cmd.startswith("_")])
            )

    def cart(self):
        """Command provide a sub commands to interact with shopping cart."""
        if len(sys.argv) == 2:
            self._cart.list()
        else:
            parser = argparse.ArgumentParser(
                description="Interact with shopping cart."
                )
            parser.add_argument(
                "-a", 
                "--add", 
                nargs="+",
                help="Enter the item code separated by space."
                )
            parser.add_argument(
                "-r",
                "--remove",
                nargs="+",
                help="Enter the item code separated by space."
                )
            parser.add_argument(
                "-c",
                "--checkout",
                action="store_true",
                help="Checkout from cart."
                )
            args = parser.parse_args(sys.argv[2:])
            if args.add:
                user_entered_codes = [int(item) for item in args.add]
                not_found = []
                for code in user_entered_codes:
                    if code not in self._products:
                        not_found.append(code)

                if not_found:
                    print "Items with following code not found: {}".format(not_found)

                if user_entered_codes:
                    print "Below listed items added to cart:"
                    line = "+" * 28
                    print line
                    for itemcode, value in self._products.iteritems():
                        if itemcode in user_entered_codes:
                            value.update({"itemcode": itemcode})
                            print "*", value["name"].capitalize(), value["type"] 
                            "\xa3{}".format(value["cost"])
                            self._cart_items[itemcode] = value
                    print line
                    if self._cart_items:
                        self._cart.add(self._cart_items)

            if args.remove:
                self._cart.remove([int(item) for item in args.remove])

            if args.checkout:
                checkout_items = self._cart.checkout()
                print_receipts(checkout_items)
                self._cart.remove(
                    [i["itemcode"] for i in read_user_cart_file()], 
                    verbose=False
                    )

    def display(self):
        """Displays the products in the supermarket."""
        print "Welcome to Wilko Supermarket ! "
        display_shelf = {}

        for code, product in self._products.iteritems():
            _type = product["type"] 
            product.update({"itemcode": code})
            if _type not in display_shelf:
                display_shelf[_type] = [product]
            else:
                display_shelf[_type].append(product)

        for product_type, products in display_shelf.iteritems():
            line = "-" * (len(product_type) + 22)
            print line
            print "|code\t{type}s\t Price|".format(type=product_type.capitalize())
            print line
            for product in products:
                print u"{}\t{}\t\xa3{}".format(
                    product["itemcode"], 
                    product["name"], 
                    product["cost"]
                    )



def main():
    # Initialize user interfacing class
    Supermarket()
