def change():
    expense = 23.75
    money = 100
    vueltop = int(money - expense)
    vueltoc = (money-expense)*100-(vueltop)*100
    print(f"Ingresar gasto:\n{expense}")
    print(f"Dinero recibido\n{money}")
    print(f"\nVuelto")
    print(f"\nPesos:\n{vueltop}")
    print(f"Centavos:\n{int(vueltoc)}")

change()
