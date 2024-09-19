package prueba_jython;

import org.python.util.PythonInterpreter;

public class Principal {

	public static void main(String[] args) {
		PythonInterpreter python;

		try {
			python = new PythonInterpreter();
			python.execfile("modulo.py");
			
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}

}
