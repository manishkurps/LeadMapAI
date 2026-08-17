"""
Export Business Data to JSON
"""

import json
import os
from datetime import datetime

def export_json(businesses, output_folder, filename):

    os.makedirs(output_folder, exist_ok=True)

    filename = f"{filename}.json"

    filepath = os.path.join(output_folder, filename)

    data = [business.to_dict() for business in businesses]

    with open(filepath, "w", encoding="utf-8") as file:

        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"\nJSON Saved : {filepath}")