import os

def getpostgresqlenv(options,buildout):
    os.environ['EXTRA_LDAP_LIBS'] = os.environ['LDFLAGS']
# vim:set ts=4 sts=4 et  :
