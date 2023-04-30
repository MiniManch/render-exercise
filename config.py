db_info = {'host': 'aws.connect.psdb.cloud',
           'database': 'exercise',
           'psw': 'pscale_pw_tG533BNPG7yiXFeABmq0hsvto9UCubNO8CJv7qozhQE',
           'user': 'n3cwty9nyt3rz3huqhnx',
           'port': ''}


class Config:
    SECRET_KEY = "qwertyuiop"
    SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args": dict(host=db_info['host'], user=db_info['user'],
                             password=db_info['psw'], dbname=db_info['database'],
                             sslcert="client.crt", sslkey="client.key",
                             sslrootcert="ca.crt", sslmode="verify-full", ssl_min_protocol_version="TLSv1.3")
    }
    SQLALCHEMY_DATABASE_URI = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"

