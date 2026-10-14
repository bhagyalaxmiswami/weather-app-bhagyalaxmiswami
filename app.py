import streamlit as st
import requests
API_KEY= 'aab22aa6311d02c811bde2fadd2cd0b3'

st.set_page_config(page_title='Weather App',page_icon='🌦️')

st.title('Weather App 🌦️')

st.write('Enter the city name and click the button to fetch the weather data')

city = st.text_input('Enter the city name')

if(st.button('Fetch weather')):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')
    if(response.status_code==200):
        st.success('weather data Fetched successfully')
        data=response.json()


        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather_condition =data ['weather'][0]['description']
        name= data['name']
        country = data['sys']['country']

        st.subheader(f'{name},{country}')


        col1 ,col2 = st.columns(2)
        col3 ,col4=st.columns(2)

        col1.metric('Temperature🌡️',f'{temperature}°C')
        col2.metric('Humidity💦',f'{humidity}%')
        col3.metric('wind speed🍃',f'{wind_speed}m/s')
        col4.metric('weather condition🌤️',f'{weather_condition}')

    else:
        st.error('city not found')



  