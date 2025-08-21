from fastapi import Query, APIRouter

from schemas.hotels import Hotel, HotelPATCH


router = APIRouter(prefix='/hotels', tags=['Отели'])


hotels = [
    {'id': 1, 'title': 'Sochi', 'stars': 3},
    {'id': 2, 'title': 'Saint-P', 'stars': 4},
    {'id': 3, 'title': 'Дубай', 'stars': 5},
    {'id': 4, 'title': 'Moscow', 'stars': 4},
    {'id': 5, 'title': 'Voronezh', 'stars': 3},
    {'id': 6, 'title': 'Rim', 'stars': 5}
]


@router.get('',
         summary='Получения списка отелей по конкретной сортировке параметров')
def get_hotel(
        id: int | None = Query(None, description='Айдишник'),
        title: str | None = Query(None, description='Название отеля'),
        stars: int | None = Query(None, description='Звезды отеля'),
        page : int = Query(1, description='Страница'),
        per_page : int = Query(3, description='Количество отелей на страницу')
):
    result = []
    for hotel in hotels:
        if id and id != hotel['id']:
            continue
        if title and title != hotel['title']:
            continue
        if stars and stars != hotel['stars']:
            continue
        result.append(hotel)
    start = (page - 1) * per_page
    finish = start + per_page

    return result[start:finish]


@router.post('',
          summary='Добавление отеля в базу',
          description='Добавление отеля в базу, обязательно указывать все параметры(title и stars)')
def create_hotel(hotel_data : Hotel):
    hotels.append({
        'id' : hotels[-1]['id'] + 1,
        'title' : hotel_data.title,
        'stars' : hotel_data.stars
    })

    return {'status': 'OK'}


@router.delete('/{hotel_id}',
            summary='Удаление конкретного отеля из базы',
            description='Удаления отеля из базы по конкретному id')
def delete_hotel(hotel_id : int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel['id'] != hotel_id]
    return {'status': 'OK'}


@router.put('/{hotel_id}',
         summary='Полное изменение информации об отеле',
         description='Изменение параметров title и stars по конкретному id')
def change_hotel(hotel_id : int, hotel_data : Hotel):
    global hotels
    hotel = [hotel for hotel in hotels if hotel['id'] == hotel_id][0]
    hotel['title'] = hotel_data.title
    hotel['stars'] = hotel_data.stars

    return {'status': 'OK'}


@router.patch('/{hotel_id}',
           summary='Частичное изменение информации об отеле',
           description='Здесь мы изменяем информацию об отелях в нашем приложении, мы можем изменить и title и stars, '
                       'либо что-то одно по конкретному id, не менять ничего не рекомендуется - нет смысла дергать этото endpoint')
def change_hotel(hotel_id : int, hotel_data: HotelPATCH):
    global hotels
    hotel = [hotel for hotel in hotels if hotel["id"] == hotel_id][0]
    if hotel_data.title:
        hotel['title'] = hotel_data.title
    if hotel_data.stars:
        hotel['stars'] = hotel_data.stars

    return {'status': 'OK'}