package es.curso.app;

public class Usuario {
	
	private String login;
	private String pass;
	
	private Direccion dir;

	public Usuario() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Usuario(String login, String pass, Direccion dir) {
		super();
		this.login = login;
		this.pass = pass;
		this.dir = dir;
	}

	public String getLogin() {
		return login;
	}

	public void setLogin(String login) {
		this.login = login;
	}

	public String getPass() {
		return pass;
	}

	public void setPass(String pass) {
		this.pass = pass;
	}

	public Direccion getDir() {
		return dir;
	}

	public void setDir(Direccion dir) {
		this.dir = dir;
	}

	@Override
	public String toString() {
		return "Usuario [login=" + login + ", pass=" + pass + ", dir=" + dir + "]";
	}
	
	

}
