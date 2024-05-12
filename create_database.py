import sqlite3

def create_database():
    """SQLite veritabanı oluştur."""
    try:
        conn=sqlite3.connect('database.db')
        print("veritabanı oluşturuldu ve bağlanıldı.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

if __name__=="__main__":
    create_database()
