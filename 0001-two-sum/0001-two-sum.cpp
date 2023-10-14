class Solution {
public:
    static vector<int> twoSum(vector<int>& nums, int target) {
        std::vector<int>::size_type n = nums.size();
        std::unordered_map<int, int> mp; // val -> index

        for (std::vector<int>::size_type i = 0; i < n; i++) {
            int compliment = target - nums[i];
            if (mp.find(compliment) != mp.end()) {
                return {mp[compliment], static_cast<int>(i)};
            }
            mp.insert({nums[i], static_cast<int>(i)});
        }
        return {};
    }
};