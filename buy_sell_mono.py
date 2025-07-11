import requests
from datetime import date


def get_rates():
    url = "https://api.monobank.ua/bank/currency"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()


def find_rate(data, curr_from, curr_to):
    for item in data:
        if item["currencyCodeA"] == curr_from and item["currencyCodeB"] == curr_to:
            return item.get("rateBuy"), item.get("rateSell")
    return None, None


if __name__ == "__main__":
    data = get_rates()
    buy, sell = find_rate(data, 840, 980)  # USD → UAH

    if buy and sell:
        print(f"Курс USD → UAH: купівля {buy:.4f}, продаж {sell:.4f}")
        today = date.today().strftime("%d.%m.%Y")

        try:
            amount_buy = float(input("Скільки доларів Ви хочете купити? "))
            amount_sell = float(input("Скільки доларів Ви хочете продати? "))

            # Купівля доларів (тобто ви купуєте USD, платите UAH за курсом продажу банку)
            cost_to_buy = amount_buy * sell

            # Продаж доларів (ви продаєте USD банку, отримуєте UAH за курсом купівлі банку)
            received_from_sell = amount_sell * buy

            print(f"Щоб купити {amount_buy:.2f} USD, потрібно {cost_to_buy:.2f} UAH станом на {today}")
            print(f"При продажі {amount_sell:.2f} USD Ви отримаєте {received_from_sell:.2f} UAH станом на {today}")

        except ValueError:
            print("Помилка: потрібно ввести коректне число.")
    else:
        print("Курс USD/UAH не знайдено.")
