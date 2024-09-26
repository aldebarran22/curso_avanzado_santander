package es.curso.ejemplo_java;

public class Permiso {
	
	private String permiso;
	private char tipoAcceso;
	
	
	public Permiso() {
		super();
		// TODO Auto-generated constructor stub
	}


	public Permiso(String permiso, char tipoAcceso) {
		super();
		this.permiso = permiso;
		this.tipoAcceso = tipoAcceso;
	}


	public String getPermiso() {
		return permiso;
	}


	public void setPermiso(String permiso) {
		this.permiso = permiso;
	}


	public char getTipoAcceso() {
		return tipoAcceso;
	}


	public void setTipoAcceso(char tipoAcceso) {
		this.tipoAcceso = tipoAcceso;
	}


	@Override
	public String toString() {
		return "Permiso [permiso=" + permiso + ", tipoAcceso=" + tipoAcceso + "]";
	}
	
	

}
