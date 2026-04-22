#include<iostream>
#include<string>
#include<set>

using namespace std;


class Solution {

public:
    Solution(string str);

public:
    int lengthOfLongestSubstring(string s) {
        int count = 1;
        if (s.length() == 0)
        {
            return 0;
        }
        for(int i = 0; i < s.length() - 1; i++)
        {
            std::set<char> myset;
            myset.insert(s[i]);
            int lth = 1, j = i + 1;
            
            
            while(j < s.length() - 1 && s[j] != s[i])
            {
                if(myset.find(s[j]) == myset.end())
                {
                    myset.insert(s[j]);
                    lth = myset.size();
                    cout << lth;
                    j++;
                }
                else
                {
                    break;
                }
                
            //     cout << lth;
            }
            if (lth > count)
            {
                count = lth;
            }
            cout << "\n" << s[i] << count ;
            
        }
        
        return count;
    }
};