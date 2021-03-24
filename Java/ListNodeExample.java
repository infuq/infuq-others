public class ListNodeExample {
    
    public static void main(String[] args) {

        ListNode n1 = new ListNode(3);
        ListNode n2 = new ListNode(9);
        ListNode n3 = new ListNode(12);
        
        // n1 -> n2 -> n3 -> null
        n1.setNext(n2);
        n2.setNext(n3);

        // 遍历链表
        /*
        ListNode head = n1;
        while (head != null) {
            System.out.println(head.getData());
            head = head.getNext();
        }
        */

        // 反转链表
        ListNode head = null;
        ListNode cur = n1;
        while (cur != null) {
            ListNode next = cur.getNext();
            cur.setNext(head);
            head = cur;
            cur = next;
        }

        while (head != null) {
            System.out.println(head.getData());
            head = head.getNext();
        }




    }

}
