from data_preparation.columns import *

import pandas as pd


def str_to_bool(s):
    if s== 't':
        return True
    else:
        return False


def str_to_bool_2(s):
    return s == s


def str_to_rate(s):
    if pd.isnull(s) == False:
        return float(s.replace('%', ''))
    else:
        return s


def extract_list_val(s):
    for c in ['{', '}', '"']:
        s = s.replace(c, '')
    for c in ['/', ':', ' ', '-', '.', '&', ')', '(', '\'']:
        s = s.replace(c, '_')
    s = s.replace('matress', 'mattress')
    return s.split(',')


def preprocessing_no_useless_cols(data):
    data.drop(columns=useless_cols, inplace=True)
    return data


def preprocessing_property_type(data):
    dict1 = {'Apartment': ['Condominium', 'Timeshare', 'Loft',
                           'Serviced apartment', 'Guest suite'],
             'House': ['Vacation home', 'Villa', 'Townhouse', 'In-law',
                       'Casa particular', 'Cottage',
                       'Casa particular (Cuba)'],
             'Hotel1': ['Dorm', 'Hostel', 'Guesthouse', 'Hotel',
                        'Aparthotel'],
             'Hotel2': ['Boutique hotel', 'Bed and breakfast'],
             'Other': ['Island', 'Castle', 'Yurt', 'Hut', 'Chalet',
                       'Treehouse', 'Earth House', 'Tipi', 'Cave',
                       'Train', 'Parking Space', 'Lighthouse',
                       'Tent', 'Boat', 'Cabin', 'Camper/RV', 'Bungalow',
                       'Tiny house', 'Houseboat', 'Earth house',
                       'Barn', 'Farm stay', 'Nature lodge',
                       'Ryokan (Japan)', 'Bus',
                       'Shepherd\'s hut (U.K., France)', 'Resort',
                       'Dome house']
             }
    dict2 = {i: k for k, v in dict1.items() for i in v}
    #     data['property_type'].value_counts()
    data['property_type'].replace(dict2, inplace=True)
    #     data['property_type'].value_counts()
    return data


def preprocessing_general(data):
    data['room_type'] = data['room_type'].str.replace(' ', '_')
    data['bed_type'] = data['bed_type'].str.replace(' ', '_')
    data['host_response_rate'] = data['host_response_rate'].apply(str_to_rate)
    data['host_identity_verified'] = data['host_identity_verified'].apply(str_to_bool)
    data['host_is_superhost'] = data['host_is_superhost'].apply(str_to_bool)
    data['amenities'] = data['amenities'].apply(extract_list_val).str.join(' ')

    data['require_guest_phone_verification'] = data['require_guest_phone_verification'].apply(str_to_bool)
    data['require_guest_profile_picture'] = data['require_guest_profile_picture'].apply(str_to_bool)
    data['is_location_exact'] = data['is_location_exact'].apply(str_to_bool)

    return data


def preprocessing_no_text(data):
    data.drop(columns=long_text_cols, inplace=True)
    return data


def preprocessing_text_and_nan_to_bool(data):
    for c in long_text_cols:
        data[c] = data[c].apply(str_to_bool_2)
    return data


def preprocessing_no_id(data):
    data.drop(columns=id_cols, inplace=True)
    return data


def preprocessing_1(data):
    return preprocessing_no_useless_cols(
        preprocessing_general(
            preprocessing_no_id(
            preprocessing_text_and_nan_to_bool(
                preprocessing_property_type
                (data)
            ))))