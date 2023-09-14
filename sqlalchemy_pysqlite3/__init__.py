from sqlalchemy.dialects import registry
from sqlalchemy.dialects.sqlite.pysqlite import SQLiteDialect_pysqlite

class SQLiteDialect_pysqlite3(SQLiteDialect_pysqlite):

  supports_statement_cache = True
  
  @classmethod
  def import_dbapi(cls):
    from pysqlite3 import dbapi2 as result
    return result

registry.register(
  "sqlite.pysqlite3",
  __name__,
  "SQLiteDialect_pysqlite3"
)
