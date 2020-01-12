
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

`$ supermarket cart --help`

	usage: supermarket [-h] [-a ADD [ADD ...]] [-r REMOVE [REMOVE ...]] [-c]

	Interact with shopping cart.

	optional arguments:
	  -h, --help            show this help message and exit
	  -a ADD [ADD ...], --add ADD [ADD ...]
	                        Enter the item code separated by space.
	  -r REMOVE [REMOVE ...], --remove REMOVE [REMOVE ...]
	                        Enter the item code separated by space.
	  -c, --checkout        Checkout from cart.

Here is how to use it!

* To display the contents of your cart:
	`supermarket cart`

* To add items to cart:
	`supermarket cart -a 1 2 3`

	where 1, 2, 3 are item codes you can see when you type `supermarket display`.

* To remove items previously selected:
	`supermarket cart -r 1 2 3`

* To Checkout your shopping cart:
	`supermarket cart -c`



