import sqlite3
import bcrypt
from db.connection import get_connection

def criar_usuario(usuario, senha, papel):
	senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()
	conn = get_connection()
	try:
		conn.execute('INSERT INTO usuarios (usuario, senha_hash, papel) VALUES (?, ?, ?)',
					 (usuario, senha_hash, papel))
		conn.commit()
		return True
	except sqlite3.IntegrityError:
		return False
	finally:
		conn.close()

def listar_usuarios():
	conn = get_connection()
	cur = conn.execute('SELECT id, usuario, papel FROM usuarios')
	usuarios = cur.fetchall()
	conn.close()
	return usuarios

def atualizar_usuario(id, novo_usuario=None, nova_senha=None, novo_papel=None):
	conn = get_connection()
	campos = []
	valores = []
	if novo_usuario:
		campos.append('usuario = ?')
		valores.append(novo_usuario)
	if nova_senha:
		senha_hash = bcrypt.hashpw(nova_senha.encode(), bcrypt.gensalt()).decode()
		campos.append('senha_hash = ?')
		valores.append(senha_hash)
	if novo_papel:
		campos.append('papel = ?')
		valores.append(novo_papel)
	if not campos:
		conn.close()
		return False
	valores.append(id)
	sql = f'UPDATE usuarios SET {", ".join(campos)} WHERE id = ?'
	conn.execute(sql, valores)
	conn.commit()
	conn.close()
	return True

def remover_usuario(id):
	conn = get_connection()
	conn.execute('DELETE FROM usuarios WHERE id = ?', (id,))
	conn.commit()
	conn.close()
	return True

def autenticar(usuario, senha):
	conn = get_connection()
	cur = conn.execute('SELECT senha_hash, papel FROM usuarios WHERE usuario = ?', (usuario,))
	row = cur.fetchone()
	conn.close()
	if row:
		senha_hash, papel = row
		if bcrypt.checkpw(senha.encode(), senha_hash.encode()):
			return True, papel
	return False, None

