import pandas as pd
import matplotlib.pyplot as plt

# класс для сохранения графика периода дат
class DateGraphic:
    def __init__(self, date, freq, period, filename):
        self.date = date
        self.freq = freq
        self.period = period
        self.dates = pd.date_range(start=date, periods=period, freq=freq)
        self.df = pd.DataFrame({
                    'value': range(period)
        }, index=self.dates)
        self.graphic = None
        self.filename = filename

    def save_graphic(self):
        plt.plot(self.df.index, self.df['value'], marker='o')
        plt.grid(True)
        plt.xticks(rotation=60)
        plt.tight_layout()
        plt.savefig(f'{self.filename}.png')
        plt.close()

        print(f"График сохранён в файл '{self.filename}.png'")        

