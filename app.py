import database.connection as conn
import database.DAO.devDAO as  dev

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/dev')
def get_dev():
  try:
    xconn=conn.initConnection()
    data_dev = dev.getDev(pconnection=xconn)
    return render_template('dev.html', data_dev=data_dev)
  except Exception as e:
    return '<h1>Ошибка: '+str(e)+'</h1>'
  finally:
   conn.closeConnection(pconnection=xconn)

if __name__ == '__main__':
        app.run(host='0.0.0.0')
