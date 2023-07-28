import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class StudentDb {
    private Map<String, Integer> studentMarks;

    public StudentDb() {
        studentMarks = new HashMap<>();
    }

    public void addStudent(String name, int marks) {
        studentMarks.put(name, marks);
    }

    public void printStudentInfo(String name) {
        if (studentMarks.containsKey(name)) {
            int marks = studentMarks.get(name);
            System.out.println("Student Name: " + name + ", Marks: " + marks);
        } else {
            System.out.println("Student not found in the database.");
        }
    }

    public void editStudentName(String oldName, String newName) {
        if (studentMarks.containsKey(oldName)) {
            int marks = studentMarks.remove(oldName);
            studentMarks.put(newName, marks);
            System.out.println("Name updated successfully.");
        } else {
            System.out.println("Student not found in the database.");
        }
    }

    public void editStudentMarks(String name, int newMarks) {
        if (studentMarks.containsKey(name)) {
            studentMarks.put(name, newMarks);
            System.out.println("Marks updated successfully.");
        } else {
            System.out.println("Student not found in the database.");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        StudentDb studentDb = new StudentDb();

        while (true) {
            System.out.println("\nMenu:");
            System.out.println("1. Add Student");
            System.out.println("2. Print Student Information");
            System.out.println("3. Edit Student Name");
            System.out.println("4. Edit Student Marks");
            System.out.println("5. Exit");
            System.out.print("Enter your choice (1/2/3/4/5): ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume the newline character after nextInt()

            switch (choice) {
                case 1:
                    System.out.print("Enter the student name: ");
                    String name = scanner.nextLine();
                    System.out.print("Enter the student marks: ");
                    int marks = scanner.nextInt();
                    studentDb.addStudent(name, marks);
                    scanner.nextLine(); // Consume the newline character after nextInt()
                    break;
                case 2:
                    System.out.print("Enter the student name to print information: ");
                    name = scanner.nextLine();
                    studentDb.printStudentInfo(name);
                    break;
                case 3:
                    System.out.print("Enter the student name to edit: ");
                    String oldName = scanner.nextLine();
                    System.out.print("Enter the new student name: ");
                    String newName = scanner.nextLine();
                    studentDb.editStudentName(oldName, newName);
                    break;
                case 4:
                    System.out.print("Enter the student name to edit marks: ");
                    name = scanner.nextLine();
                    System.out.print("Enter the new marks: ");
                    int newMarks = scanner.nextInt();
                    studentDb.editStudentMarks(name, newMarks);
                    scanner.nextLine(); // Consume the newline character after nextInt()
                    break;
                case 5:
                    System.out.println("Exiting program. Goodbye!");
                    scanner.close();
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
}
