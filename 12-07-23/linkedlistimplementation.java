class Node{
    public Object item;
    public Node next;//pointing to next node
}
public class linkedlistimplementation {
    private int size;
    private Node head;

   public linkedlistimplementation(){
        this.size=0;
        this.head= null;   
   }
   public void insertingnode(String i){
    Node node= new Node();
    node.item= i;
    Node current=this.head;
    if (this.head==null){
        this.head=node;
        this.head.next= null;
        this.size=1;
        System.out.println(this.head.toString());
    }else{
        while(current.next!=null){
            current=current.next;
        }
        current.next=node;
        node.next=null;
        this.size+=1;
    }
   }
    }