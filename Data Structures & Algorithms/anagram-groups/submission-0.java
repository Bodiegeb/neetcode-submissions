class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        for(String str : strs){
            char[] list = str.toCharArray();
            Arrays.sort(list);
            String key = new String(list);
            if(!map.containsKey(key)){
                map.put(key, new ArrayList<String>());
            }
            map.get(key).add(str);
            
        }
        return new ArrayList<>(map.values());    
    }
}