package interprete;

import org.python.util.PythonInterpreter;

public class Principal {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		PythonInterpreter python;
		
		python = new PythonInterpreter();
		python.exec("import sys");
		python.exec("print(sys.version)");
		python.close();
	}

}
