import pickle
import csv


class Good:
    def __init__(self, name, exporting_country, count):
        self.name = name
        self.exporting_country = exporting_country
        self.count = count


class GoodSummary:
    def __init__(self):
        self.goods = []

    def add_good(self, good):
        self.goods.append(good)

    def find_good(self, good_name):
        for good in self.goods:
            if good.name == good_name:
                return good
        return None

    def sort_goods(self, key="name"):
        if key == "name":
            self.goods.sort(key=lambda x: x.name)
        elif key == "country":
            self.goods.sort(key=lambda x: x.exporting_country)
        elif key == "count":
            self.goods.sort(key=lambda x: x.count)
        else:
            print("Invalid sort key")

    def find_countries_for_product(self, good_name):
        countries = set()
        total_count = 0
        for good in self.goods:
            if good.name == good_name:
                countries.add(good.exporting_country)
                total_count += good.count
        return list(countries), total_count

    def save_to_csv(self, filename):
        with open(filename, "w") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Name", "Countries", "Count"])
            for good in self.goods:
                writer.writerow([good.name, good.exporting_country, good.count])

    @staticmethod
    def load_from_csv(filename):
        good_summary = GoodSummary()
        with open(filename, "r") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                name, exporting_country, count = row
                good = Good(name, exporting_country, count)
                good_summary.add_good(good)
        return good_summary

    def save_to_pickle(self, filename):
        with open(filename, "wb") as pickle_file:
            pickle.dump(self.goods, pickle_file)

    @staticmethod
    def load_from_pickle(filename):
        good_summary = GoodSummary()
        with open(filename, "rb") as pickle_file:
            good_summary.goods = pickle.load(pickle_file)
        return good_summary


def task1_run():
    good_summary = GoodSummary()
    while True:
        choice = int(
            input(
                "-----Choose an action-----\n"
                "- 1. Add a good\n"
                "- 2. Sorting goods by country of export\n"
                "- 3. Sorting goods by name\n"
                "- 4. Sorting goods by count of goods\n"
                "- 5. Find goods\n"
                "- 6. Save to csv\n"
                "- 7. Load from csv\n"
                "- 8. Save to pickle\n"
                "- 9. Load from pickle\n"
                "- 0. Exit\n"
                "--------------------------\n"
            )
        )
        match choice:
            case 0:
                break
            case 1:
                name = input("- Enter good name: ")
                country = input("- Enter the exporters country: ")
                count = input("- Enter the count of goods:")
                good_summary.add_good(Good(name, country, count))
            case 2:
                good_summary.sort_goods(key="country")
                print("Goods after sorting by export country:")
                for good in good_summary.goods:
                    print(f"-- {good.name}: {good.exporting_country}")
            case 3:
                good_summary.sort_goods(key="name")
                print("Goods after sorting by name:")
                for good in good_summary.goods:
                    print(f"-- {good.name}: {good.exporting_country}: {good.count}")
            case 4:
                good_summary.sort_goods(key="count")
                print("Goods after sorting by count of goods:")
                for good in good_summary.goods:
                    print(f"-- {good.name}: {good.count}")
            case 5:
                good_name = input("Enter the good name to search: ")
                found_good = good_summary.find_good(good_name)
                if found_good:
                    print(
                        f"-- Found good: {found_good.name} from country {found_good.exporting_country} in count {found_good.count}"
                    )
                else:
                    print("-- Good not found.")
            case 6:
                good_summary.save_to_csv("task1/goods.txt")
            case 7:
                good_summary = GoodSummary.load_from_csv("task1/goods.txt")
                for good in good_summary.goods:
                    print(good.name, good.exporting_country, good.count)
            case 8:
                good_summary.save_to_pickle("task1/goods.pkl")
            case 9:
                good_summary = GoodSummary.load_from_pickle("task1/goods.pkl")
                for good in good_summary.goods:
                    print(good.name, good.exporting_country, good.count)
