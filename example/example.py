from pyconfigini import parse_ini

# Get staging settings
config = parse_ini('example.ini', 'staging')

# Demonstrate inheritance
print config.application.name # prints 'example'

# Demonstrte overrides
print config.database.host # prints 'staging.db.example.com'