import math

class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []

    def deposit(self,amount,description=""):
        self.ledger.append({'amount': amount,'description': description})

    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount,'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)
    
    def transfer(self,amount,category):
        if self.check_funds(amount):
            self.withdraw(amount,f'Transfer to {category.name}')
            category.deposit(amount,f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self,amount):
        return amount<=self.get_balance()
    
    def __str__(self):
        title = f'{self.name:*^30}\n'
        items = ""
        for item in self.ledger:
            desc = item['description'][:23]
            amount = f"{item['amount']:>7.2f}"
            items += f'{desc:<23}{amount}\n'
        total = f'Total: {self.get_balance():0.2f}'
        return title + items + total
    
def create_spend_chart(categories):
    title = f'Percentage spent by category\n'
    withdrawn=[]
    total_withdrawn = 0
    for cat in categories:
        spent = sum(abs(item['amount']) for item in cat.ledger if item['amount']<0)
        withdrawn.append(spent)
        total_withdrawn += spent

    percent = [math.floor((item/total_withdrawn)*10)*10 for item in withdrawn]

    contents = ""
    for i in range(100,-1,-10):
        contents += f'{i:>3}|'
        for per in percent:
            contents += ' o ' if per >= i else '   '
        contents += " \n"
    
    contents += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        contents += '    '
        for thing in categories:
            if i < len(thing.name):
                contents += f' {thing.name[i]} '
            else:
                contents += f'   '
        contents += ' \n' if i < max_len - 1 else ' '

    return title + contents
        

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
food.withdraw(105.55, "groceries")
food.withdraw(33.40, "snacks")

entertainment.deposit(900, "deposit")
entertainment.withdraw(150, "movies")

business.deposit(900, "deposit")
business.withdraw(10, "taxi")

print(create_spend_chart([business, food, entertainment]))
        
         
