package es.curso.clases;

public class Direccion {
	
	private String calle;
	private int cp;
	private int numero;
	
	public Direccion() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Direccion(String calle, int cp, int numero) {
		super();
		this.calle = calle;
		this.cp = cp;
		this.numero = numero;
	}

	public String getCalle() {
		return calle;
	}

	public void setCalle(String calle) {
		this.calle = calle;
	}

	public int getCp() {
		return cp;
	}

	public void setCp(int cp) {
		this.cp = cp;
	}

	public int getNumero() {
		return numero;
	}

	public void setNumero(int numero) {
		this.numero = numero;
	}

	@Override
	public String toString() {
		return "Direccion [calle=" + calle + ", cp=" + cp + ", numero=" + numero + "]";
	}
}
