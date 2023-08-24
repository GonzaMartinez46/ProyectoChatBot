
###################
# SQL SERVER (servidor Central DB: Rumaos)
###################
# Some other example server values are
# server = "localhost\sqlexpress" # for a named instance
# server = "myserver,port" # to specify an alternate port
# server = "tcp:myserver.database.windows.net"
server = "192.168.200.33,50020\cloud"
database = "Rumaos"
username = "gpedro" 
password = "s3rv1d0r"

login = [server,database,username,password]


###################
# SQL SERVER (servidor SGESFIN DB: Sgfin)
###################

loginSGFin = [
    "192.168.200.33\SGESFIN"
    , "Sgfin"
    , "gpedro"
    , "pedrito1234"
]


###################
# SQL SERVER (servidor Azcuénaga DB: MILENIUM)
###################

loginAZMilenium = [
    "192.168.111.30\sqlexpress"
    , "MILENIUM"
    , "gpedro"
    , "pedrito1234"
]


###################
# SQL SERVER (servidor Perdriel I DB: MILENIUM)
###################

loginPIMilenium = [
    "192.168.107.32\sqlexpress"
    , "MILENIUM"
    , "gpedro"
    , "pedrito1234"
]


###################
# SQL SERVER (servidor Deposito Perdriel I DB: SGES_UEN)
###################

loginPIDeposito = [
    "192.168.107.32\DEPOSITO"
    , "SGES_UEN"
    , "gpedro"
    , "rumaos1234"
]


###################
# MySQL (servidor Redmas)
###################
#host='localhost',
#port='3306'
#database='Electronics',
#user='pynative',
#password='pynative@#29'

loginMySQL = [
    "db-mysql-redmas-do-user-3119335-0.a.db.ondigitalocean.com"
    ,"25060"
    ,"red_mas_prod"
    ,"consulta"
    ,"tuepo7ne4syhu6n0"
]


###################
# Google Sheet "Cheques"
# Can be obtain from the Share button at the get link section
# https://docs.google.com/spreadsheets/d/
#   1n6gNasdrXYZVXN73-C3XP0bbBY-1KIKSKumakoaf2xM <--This is the important part
#   /edit?usp=sharing
###################

googleSheet_InfoKamel = "1n6gNh0orQpbVXN73-C3XPoaaBY-1KIKSAqY7koaf2xM"

googleSheet_DevolucionesYER = "1RjRdp8qEnEflWj9TZkkROOMp4JYgYaa-QtaLZyJr9qE"