function topKFrequent(nums: number[], k: number): number[] {

    function checkFrequency(nums: number[], k: number) {
        const map = new Map<number, number>()

        for (const frequency of nums) {
            map.set(frequency, (map.get(frequency) || 0) + 1)
        }

        const maxHeap: number[] = [];
        for (const [num, frequency] of map.entries()) {
            maxHeap.push(num);
            if (maxHeap.length > k) {
                maxHeap.sort((a, b) => map.get(b)! - map.get(a)!);
                maxHeap.pop();
            }
        }

        return maxHeap;
    }

return checkFrequency(nums, k)

}


