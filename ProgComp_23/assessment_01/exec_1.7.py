#pedrohcdsouza arquive

cash = float(input("Enter the withdrawal amount: "))
cash_note = int(cash)
cash_coin = (cash-cash_note)*100
if cash < 0.01:
    print("Write a valid number!")
else:
    note_100 = cash_note//100
    cash_note = cash_note%100
    note_50 = cash_note//50
    cash_note = cash_note%50
    note_20 = cash_note//20
    cash_note = cash_note%20
    note_10 = cash_note//10
    cash_note = cash_note%20
    note_5 = cash_note//5
    cash_note = cash_note%5
    note_2 = cash_note//2
    cash_note = cash_note%2
    coin_1 = cash_coin//100
    cash_coin = cash_coin%100
    coin_05 = cash_coin//50
    cash_coin = cash_coin%50
    coin_025 = cash_coin//25
    cash_coin = cash_coin%25
    coin_010 = cash_coin//10
    cash_coin = cash_coin%10
    coin_005 = cash_coin//5
    cash_coin = cash_coin%5
    coin_001 = cash_coin//1
    cash_coin = cash_coin%1
    if note_100 > 0:
        print(f"Você receberá {note_100} cédulas de 100 reais.")
    if note_50 > 0:
        print(f"Você receberá {note_50} cédulas de 50 reais.")
    if note_20 > 0:
        print(f"Você receberá {note_20} cédulas de 20 reais.")
    if note_10 > 0:
        print(f"Você receberá {note_10} cédulas de 10 reais.")
    if note_5 > 0:
        print(f"Você receberá {note_5} cédulas de 5 reais.")
    if note_2 > 0:
        print(f"Você receberá {note_2} cédulas de 2 reais.")
    if coin_1 > 0:
        print(f"Você receberá {coin_1} moeda(s) de 1 real.")
    if coin_05 > 0:
        print(f"Você receberá {coin_05} moeda(s) de 50 centavos.")
    if coin_025 > 0:
        print(f"Você receberá {coin_025} moeda(s) de 25 centavos.")
    if coin_010 > 0:
        print(f"Você receberá {coin_010} moeda(s) de 10 centavos.")
    if coin_005 > 0:
        print(f"Você receberá {coin_005} moeda(s) de 5 centavos.")
    if coin_001 > 0:
        print(f"Você receberá {coin_001} moeda(s) de 1 centavo.")
    else:
        print("Error")

    
    