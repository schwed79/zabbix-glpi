## Autor: Janssen dos Reis Lima / janssenreislima@gmail.com>
## Ultima atualizacao: 18/02/2016
## Observacoes: Este script eh executado automaticamente apos a abertura do ticket no GLPI
##
## 2019/Dec/26


from zabbix_api import ZabbixAPI
import sys
 
server = "http://localhost/zabbix"
username = "Admin"             
password = "zabbix"     
 
connection = ZabbixAPI(server = server)
connection.login(username, password)

ack = connection.event.acknowledge({"eventids": sys.argv[1], "message": "Ticket " + str(sys.argv[2]) + " created in GLPI."})
