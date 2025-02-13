import sqlite3

conn = sqlite3.connect('/Users/udaisinghmehra/Downloads/ages.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

cur.execute('DROP TABLE IF EXISTS ECounts')
cur.execute('CREATE TABLE ECounts (email TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM ECounts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO ECounts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE ECounts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM ECounts ORDER BY count' # DESC LIMIT 10'
dom_dict={}
for row in cur.execute(sqlstr):
    full_email=str(row[0]).split('@')
    org=full_email[1]
    val=int(str(row[1]))
    #print(org)
    dom_dict[org] = dom_dict.get(org,0) + val
#print(dom_dict)
#for keys in dom_dict:
#    print(keys, dom_dict[keys])
cur.close()

conn = sqlite3.connect('/Users/udaisinghmehra/Downloads/ages.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
for keys in dom_dict:
    print(keys, dom_dict[keys])
    val = (keys, int(dom_dict[keys]))
    row = cur.fetchone()
    sql = 'INSERT INTO Counts (org, count) VALUES (?, ?)'
    cur.execute(sql, val)
    conn.commit()
cur.close()
