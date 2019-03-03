import pandas



ipfile = "/home/praveensusundre/Git/voyager/list_of_cities.csv"
pl = pandas.read_csv(ipfile)

r = pl[['Name of City','State']]

r.insert(2,'state_id',0)

ipfile2 = "/home/praveensusundre/Git/voyager/India_States.csv"

pl2 = pandas.read_csv(ipfile2)

for row1 in r.State:
    for row2 in pl2.State_Name:
        if row1 == row2:
            r.state_id[r['State'] == row1] = int(pl2.State_Id[pl2['State_Name'] == row2])

r[['Name of City','state_id']].to_csv('/home/praveensusundre/Git/voyager/India_cities.csv')

