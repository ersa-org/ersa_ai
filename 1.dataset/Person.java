

class Person{
  public String name;
  public int age;

  Person(String name,int age){
    this.name = name;
    this.age = age;
  }

  public static void main(String[] args) {
    Person p1 =new Person("robin", 33)  ;
    System.out.println(p1.name);
    System.out.println(p1.age);
  }
}
