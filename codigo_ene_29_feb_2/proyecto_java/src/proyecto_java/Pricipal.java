package proyecto_java;

import org.python.util.PythonInterpreter;

public class Pricipal {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		PythonInterpreter interprete = new PythonInterpreter();
		
		String path = "D:/OneDrive/Escritorio/python_avanzado_santander/repositorio/codigo_ene_29_feb_2/ficheros.py";
		interprete.execfile(path);
		System.out.println("Ejecutando script ...");
		interprete.close();
	}

}
