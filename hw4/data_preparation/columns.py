long_text_cols = ['name', 'summary', 'space', 'description',
                  'neighborhood_overview', 'notes', 'transit',
                 'access', 'interaction', 'house_rules',
                  'host_about']
categoric_cols = ['host_response_time', 'property_type', 'bed_type',
                  'cancellation_policy','host_is_superhost',
                  'host_identity_verified',
                  'is_location_exact','require_guest_profile_picture',
                  'require_guest_phone_verification', 'room_type']
number_cols = ['latitude', 'longitude', 'extra_people',
              'minimum_nights']
#'bathrooms'bedrooms'accommodates', 'beds''guests_included'
special_cols = ['security_deposit', 'cleaning_fee', 'price']
useless_cols = ['host_has_profile_pic', 'host_since',
                'experiences_offered', 'square_feet',
                'amenities', 'interaction', 'room_type', 'property_type', 'guests_included', 'accommodates', 'bathrooms', 'bedrooms', 'beds']
id_cols = ['id', 'zipcode', 'host_id']
lat_long_cols = ['latitude', 'longitude']
# list_cols = ['amenities']

#columns to fill Nan with most frequent
col_to_fillna_most_frequent=[
                             'host_identity_verified',
                             'require_guest_phone_verification',
                             'minimum_nights',
                             'require_guest_profile_picture',
                             'is_location_exact',
                             'name', 'summary', 'space', 'description',
                  'neighborhood_overview', 'notes', 'transit',
                 'access', 'house_rules',
                  'host_about'
                            ]
#'interaction''beds','bedrooms','bathrooms',


#columns to fill Nan with mean
col_to_fillna_mean=['host_response_rate', 'security_deposit',
                   'cleaning_fee']

#columns for get_dummies (one hot encoding)
col_to_getdummies=['bed_type',
                   'cancellation_policy', 'host_response_time', 'neighbourhood_cleansed']
#'property_type','room_type'

# property_type - 19 - 5
# room_type - 20 - 3
# bed_type - 25 - 5
# cancellation_policy - 32 - 6
# host_response_time - 11 - 5
# neighbourhood_cleansed - 15 - 33


#columns that won't be changed
col_no_change=[
              'latitude', 'longitude']
# 'accommodates', 'guests_included'


# 41. feature 80 (0.198625) - Cancelation_polycy
# 2. feature 27 (0.196694) - neighbourhood_cleansed
# 3. feature 79 (0.176811) - Cancelation_polycy
# 4. feature 2 (0.132976) - space
# 5. feature 1 (0.119567) - summary
# 6. feature 21 (0.053805) - neighbourhood_cleansed
# 7. feature 20 (0.021392) - neighbourhood_cleansed
# 8. feature 83 (0.016821) - require_guest_profile_picture
# 9. feature 82 (0.012774) - Cancelation_polycy
# 10. feature 81 (0.007939) - Cancelation_polycy
# 11. feature 5 (0.007263) -
# 12. feature 19 (0.004950)
# 13. feature 9 (0.004909)
# 14. feature 0 (0.004680)
# 15. feature 23 (0.003545)
# 16. feature 24 (0.003215)
# 17. feature 28 (0.002674)
# 18. feature 39 (0.002610)
# 19. feature 15 (0.002224)
# 20. feature 40 (0.001376)
# 21. feature 44 (0.001136)
# 22. feature 3 (0.001032)
# 23. feature 25 (0.001029)
# 24. feature 18 (0.001022)
# 25. feature 35 (0.000931)
# 26. feature 11 (0.000929)
# 27. feature 36 (0.000906)
# 28. feature 75 (0.000875)
# 29. feature 14 (0.000863)
# 30. feature 17 (0.000812)
# 31. feature 73 (0.000745)
# 32. feature 22 (0.000721)
# 33. feature 57 (0.000701)
# 34. feature 38 (0.000696)
# 35. feature 13 (0.000675)
# 36. feature 49 (0.000658)
# 37. feature 7 (0.000648)
# 38. feature 10 (0.000641)
# 39. feature 43 (0.000552)
# 40. feature 16 (0.000514)
# 41. feature 78 (0.000511)
# 42. feature 67 (0.000503)
# 43. feature 51 (0.000477)
# 44. feature 41 (0.000457)
# 45. feature 45 (0.000445)
# 46. feature 70 (0.000445) - bed
# 47. feature 12 (0.000425) - host_response_time
# 48. feature 64 (0.000407) - bathrooms
# 49. feature 52 (0.000386)
# 50. feature 26 (0.000375) -
# 51. feature 65 (0.000352) - bedrooms
# 52. feature 69 (0.000352) - bed
# 53. feature 77 (0.000298) -
# 54. feature 32 (0.000297) -
# 55. feature 58 (0.000253) - property_type
# 56. feature 42 (0.000245)
# 57. feature 4 (0.000231)
# 58. feature 29 (0.000210)
# 59. feature 56 (0.000209)
# 60. feature 46 (0.000190)
# 61. feature 6 (0.000187)
# 62. feature 59 (0.000181)
# 63. feature 63 (0.000181)
# 64. feature 76 (0.000177)
# 65. feature 47 (0.000175)
# 66. feature 68 (0.000153)
# 67. feature 54 (0.000153)
# 68. feature 66 (0.000147)
# 69. feature 72 (0.000122)
# 70. feature 50 (0.000085)
# 71. feature 71 (0.000080) - bed
# 72. feature 53 (0.000076)
# 73. feature 60 (0.000074) - room
# 74. feature 74 (0.000044) - guest included
# 75. feature 34 (0.000034)
# 76. feature 33 (0.000030)
# 77. feature 55 (0.000026) - property-type
# 78. feature 48 (0.000022)
# 79. feature 62 (0.000018) - room
# 80. feature 61 (0.000015) - room
# 81. feature 31 (0.000012)
# 82. feature 30 (0.000000)
# 83. feature 8 (0.000000) - interaction
# 84. feature 37 (0.000000)
