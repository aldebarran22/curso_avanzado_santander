package es.curso.clases_java;

public class Permisos {

	private char acceso;
	private String detalle;
	
	public Permisos() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Permisos(char acceso, String detalle) {
		super();
		this.acceso = acceso;
		this.detalle = detalle;
	}

	public char getAcceso() {
		return acceso;
	}

	public void setAcceso(char acceso) {
		this.acceso = acceso;
	}

	public String getDetalle() {
		return detalle;
	}

	public void setDetalle(String detalle) {
		this.detalle = detalle;
	}

	@Override
	public String toString() {
		return "Permisos [acceso=" + acceso + ", detalle=" + detalle + "]";
	}
}
