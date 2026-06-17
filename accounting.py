import csv
def main():
    all_transactions()


def get_data():
    database = []
    with open("annual_transaction_data_2025.csv","r") as file:
         reader = csv.DictReader(file)
         for row in reader:
             database.append({"id":row["id"],
                            "date":row["date"],
                            "month":row["month"],
                            "transaction":row["transaction"],
                            "amount":row["amount"]
                        })
    return database


def all_transactions():
    database = get_data()
    for data in database:
        print(data)



def total_purchase(show=False):
    database = get_data()
    total_purchase = 0

    for row in database:
        if row["transaction"] == "Purchase":
            total_purchase += float(row["amount"])
    if show:
        print(f"Total Purchase ={total_purchase:.2f}")

    return total_purchase


def total_sales(show=False):
    database = get_data()
    total_sale = 0

    for row in database:
        if row["transaction"] == "Sale":
            total_sale += float(row["amount"])
    if show:
        print(f"Total Sale  ={total_sale:.2f}")

    return total_sale

def net_profit_loss():
    if (total_sales()-total_purchase()) > 0:
       print(f"net profit: {(total_sales()-total_purchase()):.2f}")
    
    elif (total_sales()-total_purchase()) == 0:   
       print(f"no profit no loss")
    
    else:
        print(f"net loss{(total_sales()-total_purchase()):.2f}")


def highest_sale():
    database = get_data()
    highest_sale = None

    for data in database:
        if data["transaction"] == "Sale":
            if highest_sale is None or float(data["amount"]) > float(highest_sale["amount"]):
                highest_sale = data

    print(highest_sale)


def highest_purchase():
    database = get_data()
    highest_purchase = None

    for data in database:
        if data["transaction"] == "Purchase":
            if highest_purchase is None or float(data["amount"]) > float(highest_purchase["amount"]):
                highest_purchase = data

    print(highest_purchase)

if __name__ == '__main__':
    main()
