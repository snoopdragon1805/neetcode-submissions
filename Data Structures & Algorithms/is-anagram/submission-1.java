class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length())
            return false;
        int [] hm=new int[26];
        for(int i=0;i<hm.length;i++){
            hm[i]=0;
        }

        int [] hm1=new int[26];
        for(int i=0;i<hm1.length;i++){
            hm1[i]=0;
        }
        for(int i=0;i<s.length();i++){
            hm[(int)(s.charAt(i))-97]++;
            hm1[(int)(t.charAt(i))-97]++;
        }
        for(int i=0;i<hm.length;i++){
            if(hm[i]!=hm1[i])
            return false;

        }
        return true;
    }
}
