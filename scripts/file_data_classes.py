from bs4 import BeautifulSoup


'''A module to store file data classes, and methods to work with html files'''


class ChileFiles:
    def __init__(self, file_path, file_year):
        self.file_path = file_path
        self.file_year = file_year
        self.file_totals = 0

    def extract_data(self):
        '''Extract td for each html file located at self.file_path'''
        with open(self.file_path, 'r', encoding="iso-8859-1") as file:
            soup = BeautifulSoup(file, 'html.parser')
            main_data = [
                [td.get_text(strip=True) for td in tr.find_all('td')]
                for tr in soup.find_all('tr')
            ]

            '''get the total name count for that file located at index [-2], assign it to self.file_totals'''
            string = [i.replace('.', '') for i in main_data[-2]]
            self.file_totals = int(
                ''.join(filter(str.isdigit, ''.join(string))))

            '''Delete unnecessary rows'''
            del main_data[0:2]

            '''Append file totals and file year to each row'''
            for row in main_data:
                row.append(self.file_totals)
                row.append(self.file_year)
            return main_data
