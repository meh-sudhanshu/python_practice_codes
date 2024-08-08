import java.util.HashMap;

class MaximumSum{
    public static void main(String[] args) {
        int[] arr = {-3,-3,2,9,12,8,16,7,16,-3,2};
        int ws = 5;
        int ans = getMaximumSum(arr,ws);
        System.out.println(ans);
    }

    private static int getMaximumSum(int[] arr, int ws) {
        int ans = Integer.MIN_VALUE;
        int cs = 0, ps = 0;
        int i = 0, j = ws-1;
        HashMap<Integer,Integer> myMap = new HashMap<>();
        while (j < arr.length) {
            if(i == 0){
                for(int k=i;k<=j;k++){
                    cs+=arr[k];
                    int oldValue  = myMap.getOrDefault(arr[k], 0);
                    oldValue+=1;
                    myMap.put(arr[k],oldValue);
                }
                if(cs > ans && myMap.size() == ws){
                    ans = cs;
                }
                ps = cs;
            }else{

                cs = ps - arr[i-1]+arr[j];
                int oldFrequency = myMap.get(arr[i-1]);
                if(oldFrequency == 1){
                    myMap.remove(arr[i-1]);
                }else{
                    oldFrequency-=1;
                    myMap.put(arr[i-1],oldFrequency);
                }

                if(myMap.containsKey(arr[j])){
                    int oFrequency = myMap.get(arr[j]);
                    oFrequency+=1;
                    myMap.put(arr[j],oFrequency);
                }else{
                    myMap.put(arr[j],1);
                }

                if(myMap.size() == ws && cs > ans){
                    ans = cs;
                }

                ps = cs;

            }
            i+=1;
            j+=1;
        }
    
        return ans;
    
    }


  


}