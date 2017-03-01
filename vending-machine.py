#!/usr/bin/python

"""
    Author: Gianluca Biccari

    Problem:
    Implement a vending machine with the following requirements:
    - This vending machine must take user inputs (i.e. A1, A2, B1..etc) and dispenses an item after users input money.
    - There are only 9 inputs.
    - Assume that there are different kinds of items in the vending machine (Sprite, cheetos, etc).
    - The vending machine must store instances of items to be dispensed, the item can't be created at the moment someone requests it.

    Assumptions:
    - input goes from 1 to 9 like a numeric keyboards, selection of
      a single product per button. No numeri combinations allowed.
    - items sold are 9, mapped one to one to the button pushed. The prices have
      min incremental value of a quarters (i.e. $2, $4.50, $2.25)
    - the vending machine accepts only $1 bills and $5 and give changes.
    - the machine comes with backdoor code for reporting and shutdown.
 """

class Item(object):
    """
        Item sold by the vendor machine
    """
    def __init__(self, code, name, price):
		self.price = price
		self.code = code
		self.name = name


class Register(object):
    """
		Register for cash flow in the vending machine
	"""
    def __init__(self):
		# a balance for the $1 bills inserted, machine takes only $1 bill
		self._balance = 0
		# a balance of the quarters available for change
		self._quarters = 10

    def add_money(self, amount):
		self._balance += amount

    def refill_quarters(self, amount):
		self._quarters = amount

    def withdraw_balance(self):
        v = self._balance
        self._balance = 0
        return v

    def available_change(self):
		return self._quarters

    def give_change(self, rest):
        if rest > 0:
            to_give = min(self._quarters, rest)
            print 'Here is your change: ${}'.format(to_give)
            self._quarters = self._quarters - to_give
            if self._quarters <= 0:
                self._quarters = 0

    def report(self):
        print '**Register status'
        print 'Register available balance: ${}'.format(self._balance)
        print 'Register available change: ${}'.format(self._quarters)

class Inventory(object):
    def __init__(self):
        self._items = {}
        self._quantity = {}

    def add(self, item):
        code = item.code
        if self._items.has_key(code):
            self._quantity[code] += 1
        else:
            self._items[code] = item
            self._quantity[code] = 1

    def remove(self, item):
        code = item.code
        if self._quantity.has_key(code):
            self._quantity[code] -= 1
            if self._quantity[code] <= 0:
                del self._items[code]
                del self._quantity[code]

    def get(self, code):
        # return tuple (item, quantity)
        if self._items.has_key(code):
            return (self._items[code], self._quantity[code])

    def available_items(self):
        # returns list of item codes
        return self._items.values()

    def available_codes(self):
        # returns list of item codes available
        return self._items.keys()

    def report(self):
        print '**Inventory status'
        for item in self.available_items():
            print '{:9} : quantity: {}, price: ${}'.format(item.name, self._quantity[item.code], item.price)



class Machine(object):
    """
        The code of each item sold by the machine is mapped 1:1 to the key input,
        the code is used also as a key to keep the inventory.
    """

    def __init__(self):
        self._register = Register()
        self._inventory = Inventory()
        self._init_items()
        # Backdoor code access (example of two)
        self._CODE_SHUTDOWN = 100000
        self._CODE_REPORT_STATUS = 100001

    def _init_items(self):
        item1 = Item(1, "Coke", 2)
        self._refill_item(item1, 2)
        item2 = Item(2, "Fanta", 1.50)
        self._refill_item(item2, 4)
        item3 = Item(3, "Sprite", 2)
        self._refill_item(item3, 1)
        item4 = Item(4, "Water", 3.50)
        self._refill_item(item4, 1)
        item5 = Item(5, "Ice Tea", 2)
        self._refill_item(item5, 10)
        item6 = Item(6, "Chips", 1.50)
        self._refill_item(item6, 10)
        item7 = Item(7, "Yougurt", 1.50)
        self._refill_item(item7, 10)
        item8 = Item(8, "Almonds", 1.50)
        self._refill_item(item8, 2)
        item9 = Item(9, "Crackers", 1.50)
        self._refill_item(item9, 10)

    def _refill_item(self, item, quantity):
        for i in range(0, quantity):
            self._inventory.add(item)

    def run(self):
        keep_running = True
        reason_to_stop = ""
        while keep_running:
            # check all the reasons to stop the machine
            if not self._inventory.available_codes():
                keep_running = False
                reason_to_stop = "Machine stopped, no more items avaialable"
                continue
            choice = self._get_input()
            if choice == self._CODE_SHUTDOWN:
                keep_running = False
                reason_to_stop = "Machine stopped, operator code"
                continue
            if choice == self._CODE_REPORT_STATUS:
                self._register.report()
                self._inventory.report()
                continue
            # we got a valid choice, ask for money
            tpl = self._inventory.get(choice)
            item = tpl[0]
            raw_input("Payment Next: press enter to add money or 99 to cancel.")
            money_received = 0
            while money_received < item.price:
                val = raw_input("Collected ${}, insert $1 or $5:".format(money_received))
                val = int(val)
                # abort if client asked to cancel
                if val == 99:
                    break
                elif val not in [1, 5]:
                    print('Only $1 and $5 bills accepted, sorry.')
                    continue
                money_received += val
            else:
                # received the money, update register, distribute item, update inventory
                self._register.add_money(money_received)
                self._register.give_change(money_received - item.price)
                self._inventory.remove(item)
                print "Here is your {}, enjoy it!".format(item.name)

        print reason_to_stop

    def _get_input(self):
        # Map the user input to one of the possible code for the items sold.
        # We manage here operationals codes as well, i.e. shutdown machine.
        # Return an integer
        valid_codes = self._inventory.available_codes()
        valid_codes.append(self._CODE_SHUTDOWN)
        valid_codes.append(self._CODE_REPORT_STATUS)
        input_val = -1
        while input_val not in valid_codes:
            self.print_menu()
            try:
                input_val = int(raw_input("Select item (max change ${}): ".format(self._register.available_change())))
            except ValueError:
                print "Not valid number, try again"
        return input_val

    def print_menu(self):
		for i in self._inventory.available_items():
			print "{:8} ${:02.1f} Code:{}".format(i.name, i.price, i.code)

# Demoing:
vmachine = Machine()
vmachine.run()
