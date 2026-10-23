 import os, sqlite3, subprocess

  def buscar_usuario(db, nombre):
      # SQL construido por concatenación
      return db.execute("SELECT * FROM usuarios WHERE nombre = '" + nombre + "'").fetchall()

  def ejecutar(cmd):
      return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout
