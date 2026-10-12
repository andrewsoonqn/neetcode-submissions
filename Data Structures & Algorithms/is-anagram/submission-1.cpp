class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> count(26, 0);

        for (const auto& c : s) {
            ++count[c-'a'];
        }

        for (const auto& c : t) {
            --count[c-'a'];
        }
        
        for (const auto& lol : count) {
            if (lol != 0) return false;
        }
        return true;
    }

};
