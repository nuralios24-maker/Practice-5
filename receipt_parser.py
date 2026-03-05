import re
import json


def parse_receipt(text: str) -> dict:
    result = {}

    product_pattern = r"\d+\.\s*\n(.+)"
    products = re.findall(product_pattern, text)
    products = [p.strip() for p in products]
    result["products"] = products

    price_pattern = r"\d{1,3}(?:\s\d{3})*,\d{2}"
    prices = re.findall(price_pattern, text)

    prices_float = [
        float(p.replace(" ", "").replace(",", "."))
        for p in prices
    ]
    result["all_prices"] = prices_float

    total_pattern = r"ИТОГО:\s*\n?([\d\s,]+)"
    total_match = re.search(total_pattern, text)

    if total_match:
        total_amount = float(
            total_match.group(1).replace(" ", "").replace(",", ".")
        )
    else:
        total_amount = None

    result["total_amount"] = total_amount

    datetime_pattern = r"Время:\s*(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})"
    datetime_match = re.search(datetime_pattern, text)

    result["date_time"] = datetime_match.group(1) if datetime_match else None

    payment_pattern = r"(Банковская карта|Наличные)"
    payment_match = re.search(payment_pattern, text)

    result["payment_method"] = payment_match.group(1) if payment_match else None

    return result


def main():
    with open("raw.txt", "r", encoding="utf-8") as file:
        receipt_text = file.read()

    parsed_data = parse_receipt(receipt_text)

    print(json.dumps(parsed_data, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()