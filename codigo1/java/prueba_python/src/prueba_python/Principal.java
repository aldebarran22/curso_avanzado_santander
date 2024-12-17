package prueba_python;

import org.python.util.PythonInterpreter;

public class Principal {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		try {
			PythonInterpreter python = new PythonInterpreter();

			python.execfile("scripts/codigo.py");
			python.close();
			
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}

}
