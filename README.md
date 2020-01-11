
Install
-------

    sudo  python setup.py install

First, copy **products.yaml** inventory file to your home directory.


Usage
-----

    * supermarket COMMAND [OPTIONS]
    * supermarket COMMAND --help
    * supermarket --help

The supermarket command provides way to list items in supermarket and
 interact with shopping cart checkout system.

	* Usage 1 runs command in text-only (CLI) mode.
	* Usage 2 gives help about specific cmds.
	* Usage 3 prints this general help message.

COMMAND is one of:
        
	cart
	display

Use Usage 2 for info about OPTIONS for each COMMAND.

The `cart` command further has 3 commands, 
    
    add
    remove
    checkout

Here is how to use it!

* To display the contents of your cart:
	`supermarket cart`

* To add items to cart:
	`supermarket cart -a 1 2 3`
	# where 1, 2, 3 are item codes you can see when you type `supermarket display`.

* To remove items previously selected:
	`supermarket cart -r 1 2 3`

* To Checkout your shopping cart:
	`supermarket cart -c`



