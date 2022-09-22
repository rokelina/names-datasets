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


class UsaFiles:
    def __init__(self, file_path, file_year):
        self.file_path = file_path
        self.file_year = file_year

    def extract_data(self):
        '''Extract td for each html file located at self.file_path'''

        with open(self.file_path, 'r', encoding="iso-8859-1") as file:
            soup = BeautifulSoup(file, "html.parser")
            tables = [
                [
                    [td.get_text(strip=True) for td in tr.find_all('td')]
                    for tr in table.find_all('tr')
                ]
                for table in soup.find_all('table')
            ]

            '''The data we need is on tables[2], checks for rows that have 5 objects in it (rank, male name, male count, female name, female count)'''
            main_data = []
            for item in tables[2]:
                if len(item) == 5:
                    '''we only want to append male name, male count, female name, female count and file year'''
                    new_row = [item[1], int(item[2].replace(',', '')),
                               item[3], int(item[4].replace(',',  '')), self.file_year]
                    main_data.append(new_row)
            return main_data
