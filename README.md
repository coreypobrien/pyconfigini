README
======
pyconfigini is a .ini style config file parser modeled on [Zend_Config_Ini](http://framework.zend.com/manual/en/zend.config.adapters.ini.html).  
Lines beginning with '#' are treated as comments.  

It supports section inheritance and uses the '.' character for namespacing values. E.g.
	
	# This is a global value
	global = True
	 
    [production]
    database.host = db.example.com
    database.port = 3306
    database.user = prod
    database.pass = prod_password

    [dev : production]
    database.host = localhost
    database.user = dev
    database.pass = dev_password

pyconfigini exposes one function `parse_ini` which takes 2 arguments: the path (relative or absoloute) of the config file to be parsed, and (optionally) the section to load.  
If no section is specified it will load all sections and the section name must be used to access values. E.g.

    config = parse_ini('example.ini')
    print config.global # prints (boolean) True
    print config.production.database.host

    vs.

    config = parse_ini('example.ini', 'production')
    print config.global # prints (boolean) True
    print config.database.host

