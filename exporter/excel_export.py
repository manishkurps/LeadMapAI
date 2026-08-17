"""
Export Business Data to Excel
"""

import os
from datetime import datetime

from openpyxl import Workbook


def export_excel(businesses, output_folder, filename):

    os.makedirs(output_folder, exist_ok=True)

    wb = Workbook()

    ws = wb.active

    ws.title = "Businesses"

    ws.append([
        "Name",
        "Phone",
        "Website",
        "Address",
        "Rating",
        "Reviews",
        "Maps URL"
    ])

    for business in businesses:

        ws.append([

            business.name,

            business.phone,

            business.website,

            business.address,

            business.rating,

            business.reviews,

            business.maps_link

        ])

    filename = f"{filename}.xlsx"

    filepath = os.path.join(output_folder, filename)

    wb.save(filepath)

    print(f"Excel Saved : {filepath}")