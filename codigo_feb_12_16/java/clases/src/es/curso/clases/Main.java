package es.curso.clases;

import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		List<Usuario> users;
		
		users = new ArrayList<Usuario>();
		users.add(new Usuario("Ana", "Pérez", 45));
		users.add(new Usuario("Raúl", "Pérez", 25));
		users.add(new Usuario("Eva", "Pérez", 65));
		
		System.out.println(users);
		
	}

}
