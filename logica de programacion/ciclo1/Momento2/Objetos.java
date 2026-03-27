import java.util.HashMap;

public class Objetos{
    public static void main (String[]args){
        HashMap<String, String> estudiante = new HashMap<>();

        estudiante.put("Nombre", "Ana");
        estudiante.put("Edad", "22");
        estudiante.put("Carrera", "Sistemas");

        System.out.println("Nombre" + estudiante.get ("Carrera"));

        if (estudiante.containsKey("Nota")){
            System.out.println("Nota: " + estudiante.get("Nota"));

        }else{
            System.out.println("El estudiante no tiene nota.");
        }
        estudiante.remove("Edad");
    }

}