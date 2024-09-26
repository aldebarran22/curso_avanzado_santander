package es.curso.app;

import org.python.util.PythonInterpreter;

public class Principal {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		PythonInterpreter python = new PythonInterpreter();

		try {
			python.execfile("scripts/modulo.py");
			System.out.println("Se ha generado un fichero");

		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}

}
