from ckan_api_controller import CkanController
from pprint import pprint
import json

if __name__ == "__main__":

    url = 'https://data.gov.il'
    params = {
        'resource_id':'bfd22231-7a8b-4fc0-91bd-342397860ab5',
        'limit':'10000'
    }
    con = CkanController(url, params)
    # con.request_data()
    # con.request_data()
    data = con.request_data()

    df = con.ckan_to_dataframe(data)

    df.to_csv(r'C:\Users\yamti\PycharmProjects\data-science-project\resources\ravkav2022.csv')

