from django.shortcuts import render
from .models import Phone, ApplePhone, SamsungPone, PechenkaPhone


def show_catalog(request):
    phone_list = list(Phone.objects.all())
    comparison_dict = {'Модель': [],
                       'Стоимость': [],
                       'Операционная система': [],
                       'Оперативная память': [],
                       'Разрешение экрана': [],
                       'Разрешение камеры': [],
                       'Процессор': [],
                       'FM - радио': [],
                       'Дополнительно': []}

    def phone_to_dict(phone):
        comparison_dict['Модель'].append(phone.model)
        comparison_dict['Стоимость'].append(phone.price)
        comparison_dict['Операционная система'].append(phone.os)
        comparison_dict['Оперативная память'].append(phone.ram)
        comparison_dict['Разрешение экрана'].append(phone.screen_resolution)
        comparison_dict['Разрешение камеры'].append(phone.camera_resolution)
        comparison_dict['Процессор'].append(phone.cpu)
        if hasattr(phone, 'fm_radio'):
            comparison_dict['FM - радио'].append(phone.fm_radio)
        else:
            comparison_dict['FM - радио'].append(False)
        if isinstance(phone, ApplePhone):
            comparison_list = []
            if phone.air_pods:
                comparison_list.append("AirPods")
            if phone.face_id:
                comparison_list.append("FaceID")
            if phone.apple_pay:
                comparison_list.append("ApplePay")
            comparison_dict['Дополнительно'].append(comparison_list)
            # comparison_list = ''
            # if phone.air_pods:
            #     comparison_list += "AirPods \n"
            # if phone.face_id:
            #     comparison_list += "FaceID \n"
            # if phone.apple_pay:
            #     comparison_list += "ApplePay \n"
            # comparison_dict['Дополнительно'].append(comparison_list)
        if isinstance(phone, SamsungPone):
            comparison_list = []
            if phone.samsung_pay:
                comparison_list.append("SamsungPay")
            comparison_dict['Дополнительно'].append(comparison_list)

    for phone in list(ApplePhone.objects.all()):
        phone_to_dict(phone)

    for phone in list(SamsungPone.objects.all()):
        phone_to_dict(phone)

    for phone in list(PechenkaPhone.objects.all()):
        phone_to_dict(phone)




    # print (comparison_dict)
    context = {'phones': comparison_dict,
              'len': len(phone_list),
               'phone': phone_list
              }

    # print(context['phones'])
    return render(
        request,
        'catalog.html', context
    )
