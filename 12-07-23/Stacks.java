public class Stacks {
	private static Object[] stackarray;
	private static int size;
	private int top;
	public Stacks(int size)
	{
		this.size=size;
		this.top=-1;
		stackarray=new Object[size];
	}
	public void push(Object value)
	{
		if(top==size-1 ) {
			System.out.println("Stack is Full");
		}
		else {
		top++;
		stackarray[top]=value;
		}
	}
	public Object pop()
	{
		if(top==-1) {
			System.out.println("Stack is Empty");
			return -1;
		}
		else
		{
			int oldtop=top;
			top--;
			stackarray[oldtop]=null;
			return stackarray[top];
		}
	}
	public Object peek()
	{
		return stackarray[top];
	}
	public static void main(String[] args) {
		Stacks s=new Stacks(5);
		s.push(10);
		s.push(20);
		s.push(30);
		s.push(40);
		s.push(50);
		s.pop();
		for(int i=0;i<size;i++)
			System.out.println(stackarray[i]);
	}

}