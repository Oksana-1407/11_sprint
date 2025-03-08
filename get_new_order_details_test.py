# Оксана Королева, 27а когорта — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_request


def test_get_new_order_details():
    response_order = sender_stand_request.post_new_order(data.order_body)
    track = response_order.json().get("track")
    
    
    response_get_order = sender_stand_request.get_new_order(track)
    
    assert response_get_order.status_code == 200
