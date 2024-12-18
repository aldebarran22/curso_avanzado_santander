package interprete;

import org.python.util.PythonInterpreter;

public class Principal {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		PythonInterpreter python;

		try {
			python = new PythonInterpreter();
			python.execfile("scripts/modulo.py");
			python.close();
			
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}
}
