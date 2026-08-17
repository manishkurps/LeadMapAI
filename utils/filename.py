import re

def generate_filename(search_query, total_businesses):
    """
    Generate a clean filename.

    Example:
    Banquet Hall Pune, 10
    ->
    Banquet_Hall_Pune_10
    """

    filename = search_query.strip()

    # Replace spaces with underscores
    filename = filename.replace(" ", "_")

    # Remove invalid filename characters
    filename = re.sub(r'[\\/*?:"<>|]', "", filename)

    return f"{filename}_{total_businesses}"