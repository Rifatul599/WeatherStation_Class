from datetime import datetime

class WeatherStation:
    def __init__(self):
        self.records=[]

    def record_temperature(self,temperature):
        timestamp=datetime.now()
        self.records.append({"temperature": temperature,"timestamp": timestamp})
        print(f"Recorded temperature {temperature} at {timestamp}.")

    def get_average_temperature(self):
        if not self.records:
            print("No temperature data available to calculate average.")
            return None
        total_temp=sum(record["temperature"] for record in self.records)
        average_temp=total_temp/len(self.records)
        return average_temp

    def get_highest_temperature(self):
        if not self.records:
            print("No temperature data available to find the highest temperature.")
            return None
        highest_temp=max(record["temperature"] for record in self.records)
        return highest_temp

    def get_lowest_temperature(self):
        if not self.records:
            print("No temperature data available to find the lowest temperature.")
            return None
        lowest_temp=min(record["temperature"] for record in self.records)
        return lowest_temp
    def get_temperature_on_date(self,date):
        if isinstance(date, str):
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        else:
            date_obj = date

            
        temperature_on_date = [
            record["temperature"]
            for record in self.records
            if record["timestamp"].date() == date_obj
        ]
        if not temperature_on_date:
            print(f"No temperature data available for {date_obj}.")
            return None
        return temperature_on_date

    def clear_data(self):
        self.records.clear()
        print("All temperature data has been cleared.")

station=WeatherStation()

station.record_temperature(22.5)
station.record_temperature(24.0)
station.record_temperature(23.5)

print(f"Average Temperature: {station.get_average_temperature():.2f}")
print(f"Highest Temperature: {station.get_highest_temperature()}")
print(f"Lowest Temperature: {station.get_lowest_temperature()}")

today=datetime.now().date()
print(f"Temperatures on {today}: {station.get_temperature_on_date(today)}")