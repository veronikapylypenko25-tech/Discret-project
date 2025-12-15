import requests

filename = "2_Пилипенко.txt"
API_KEY = '2ffda98bfbe8f5d17280fa7d817d1e2b'

def write_log(line: str):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(line.strip() + "\n")

class OpenWeatherMap:
    def __init__(self, city: str):
        self._city_requested = city
        self.key = API_KEY
        self._data = None

        try:
            self.__set_data(city)
            if self._data is None:
                write_log(f"Помилка! Дані для '{city}' не отримано!!!")
            else:
                write_log(f"Помилка! Дані для '{city}' отримано!!!")
        except Exception as e:
            write_log(f"INIT ERROR для '{city}': {e}!")

    def __set_data(self, city):
        try:
            resp = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.key}"
            )
            resp.raise_for_status()

            self._data = resp.json()

        except requests.exceptions.HTTPError:
            if resp.status_code == 404:
                print(f"Помилка: такого міста '{city}' не знайдено! Ви не корректно ввели назву! Спробуйте ще!")
            elif resp.status_code == 401:
                print("Помилка: Невірний API KEY!")
            else:
                print(f"HTTP помилка: {resp.status_code}")
            self._data = None

        except requests.exceptions.RequestException:
            print("Помилка! Наразі неможливо з'єднатися з сервером OpenWeatherMap!")
            self._data = None

    def get_temp(self, system="C"):
        try:
            temp = self._data["main"]["temp"]

            if system == "C":
                val = round(temp - 273.15, 1)
            elif system == "F":
                val = round((temp - 273.15) * 9 / 5 + 32, 1)
            elif system == "K":
                val = round(temp, 1)
            else:
                val = None

            write_log(f"get_temp({system}) => {val}")
            return val

        except Exception as e:
            write_log(f"get_temp ERROR: {e}")
            return None

    def get_weather(self):
        try:
            w = self._data["weather"][0]["main"]
            write_log(f"get_weather => {w}")
            return w
        except Exception as e:
            write_log(f"get_weather ERROR: {e}")
            return "Невідомо!"

    def get_wind(self):
        try:
            deg = self._data["wind"]["deg"]
            sectors = ["Північ", "Схід", "Південь", "Захід"]
            idx = int((deg + 22.5) // 90) % 4
            direction = sectors[idx]
            write_log(f"get_wind => {direction}")
            return direction
        except Exception as e:
            write_log(f"get_wind ERROR: {e}")
            return "Невідомо!"

    def get_city(self):
        try:
            city_name = self._data["name"]
            write_log(f"get_city => {city_name}")
            return city_name
        except Exception as e:
            write_log(f"get_city ERROR: {e}")
            return "Невідомо!"

    def get_text(self):
        try:
            d = self._data
            text = (
                f"Місто: {d.get('name')} | "
                f"Погода: {d['weather'][0].get('main')} | "
                f"Опис: {d['weather'][0].get('description')} | "
                f"Температура (K): {d['main'].get('temp')} | "
                f"Тиск: {d['main'].get('pressure')} | "
                f"Вологість: {d['main'].get('humidity')} | "
                f"Швидкість вітру: {d['wind'].get('speed')} | "
                f"Напрям вітру: {d['wind'].get('deg')}"
            )
            write_log(f"get_text => {text}")
            return text

        except Exception as e:
            write_log(f"get_text ERROR: {e}")
            return "Неможливо сформувати текст."

    def show(self):
        try:
            city = self.get_city()
            weather = self.get_weather()
            temp = self.get_temp("C")

            result = f"Сьогодні у {city} погода буде - {weather}. Температура за вікном {temp} °C"
            print(result)
            write_log(f"show => {result}")
            return result

        except Exception as e:
            write_log(f"show ERROR: {e}")
            print("Неможливо відобразити дані.")
            return None

    def get_set_data_method(self):
        try:
            return self.__set_data
        except Exception as e:
            write_log(f"get_set_data_method ERROR: {e}")
            return None

def ai(data: dict, set_data_func=None) -> str:
    advice = []
    try:
        temp_c = round(data['main']['temp'] - 273.15, 1)
        weather_main = data['weather'][0]['main'].lower()

        if "rain" in weather_main or "drizzle" in weather_main:
            advice.append("Не забудьте парасольку.")
        elif "snow" in weather_main:
            advice.append("Одягніться тепліше, можлива ожеледиця.")
        elif "clear" in weather_main or "sun" in weather_main:
            advice.append("Сьогодні можна не брати парасольку. Не забудьте взяти капелюх.")

        if temp_c <= 0:
            advice.append("Буде дуже холодно, рекомендується взяти шапку та рукавички.")
        elif 0 < temp_c <= 5:
            advice.append("Холодно,рекомендується вдягнути теплий одяг.")
        elif 10 < temp_c <= 20:
            advice.append("Прохолодно, але куртка буде достатньою.")
        elif 20 < temp_c <= 28:
            advice.append("Тепло, рекомендується обирати весняний або літній одяг.")
        else:
            advice.append("Буде спекотно рекомендується одягти легкий літній одяг.")

        text = " ".join(advice)
        write_log(f"ai => {text}")
        return text

    except Exception as e:
        write_log(f"ai ERROR: {e}")
        return "Неможливо сформувати пораду."

if __name__ == "__main__":
    city = input("City>>> ").strip()
    owm = OpenWeatherMap(city)
    if owm._data:
        owm.show()
        print("\nДетальний звіт:")
        print(owm.get_text())
        print("\nПорада на день:")
        print(ai(owm._data, set_data_func=owm.get_set_data_method()))
    else:
        print("Помилка! Дані не було отримано. Перевірте назву міста.")
