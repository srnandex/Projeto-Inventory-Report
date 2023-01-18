from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def import_data(self, path, type):
        data = []

        with open(path, "r") as file:
            if path.endswith(".csv"):
                data = list(csv.DictReader(file))
            if path.endswith(".json"):
                data = json.load(file)
            if path.endswith(".xml"):
                data = xmltodict.parse(file.read())["dataset"]["record"]

        if type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)
