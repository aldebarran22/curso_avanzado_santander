package es.curso.clases_java;

import java.util.List;

public class Usuario {
	
	private String nombre;
	private String login;
	private String password;
	
	private List<Permisos> permisos;

	public Usuario() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Usuario(String nombre, String login, String password, List<Permisos> permisos) {
		super();
		this.nombre = nombre;
		this.login = login;
		this.password = password;
		this.permisos = permisos;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getLogin() {
		return login;
	}

	public void setLogin(String login) {
		this.login = login;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public List<Permisos> getPermisos() {
		return permisos;
	}

	public void setPermisos(List<Permisos> permisos) {
		this.permisos = permisos;
	}
	
	public void addPermiso(Permisos permiso) {
		this.permisos.add(permiso);
	}

	@Override
	public String toString() {
		return "Usuario [nombre=" + nombre + ", login=" + login + ", password=" + password + ", permisos=" + permisos
				+ "]";
	}
	
}
