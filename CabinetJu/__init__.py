import pymysql

# Spoof version for Django 4.x compatibility
pymysql.version_info = (2, 2, 8, "final", 0)
pymysql.install_as_MySQLdb()
