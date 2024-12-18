package es.curso.clases;

public class Usuario {
	
	private String nombre;
	private int edad;
	private Direccion dir;
	
	public Usuario() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Usuario(String nombre, int edad, Direccion dir) {
		super();
		this.nombre = nombre;
		this.edad = edad;
		this.dir = dir;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public int getEdad() {
		return edad;
	}

	public void setEdad(int edad) {
		this.edad = edad;
	}

	public Direccion getDir() {
		return dir;
	}

	public void setDir(Direccion dir) {
		this.dir = dir;
	}

	@Override
	public String toString() {
		return "Usuario [nombre=" + nombre + ", edad=" + edad + ", dir=" + dir + "]";
	}
	
}
