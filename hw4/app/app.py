from flask import Flask, render_template, request, g, redirect
from wtforms import (Form, SubmitField, BooleanField, SelectField, DecimalField)
import os
import dill
import pandas as pd

app = Flask(__name__)
model_path = os.path.join(app.root_path, 'model')

column_names = ['name', 'summary', 'space', 'description', 'neighborhood_overview', 'notes', 'transit', 'access',
                                                      'house_rules', 'host_about', 'host_response_time', 'host_response_rate', 'host_is_superhost',
                                                      'host_identity_verified', 'neighbourhood_cleansed', 'latitude', 'longitude', 'is_location_exact', 'bed_type',
                                                      'security_deposit', 'cleaning_fee', 'extra_people', 'minimum_nights', 'cancellation_policy',
                                                      'require_guest_profile_picture', 'require_guest_phone_verification']

host_response_time_arr = ['within an hour', 'within a few hours', 'within a day', 'None', 'a few days or more']
neighbourhood_cleansed_arr = ['Westminster', 'Tower Hamlets', 'Kensington and Chelsea', 'Camden', 'Hackney', 'Southwark', 'Islington', 'Lambeth',
                          'Hammersmith and Fulham', 'Wandsworth', 'Brent', 'Lewisham', 'Newham', 'Haringey', 'Ealing', 'Greenwich', 'Barnet', 'Merton',
                          'Waltham Forest', 'Croydon', 'Richmond upon Thames', 'Hounslow', 'Hillingdon', 'Redbridge', 'City of London', 'Bromley',
                          'Enfield', 'Kingston upon Thames', 'Harrow', 'Barking and Dagenham', 'Havering', 'Sutton', 'Bexley']
bed_type_arr = ['Real_Bed', 'Pull-out_Sofa', 'Futon', 'Couch', 'Airbed']

cancellation_policy_arr  = ['strict_14_with_grace_period', 'flexible', 'moderate', 'super_strict_30', 'super_strict_60']

# Create user input form
class AirbnbForm(Form):

    # team1 = SelectField(label = 'Team one', choices = teams, default = teams[0])
    # team2 = SelectField(label = 'Team two', choices = teams, default = teams[1])
    name = BooleanField(label = 'name', default="false")
    summary = BooleanField(label = 'summary')
    space = BooleanField(label = 'space')
    description = BooleanField(label = 'description')
    neighborhood_overview = BooleanField(label = 'neighborhood_overview')
    notes = BooleanField(label = 'notes')
    transit = BooleanField(label = 'transit')
    access = BooleanField(label = 'access')
    house_rules = BooleanField(label = 'house_rules')
    host_about = BooleanField(label = 'host_about')
    host_response_time = SelectField(label = 'host_response_time', choices = host_response_time_arr, default = host_response_time_arr[0])
    host_response_rate = DecimalField(label = 'host_response_rate', default=0)
    host_is_superhost = BooleanField(label = 'host_is_superhost')
    host_identity_verified = BooleanField(label = 'host_identity_verified')
    neighbourhood_cleansed = SelectField(label = 'neighbourhood_cleansed', choices = neighbourhood_cleansed_arr, default = neighbourhood_cleansed_arr[0])
    latitude = DecimalField(label = 'latitude', default=0)
    longitude = DecimalField(label = 'longitude', default=0)
    is_location_exact = BooleanField(label = 'is_location_exact')
    bed_type = SelectField(label = 'bed_type', choices = bed_type_arr, default = bed_type_arr[0])
    security_deposit = DecimalField(label = 'security_deposit', default=0)
    cleaning_fee = DecimalField(label = 'cleaning_fee', default=0)
    extra_people = DecimalField(label = 'extra_people', default=0)
    minimum_nights = DecimalField(label = 'minimum_nights', default=0)
    cancellation_policy = SelectField(label = 'cancellation_policy', choices = cancellation_policy_arr, default = cancellation_policy_arr[0])
    require_guest_profile_picture = BooleanField(label = 'require_guest_profile_picture')
    require_guest_phone_verification = BooleanField(label = 'require_guest_phone_verification')


    submit = SubmitField("Predict price!")


