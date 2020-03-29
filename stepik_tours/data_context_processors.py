import tours.data as data


def data_context_processors(requests) -> dict:
    return {
        "tours": data.tours,
        "departures": data.departures,
        "title": data.title,
        "subtitle": data.subtitle,
        "description": data.description,
        "departure": '', # метка текущего направления
    }
