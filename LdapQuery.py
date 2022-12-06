import sys
import ldap
import re

### Bind and test connection to LDAP server
l = ldap.initialize('ldap://<ldap_server>')
username = "<user full path>
password = "<password>
basedn = "<basedn>"
scope = ldap.SCOPE_SUBTREE
try:
  l.protocol_version = ldap.VERSION3
  l.simple_bind_s(username, password)
  valid = True
except ldap.INVALID_CREDENTIALS:
  print ("Your username or password is incorrect.")
  sys.exit(0)
except ldap.LDAPError as e:
  if type(e.message) == dict and e.message.has_key('desc'):
    print (e.message['desc'])
  else:
    print (e)
  sys.exit(0)
  
def getGroups(username):
  searchFilter = f'(&objectClass=posixgroup)(memberUid={username}))'
  searchAttribute = ["dn"]
  
  ldap_groups = l.search_s(basedn,scope,searchFilter,searchAttribute)
  ldap_groups_string = str(ldap_groups)
  ldap_groups_list = re.findall(r'cn=(<group>|<group>|<group>)', ldap_groups_string)
  return ldap_group_list

def getOrgs(username):
  searchFilter = f'(&objectClass=posixgroup)(memberUid={username}))'
  searchAttribute = ["dn"]
  
  ldap_groups = l.search_s(basedn,scope,searchFilter,searchAttribute)
  ldap_groups_string = str(ldap_groups)
  ldap_groups_list = re.findall(r'cn=(<org>|<org>|<org>)', ldap_groups_string)
  return ldap_group_list

def getAllUsers():
  searchFilter = "(&(objectClass=posixaccount)(objectClass=person)(objectClass=organizationalperson))"
  searchAttribute = ["dn"]
  ldap_users = l.search_s(basedn,scope,searchFilter,searchAttribute)
  ldap_users_string = str(ldap_users)
  ldap_user_list = re.findall(r'uid=(\w*)', ldap_users_string)
  return ldap_user_list

### write passwd file with above info
def printUsersandGroups():
  with open('<path to passwd>', 'w') as f:
    
    userList = getAllusers()
    for user in userList:
      
      groups_string=' '.join(map(str,getGroups(user)))
      orgs_string=' '.join(map(str,getOrgs(user)))
      user_passwd_entry = "{}, {}, {}".format(user, groups_string, orgs_string)
      f.writelines([user_passwd_entry, '\n'])
  
  f.close()
  
printUsersandGroups()
