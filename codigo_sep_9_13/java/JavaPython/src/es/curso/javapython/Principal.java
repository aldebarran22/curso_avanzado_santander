package es.curso.javapython;

import org.python.util.PythonInterpreter;

public class Principal {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		PythonInterpreter python = new PythonInterpreter();
		python.execfile("scripts/codigo.py");
				
	}

}
