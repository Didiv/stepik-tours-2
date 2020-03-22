from django.http import HttpResponseNotFound

from django.shortcuts import render

from django.views.generic import View

import tours.data as data


class MainView(View):
    def get(self, request):

        return render(
            request, 'tours/index.html', context={
                "title": data.title,
                "subtitle": data.subtitle,
                "description": data.description,
                "departures": data.departures,
                "tours": data.tours,
            }
        )


class DepartureView(View):
    def get(self, request, departure: str):

        if departure not in data.departures:
            return HttpResponseNotFound(
                f'Вылет из {departure} не поддерживается')

        tours_filtered = dict(
            filter(
                lambda x: x[1]['departure'] == departure,
                data.tours.items()))
        min_price = min(
            tours_filtered.values(),
            key=lambda x: x['price'])['price']
        max_price = max(
            tours_filtered.values(),
            key=lambda x: x['price'])['price']
        min_nights = min(
            tours_filtered.values(),
            key=lambda x: x['nights'])['nights']
        max_nights = max(
            tours_filtered.values(),
            key=lambda x: x['nights'])['nights']

        return render(
            request, 'tours/departure.html', context={
                "title": data.title,
                "subtitle": data.subtitle,
                "description": data.description,
                "departures": data.departures,
                "departure": departure,
                "departure_name": data.departures[departure],
                "tours": tours_filtered,
                "min_price": min_price,
                "max_price": max_price,
                "min_nights": min_nights,
                "max_nights": max_nights,
            }
        )


class TourView(View):
    def get(self, request, id: int):

        if id not in data.tours:
            return HttpResponseNotFound(
                f'Тур с id {id} нам не известен')

        return render(
            request, 'tours/tour.html', context={
                "title": data.title,
                "departures": data.departures,
                "tour": data.tours[id],
                "departure_name": data.departures[data.tours[id]['departure']]
            }
        )
