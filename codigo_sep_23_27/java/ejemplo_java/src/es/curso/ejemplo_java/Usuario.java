package es.curso.ejemplo_java;

import java.util.ArrayList;
import java.util.List;

public class Usuario {
	
	private String user;
	private String pass;
	private List<Permiso> permisos;
	
	public Usuario() {		
		super();
		// TODO Auto-generated constructor stub
	}

	public Usuario(String user, String pass) {
		super();
		this.user = user;
		this.pass = pass;
		this.permisos = new ArrayList<>();
	}
	
	public void addPermiso(Permiso permiso) {
		this.permisos.add(permiso);
	}

	public String getUser() {
		return user;
	}

	public void setUser(String user) {
		this.user = user;
	}

	public String getPass() {
		return pass;
	}

	public void setPass(String pass) {
		this.pass = pass;
	}

	public List<Permiso> getPermisos() {
		return permisos;
	}

	public void setPermisos(List<Permiso> permisos) {
		this.permisos = permisos;
	}

	@Override
	public String toString() {
		return "Usuario [user=" + user + ", pass=" + pass + ", permisos=" + permisos + "]";
	}
}
