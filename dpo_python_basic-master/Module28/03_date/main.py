class Date:
    def __init__(self, day: int = 0, month=0, year: int = 0) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return f'День: {self.day}\tМесяц: {self.month}\tГод: {self.year}'

    @classmethod
    def split_date(cls, date: str) -> None:
        dmy_lst = []
        if '-' in date:
            dmy_lst = date.split('-')
        elif '/' in date:
            dmy_lst = date.split('/')
        elif '.' in date:
            dmy_lst = date.split('.')
        if len(dmy_lst) != 3:
            cls.day = None
            cls.month = None
            cls.year = None
        else:
            cls.day, cls.month, cls.year = map(int, dmy_lst)

    @classmethod
    def date_valid(cls, date: str) -> bool:
        cls.split_date(date)
        return 0 < cls.day <= 31 and 0 < cls.month <= 12 and 0 < cls.year <= 9999

    @classmethod
    def dmy_string(cls, date: str) -> 'Date':
        cls.split_date(date)
        date_obj = cls(cls.day, cls.month, cls.year)
        return date_obj


date = Date.dmy_string('10-06-1997')
print(date)
print(Date.date_valid('11-13-2022'))
print(Date.date_valid('16-03-2023'))
