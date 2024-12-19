
def getDev(pconnection):
  try:
    xcursor = pconnection.cursor()
    xdev = []
    xsql = 'SELECT  number, name, price, finance, state  FROM  dev_tab'
    xcursor.execute(xsql,())
    xcolumns = [column[0] for column in xcursor.description]
    xrows =  xcursor.fetchall()
    for  row in xrows:
     xdev.append(dict(zip(xcolumns,row)))
    return  xdev
  finally:
    xcursor.close()
