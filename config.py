db_info = {'host': 'dpg-ch7oemrhp8u9bo7v73e0-a',
           'database': 'booksexercise',
           'psw': '7Ed9IXIIndJrSm4J8G9yVsHnz48ZjQL4',
           'user': 'emmanuel',
           'port': ''}

# postgres://emmanuel:7Ed9IXIIndJrSm4J8G9yVsHnz48ZjQL4@dpg-ch7oemrhp8u9bo7v73e0-a/booksexercise
class Config:
    SECRET_KEY = "qwertyuiop"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"