#Home page
@app.route('/',  methods=['GET', 'POST'])
def home():
    form = AirbnbForm(request.form)

    # Get team names and send to model
    if request.method == 'POST' and form.validate():
        name = form.name.data
        summary = form.summary.data
        space = form.space.data
        description = form.description.data
        neighborhood_overview = form.neighborhood_overview.data
        notes = form.notes.data
        transit = form.transit.data
        access = form.access.data
        house_rules = form.house_rules.data
        host_about = form.host_about.data
        host_response_time = form.host_response_time.data
        host_response_rate = form.host_response_rate.data
        host_is_superhost = form.host_is_superhost.data
        host_identity_verified = form.host_identity_verified.data
        neighbourhood_cleansed = form.neighbourhood_cleansed.data
        latitude = form.latitude.data
        longitude = form.longitude.data
        is_location_exact = form.is_location_exact.data
        bed_type = form.bed_type.data
        security_deposit = form.security_deposit.data
        cleaning_fee = form.cleaning_fee.data
        extra_people = form.extra_people.data
        minimum_nights = form.minimum_nights.data
        cancellation_policy = form.cancellation_policy.data
        require_guest_profile_picture = form.require_guest_profile_picture.data
        require_guest_phone_verification = form.require_guest_phone_verification.data

        return render_template('prediction.html',
                               price=model_predict(name, summary, space, description, neighborhood_overview, notes, transit, access,
                                                      house_rules, host_about, host_response_time, host_response_rate, host_is_superhost,
                                                      host_identity_verified, neighbourhood_cleansed, latitude, longitude, is_location_exact, bed_type,
                                                      security_deposit, cleaning_fee, extra_people, minimum_nights, cancellation_policy,
                                                      require_guest_profile_picture, require_guest_phone_verification))

    # Send template information to index.html
    return render_template('index.html', form=form)


def model_predict(name, summary, space, description, neighborhood_overview, notes, transit, access,
                                                      house_rules, host_about, host_response_time, host_response_rate, host_is_superhost,
                                                      host_identity_verified, neighbourhood_cleansed, latitude, longitude, is_location_exact, bed_type,
                                                      security_deposit, cleaning_fee, extra_people, minimum_nights, cancellation_policy,
                                                      require_guest_profile_picture, require_guest_phone_verification):
    basedir = os.path.abspath(os.path.dirname(__file__))
    with open(basedir + '/model/pipeline.pkl', 'rb') as file:
        model = dill.load(file)



    df = pd.DataFrame(columns=column_names)
    df.loc[0] = [name, summary, space, description, neighborhood_overview, notes, transit, access,
                                                      house_rules, host_about, host_response_time, host_response_rate, host_is_superhost,
                                                      host_identity_verified, neighbourhood_cleansed, latitude, longitude, is_location_exact, bed_type,
                                                      security_deposit, cleaning_fee, extra_people, minimum_nights, cancellation_policy,
                                                      require_guest_profile_picture, require_guest_phone_verification]

    convert_dict = {'name' : bool,
                    'summary' : bool,
                   'space' : bool,
                   'description' : bool,
                   'neighborhood_overview' : bool,
                   'notes' : bool,
                   'transit' : bool,
                   'access' : bool,
                   'house_rules' : bool,
                   'host_about' : bool,
                   'host_response_time' : object,
                   'host_response_rate' : float,
                   'host_is_superhost' : bool,
                   'host_identity_verified' : bool,
                   'neighbourhood_cleansed' : object,
                   'latitude' : float,
                   'longitude' : float,
                   'is_location_exact' : bool,
                   'bed_type' : object,
                   'security_deposit' : float,
                   'cleaning_fee' : float,
                   'extra_people' : float,
                   'minimum_nights' : int,
                   'cancellation_policy' : object,
                   'require_guest_profile_picture' : bool,
                   'require_guest_phone_verification' : bool
    }

    df = df.astype(convert_dict)
    prediction = model.predict(df)

    # Results
    html_price = "Predicted price %s" % (int(round(prediction[0])))

    return html_price


# Return to home page from prediction
@app.route('/button', methods=["GET", "POST"])
def button():
    if request.method == "POST":
        return redirect(("/"))


if __name__ == '__main__':
    app.run()
